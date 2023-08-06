# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import io
import traceback


from ..errored import Errors


def err(event):
    for ex in Errors.errors:
        stream = io.StringIO(traceback.print_exception(type(ex), ex, ex.__traceback__))
        for line in stream.readlines():
            event.reply(line)
    else:
        event.reply("no error")
