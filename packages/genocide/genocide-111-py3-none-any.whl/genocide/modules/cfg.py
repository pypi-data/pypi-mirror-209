# This file is placed in the Public Domain.
# pylint: disable=C,I,R


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from genocide.objects import edit, keys, prt
from genocide.persist import last, write
from genocide.runtime import Cfg


def __dir__():
    return (
            "kcfg",
           )


__all__ = __dir__()


def kcfg(event):
    config = Cfg
    last(config)
    if not event.sets:
        event.reply(prt(
                        config,
                        keys(config)
                       )
                   )
    else: 
        edit(config, event.sets)
        write(config)
        event.reply('ok')
