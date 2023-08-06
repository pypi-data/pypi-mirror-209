# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0401,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from opr.listens import Listens
from opr.objects import prt


def sts(event):
    for bot in Listens.objs:
        if 'state' in dir(bot):
            event.reply(prt(bot.state, skip='lastline'))
    else:
        event.reply("no status")
