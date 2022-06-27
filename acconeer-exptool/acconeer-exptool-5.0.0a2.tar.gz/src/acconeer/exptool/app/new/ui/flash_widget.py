from __future__ import annotations

import importlib
import logging
import traceback
from typing import Optional

import serial

from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QCloseEvent, QMovie
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QFileDialog,
    QFormLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from acconeer.exptool.app import resources  # type: ignore[attr-defined]
from acconeer.exptool.app.new.app_model import AppModel, ConnectionState
from acconeer.exptool.app.new.ui.misc import ExceptionWidget
from acconeer.exptool.flash import find_flash_port, flash_image  # type: ignore[import]


log = logging.getLogger(__name__)


class _FlashThread(QThread):
    flash_failed = Signal(Exception, str)
    flash_done = Signal()

    def __init__(self, bin_file: str, flash_port: serial.tools.list_ports.ListPortInfo) -> None:
        super().__init__()
        self.bin_file = bin_file
        self.flash_port = flash_port

    def run(self) -> None:
        try:
            flash_image(self.bin_file, self.flash_port)
            self.flash_done.emit()
        except Exception as e:
            log.error(str(e))
            self.flash_failed.emit(e, traceback.format_exc())


class _FlashDialog(QDialog):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.setWindowTitle("Flash tool")
        self.setMinimumWidth(350)

        vbox = QVBoxLayout(self)
        vbox.setAlignment(Qt.AlignCenter)
        vbox.setSizeConstraint(QVBoxLayout.SetMinimumSize)

        self.loading = QLabel()
        self.loading.setAlignment(Qt.AlignCenter)

        loader_gif = None
        with importlib.resources.path(resources, "loader.gif") as path:
            loader_gif = path

        self.flash_movie = QMovie(str(loader_gif))
        self.loading.setMovie(self.flash_movie)
        vbox.addWidget(self.loading)

        self.flash_label = QLabel(self)
        self.flash_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        self.flash_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.flash_label)

        self.setLayout(vbox)

    def flash(self, bin_file, flash_port):
        self.flash_thread = _FlashThread(bin_file, flash_port)
        self.flash_thread.started.connect(self._flash_start)
        self.flash_thread.finished.connect(self.flash_thread.deleteLater)
        self.flash_thread.finished.connect(self._flash_stop)
        self.flash_thread.flash_done.connect(self._flash_done)
        self.flash_thread.flash_failed.connect(self._flash_failed)

        self.flash_thread.start()
        self._flashing = True
        self.exec()

    def _flash_start(self) -> None:
        self.flash_label.setText("Flashing...")
        self.flash_movie.start()

    def _flash_stop(self) -> None:
        self.flash_movie.stop()
        self.loading.hide()
        self._flashing = False

    def _flash_done(self) -> None:
        self.flash_label.setText("Flashing done!")

    def _flash_failed(self, exception: Exception, traceback_str: Optional[str]) -> None:
        self.flash_label.setText("Flashing failed!")
        ExceptionWidget(self, exc=exception, traceback_str=traceback_str).exec()

    def closeEvent(self, event: QCloseEvent) -> None:
        if self._flashing:
            self.flash_thread.terminate()
            self.flash_thread.wait()
        super().closeEvent(event)


class _FlashPopup(QDialog):
    def __init__(self, app_model: AppModel, parent: QWidget) -> None:
        super().__init__(parent)

        self.app_model = app_model

        self.setWindowTitle("Flash tool")
        self.setMinimumWidth(350)

        self.flash_port = None
        self.bin_file = None

        layout = QFormLayout(self)

        self.file_label = QLineEdit("<Select a bin file>")
        self.file_label.setReadOnly(True)

        browse_button = QPushButton("Browse", self)
        browse_button.clicked.connect(self._browse_file)
        layout.addRow(browse_button, self.file_label)

        self.port_combo_box = QComboBox(self)
        self.port_combo_box.currentTextChanged.connect(self._on_port_combo_box_change)
        layout.addWidget(self.port_combo_box)

        self.flash_button = QPushButton("Flash", self)
        self.flash_button.clicked.connect(self._flash)
        self.flash_button.setEnabled(False)
        layout.addRow(self.flash_button)

        self.setLayout(layout)

        self.browse_file_dialog = QFileDialog(None)
        self.browse_file_dialog.setNameFilter("Bin files (*.bin)")

        self.flash_dialog = _FlashDialog(self)

        app_model.sig_notify.connect(self._on_app_model_update)

    def _browse_file(self) -> None:
        if self.browse_file_dialog.exec():
            filenames = self.browse_file_dialog.selectedFiles()
            self.bin_file = filenames[0]
            self.file_label.setText(self.bin_file)

        self.flash_button.setEnabled(self.flash_port is not None and self.bin_file is not None)

    def _flash(self) -> None:
        flash_port = find_flash_port(self.flash_port)

        self.flash_dialog.flash(self.bin_file, flash_port)

    def _on_port_combo_box_change(self) -> None:
        self.app_model.set_serial_connection_port(self.port_combo_box.currentData())
        self.flash_port = self.port_combo_box.currentData()

        self.flash_button.setEnabled(self.flash_port is not None and self.bin_file is not None)

    def _on_app_model_update(self, app_model: AppModel) -> None:
        self.port_combo_box.blockSignals(True)

        tagged_ports = app_model.available_tagged_ports

        self.port_combo_box.clear()
        for port, tag in tagged_ports:
            label = port if tag is None else f"{port} ({tag})"
            self.port_combo_box.addItem(label, port)

        index = self.port_combo_box.findData(app_model.serial_connection_port)
        self.port_combo_box.setCurrentIndex(index)
        self.flash_port = self.port_combo_box.currentData()

        self.port_combo_box.blockSignals(False)


class FlashButton(QPushButton):
    def __init__(self, app_model: AppModel, parent: QWidget) -> None:
        super().__init__(parent)

        self.app_model = app_model

        self.setFixedWidth(100)
        self.setText("Flash")

        app_model.sig_notify.connect(self._on_app_model_update)
        self.pop_up = _FlashPopup(app_model, self)
        self.clicked.connect(self._on_click)

    def _on_click(self) -> None:
        self.pop_up.exec()

    def _on_app_model_update(self, app_model: AppModel) -> None:
        self.setEnabled(app_model.connection_state == ConnectionState.DISCONNECTED)
