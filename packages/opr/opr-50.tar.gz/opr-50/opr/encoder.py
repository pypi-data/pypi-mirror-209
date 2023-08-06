# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import json


from .objects import Object


def __dir__():
    return (
            'ObjectEncoder',
            'dumps'
           )


__all__ = __dir__()


class ObjectEncoder(json.JSONEncoder):


    def default(self, o) -> str:
        if isinstance(o, dict):
            return o.items()
        if isinstance(o, Object):
            return vars(o)
        if isinstance(o, list):
            return iter(o)
        if isinstance(o,
                      (type(str), type(True), type(False),
                       type(int), type(float))
                     ):
            return str(o)
        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return str(o)

    def encode(self, o) -> str:
        return json.JSONEncoder.encode(self, o)

    def iterencode(self, o, _one_shot=False) -> str:
        return json.JSONEncoder.iterencode(self, o, _one_shot)


def dumps(*args, **kw) -> str:
    kw["cls"] = ObjectEncoder
    return json.dumps(*args, **kw)
