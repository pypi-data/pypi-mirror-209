# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import json


from .objects import Object, copy


def __dir__():
    return (
            'ObjectDecoder',
            'loads'
           )


__all__ = __dir__()


class ObjectDecoder(json.JSONDecoder):

    def decode(self, s, _w=None) -> Object:
        val = json.JSONDecoder.decode(self, s)
        if not val:
            val = {}
        obj = Object()
        copy(obj, val)
        return obj

    def raw_decode(self, s, idx=0) -> (int, Object):
        return json.JSONDecoder.raw_decode(self, s, idx)


def loads(string, *args, **kw) -> Object:
    return json.loads(string, *args, cls=ObjectDecoder, **kw)
