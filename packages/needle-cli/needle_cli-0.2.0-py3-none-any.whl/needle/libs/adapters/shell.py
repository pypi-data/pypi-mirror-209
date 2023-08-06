from needle.libs.adapters.__base import BaseAdapter


class ShellAdapter(BaseAdapter):
    def __enter__(self):
        pass

    def __exit__(self):
        pass

    def __init__(self):
        pass

class BashAdapter(ShellAdapter):
    pass

class ZshAdapter(ShellAdapter):
    pass
