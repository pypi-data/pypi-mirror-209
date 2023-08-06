# This file is placed in the Public Domain.
# pylint: disable=C,I,R,E0401,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import time


from opr.classes import Classes
from opr.objects import Object
from opr.persist import find, fntime, write
from opr.utility import elapsed


class Todo(Object):

    def __init__(self):
        super().__init__()
        self.txt = ''


Classes.add(Todo)


def dne(event):
    if not event.args:
        return
    selector = {'txt': event.args[0]}
    for obj in find('todo', selector):
        obj.__deleted__ = True
        write(obj)
        event.reply('ok')
        break


def tdo(event):
    if not event.rest:
        nr = 0
        for obj in find('todo'):
            lap = elapsed(time.time()-fntime(obj.__oid__))
            event.reply(f'{nr} {obj.txt} {lap}')
            nr += 1
        if not nr:
            event.reply("no todo")
        return
    o = Todo()
    o.txt = event.rest
    write(o)
    event.reply('ok')
