"""Languages Renderers"""
from needle.libs.renderers.__base import BaseRenderer


class MoustacheRenderer(BaseRenderer):
    def render(self, code: str):
        super().render(code)
