"""..."""
from typing import Iterator

from aligo.core.Config import ADRIVE_V1_FILE_DUPLICATE_LIST
from aligo.response import DuplicateItem, DuplicateListResponse
from .BaseAligo import BaseAligo


class Duplicate(BaseAligo):
    """..."""

    def _core_duplicate_list(self, drive_id: str = None) -> Iterator[DuplicateItem]:
        """..."""
        yield from self._list_file(ADRIVE_V1_FILE_DUPLICATE_LIST, {'drive_id': drive_id}, DuplicateListResponse)
