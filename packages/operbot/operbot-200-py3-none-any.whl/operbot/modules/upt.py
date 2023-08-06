# This file is placed in the Public Domain.
# pylint: disable=C,I,R,E0401,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import time


from opr.utility import elapsed


def __dir__():
    return (
            'upt',
           )


__all__ = __dir__()


starttime = time.time()


def upt(event):
    event.reply(elapsed(time.time()-starttime))
