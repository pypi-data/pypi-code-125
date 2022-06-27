from __future__ import annotations

from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QStackedWidget,
    QWidget,
)

from acconeer.exptool.app.new.app_model import AppModel, ConnectionInterface, ConnectionState
from acconeer.exptool.app.new.qt_subclasses import AppModelAwareWidget


class _ConnectAndDisconnectButton(QPushButton):
    def __init__(self, app_model: AppModel, parent: QWidget) -> None:
        super().__init__(parent)

        self.app_model = app_model

        self.setFixedWidth(100)

        app_model.sig_notify.connect(self._on_app_model_update)

        self.clicked.connect(self._on_click)

    def _on_click(self) -> None:
        if self.app_model.connection_state == ConnectionState.DISCONNECTED:
            self.app_model.connect_client()
        elif self.app_model.connection_state == ConnectionState.CONNECTED:
            self.app_model.disconnect_client()
        else:
            raise RuntimeError

    def _on_app_model_update(self, app_model: AppModel) -> None:
        TEXTS = {
            ConnectionState.DISCONNECTED: "Connect",
            ConnectionState.CONNECTING: "Connecting...",
            ConnectionState.CONNECTED: "Disconnect",
            ConnectionState.DISCONNECTING: "Disconnecting...",
        }
        ENABLED_STATES = {ConnectionState.CONNECTED, ConnectionState.DISCONNECTED}

        self.setText(TEXTS[app_model.connection_state])
        self.setEnabled(
            app_model.connection_state in ENABLED_STATES and app_model.plugin_state.is_steady
        )


class _SocketConnectionWidget(AppModelAwareWidget):
    def __init__(self, app_model: AppModel, parent: QWidget) -> None:
        super().__init__(app_model, parent)
        self.app_model = app_model

        self.setLayout(QHBoxLayout(self))
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.ip_line_edit = QLineEdit(self)
        self.ip_line_edit.setPlaceholderText("<IP address>")
        self.ip_line_edit.editingFinished.connect(self._on_line_edit)
        self.layout().addWidget(self.ip_line_edit)

    def _on_line_edit(self) -> None:
        self.app_model.set_socket_connection_ip(self.ip_line_edit.text())


class _SerialConnectionWidget(AppModelAwareWidget):
    def __init__(self, app_model: AppModel, parent: QWidget) -> None:
        super().__init__(app_model, parent)
        self.app_model = app_model

        self.setLayout(QHBoxLayout(self))
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.port_combo_box = QComboBox(self)
        self.port_combo_box.currentTextChanged.connect(self._on_combo_box_change)
        self.layout().addWidget(self.port_combo_box)

    def _on_combo_box_change(self) -> None:
        self.app_model.set_serial_connection_port(self.port_combo_box.currentData())

    def on_app_model_update(self, app_model: AppModel) -> None:
        self.port_combo_box.blockSignals(True)

        tagged_ports = app_model.available_tagged_ports

        self.port_combo_box.clear()
        for port, tag in tagged_ports:
            label = port if tag is None else f"{port} ({tag})"
            self.port_combo_box.addItem(label, port)

        index = self.port_combo_box.findData(app_model.serial_connection_port)
        self.port_combo_box.setCurrentIndex(index)

        self.port_combo_box.blockSignals(False)


class ClientConnectionWidget(AppModelAwareWidget):
    def __init__(self, app_model: AppModel, parent: QWidget) -> None:
        super().__init__(app_model, parent)

        self.app_model = app_model

        self.setLayout(QHBoxLayout(self))
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.interface_dd = QComboBox(self)
        self.layout().addWidget(self.interface_dd)

        self.interface_dd.addItem("Socket", userData=ConnectionInterface.SOCKET)
        self.interface_dd.addItem("Serial", userData=ConnectionInterface.SERIAL)

        self.interface_dd.currentIndexChanged.connect(self._on_interface_dd_change)

        self.stacked = QStackedWidget(self)
        self.stacked.setStyleSheet("QStackedWidget {background-color: transparent;}")
        self.stacked.addWidget(_SocketConnectionWidget(app_model, self.stacked))
        self.stacked.addWidget(_SerialConnectionWidget(app_model, self.stacked))
        self.layout().addWidget(self.stacked)

        self.layout().addWidget(_ConnectAndDisconnectButton(app_model, self))
        self.layout().addStretch(1)

    def _on_interface_dd_change(self) -> None:
        self.app_model.set_connection_interface(self.interface_dd.currentData())

    def on_app_model_update(self, app_model: AppModel) -> None:
        self.stacked.setEnabled(
            app_model.connection_state == ConnectionState.DISCONNECTED,
        )
        self.interface_dd.setEnabled(
            app_model.connection_state == ConnectionState.DISCONNECTED,
        )

        interface_index = self.interface_dd.findData(app_model.connection_interface)
        if interface_index == -1:
            raise RuntimeError

        self.interface_dd.setCurrentIndex(interface_index)
        self.stacked.setCurrentIndex(interface_index)


class GenerationSelection(QComboBox):
    def __init__(self, app_model: AppModel, parent: QWidget) -> None:
        super().__init__(parent)

        self.addItem("A121")
        self.setEnabled(False)
