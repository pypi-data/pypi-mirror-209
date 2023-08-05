from dataclasses import dataclass, field
import pendulum
from typing import Optional


class MetaIterator:

    def __init__(self, meta_class):
        self._class_attrs = [a for a in dir(meta_class)if not a.startswith('__') and not callable(getattr(meta_class, a))]
        self._class_size = len(self._class_attrs)
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < self._class_size:
            element = self._class_attrs[self._current_index]
            self._current_index += 1
            return element
        raise StopIteration


@dataclass
class MetaData:

    record_source: Optional[str] = None
    extraction_timestamp: Optional[pendulum.DateTime] = None
    tags: Optional[list] = field(default_factory=list)
    dump_uri: Optional[str] = ''
    records_extracted: int = 0
    is_restored: bool = False

    def __iter__(self):
        return MetaIterator(self)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def __eq__(self, other):
        if isinstance(other, MetaData):
            return self.__dict__ == other.__dict__
        elif isinstance(other, dict):
            return self.__dict__ == other
        return NotImplemented

    def __contains__(self, item):
        if isinstance(item, MetaData):
            return item.items() <= self.items()
        elif isinstance(item, dict):
            return item.items() <= self.__dict__.items()
        return False

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def items(self):
        return self.__dict__.items()