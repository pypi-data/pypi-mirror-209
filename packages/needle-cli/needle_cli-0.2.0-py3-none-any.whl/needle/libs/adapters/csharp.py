from re import Pattern
from typing import Union

from needle.libs.adapters.__base import BaseAdapter


class CSharpAdapter(BaseAdapter):
    line_comments: list[Union[Pattern, str]] = []
    multiline_comments: list[Union[Pattern, str]] = []

    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def __init__(self):
        pass
