# This file is placed in the Public Domain.
# pylint: disable=C,I,R


"""operator bot

OPERBOT is a bot, intended to be programmable, with a client program to
develop modules on and a systemd version with code included to run a 24/7
presence in a channel.

OPERBOT uses object programming, where the methods are seperated
out into functions that use the object as the first argument of that funcion.
This gives base class definitions a clean namespace to inherit from and to load
json data into the object's __dict__. A clean namespace prevents a json loaded
attribute to overwrite any methods.

OPERBOT provides object persistence, an event handler and some basic code to
load modules that can provide additional commands.

OPERBOT has some functionality, mostly feeding RSS feeds into a irc
channel. It can do some logging of txt and take note of things todo.

"""


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from operbot.modules import *
