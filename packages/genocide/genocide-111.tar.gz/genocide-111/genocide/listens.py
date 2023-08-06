# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from .objects import Object


def __dir__():
    return (
            'Listens',
           )


__all__ = __dir__()



class Listens(Object):

    objs = []

    @staticmethod
    def add(obj):
        Listens.objs.append(obj)

    @staticmethod
    def announce(txt):
        for obj in Listens.objs:
            obj.announce(txt)

    @staticmethod
    def byorig(orig):
        for obj in Listens.objs:
            if repr(obj) == orig:
                return obj
        return None

    @staticmethod
    def remove(bot):
        try:
            Listens.objs.remove(bot)
        except ValueError:
            pass

    @staticmethod
    def say(orig, txt, channel=None):
        bot = Listens.byorig(orig)
        if bot:
            if channel:
                bot.say(channel, txt)
            else:
                bot.raw(txt)
