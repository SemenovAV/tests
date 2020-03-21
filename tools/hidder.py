import sys
from io import StringIO


class Hider:
    def __init__(self, channels=('stdout',)):
        self._stomach = StringIO()
        self._orig = {ch: None for ch in channels}

    def __enter__(self):
        for ch in self._orig:
            self._orig[ch] = getattr(sys, ch)
            setattr(sys, ch, self)
        return self

    def write(self, string):
        self._stomach.write(string)

    def flush(self):
        pass

    def autopsy(self):
        return self._stomach.getvalue()

    def __exit__(self, *args):
        for ch in self._orig:
            setattr(sys, ch, self._orig[ch])
