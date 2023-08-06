# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from .objects import  Object


def __dir__():
    return (
            'Error',
            'Errors',
            'NoClassError',
           )


__all__ = __dir__()


class Error(Exception):

    "opb errors"

class NoClassError(Error):

    "the class is not registered."

class Errors(Object):

    errors = []

    @staticmethod
    def handle(ex):
        exc = ex.with_traceback(ex.__traceback__)
        Errors.errors.append(exc)
