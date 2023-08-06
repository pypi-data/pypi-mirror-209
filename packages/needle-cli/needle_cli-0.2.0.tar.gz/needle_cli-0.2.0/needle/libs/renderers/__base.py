"""Languages Renderers"""
from abc import abstractmethod


class BaseRenderer:

    @abstractmethod
    def render(self, code: str):
        raise NotImplementedError
