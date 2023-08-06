# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from .clocked import Timer
from .threads import launch


def __dir__():
    return (
            "Repeater",
           )


class Repeater(Timer):

    def run(self):
        thr = launch(self.start)
        super().run()
        return thr
