from abc import abstractmethod, abstractproperty
from re import Pattern
from typing import Union


class BaseAdapter:
    line_comments: list[Union[Pattern, str]] = []
    multiline_comments: list[Union[Pattern, str]] = []

    @abstractmethod
    def __init__(self):
        BaseAdapter.extensions = []
        BaseAdapter.line_comments = ["{{", "}}", "#"]
        BaseAdapter.multiline_comments = ["/*", "*/"]

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError

    @abstractmethod
    def __exit__(self):
        raise NotImplementedError

    def is_adapter(self, filename: str) -> bool:
        for ext in self.extensions:
            if filename.endswith(f".{ext}") if isinstance(ext, str) else ext.match(filename):
                return True
        return False
