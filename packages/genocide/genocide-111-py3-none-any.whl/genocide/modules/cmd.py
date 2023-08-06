# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from ..command import Command


def __dir__():
    return (
            'cmd',
           )


def cmd(event):
    event.reply(','.join(sorted(Command.cmds)))
