# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0401,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1



from opr.listens import Listens
from opr.objects import kind


def __dir__():
    return (
            'flt',
           )


__all__ = __dir__()


def flt(event):
    try:
        index = int(event.args[0])
        event.reply(Listens.objs[index])
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(' | '.join([kind(obj) for obj in Listens.objs]))
