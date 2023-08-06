# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import inspect


from .errored import Errors
from .objects import Object


def __dir__():
    return (
            'Command',
            'command',
            'scan'
           )


__all__ = __dir__()


class Command(Object):

    cmds = Object()

    @staticmethod
    def add(cmd, func):
        setattr(Command.cmds, cmd, func)

    @staticmethod
    def handle(evt):
        evt.parse(evt.txt)
        func = getattr(Command.cmds, evt.cmd, None)
        if func:
            try:
                func(evt)
                evt.show()
            except Exception as ex:
                Errors.handle(ex)
        evt.ready()
        return evt


def command(cli, txt):
    evt = cli.event(txt)
    Command.handle(evt)
    evt.ready()
    return evt


def scan(mod):
    for _key, cmd in inspect.getmembers(mod, inspect.isfunction):
        if 'event' in cmd.__code__.co_varnames:
            Command.add(cmd.__name__, cmd)
