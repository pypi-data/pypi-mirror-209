# This file is placed in the Public Domain.
# pylint: disable=C,I,R,E0401,E0402


import time


from opr.classes import Classes
from opr.persist import find, fntime, write
from opr.objects import Object
from opr.utility import elapsed


def __dir__():
    return (
            'Log',
            'log',
           )


class Log(Object):

    def __init__(self):
        super().__init__()
        self.txt = ''


Classes.add(Log)


def log(event):
    if not event.rest:
        nmr = 0
        for obj in find('log'):
            lap = elapsed(time.time() - fntime(obj.__oid__))
            event.reply(f'{nmr} {obj.txt} {lap}')
            nmr += 1
        if not nmr:
            event.reply('no log')
        return
    obj = Log()
    obj.txt = event.rest
    write(obj)
    event.reply('ok')
