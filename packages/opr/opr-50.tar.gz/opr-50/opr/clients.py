# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from .command import Command
from .handler import Handler
from .listens import Listens


def __dir__():
    return (
            "Client",
           )


__all__ = __dir__()


class Client(Handler):

    def __init__(self):
        Handler.__init__(self)
        Listens.add(self)
        self.register('command', Command.handle)

    def announce(self, txt):
        self.raw(txt)

    def raw(self, txt):
        pass

    def say(self, channel, txt):
        self.raw(txt)
