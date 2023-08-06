# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


from .default import Default


def __dir__():
    return (
            'Classes',
           )


__all__ = __dir__()



class Classes:

    cls = Default()

    @staticmethod
    def add(clz) -> str:
        setattr(Classes.cls, f"{clz.__module__}.{clz.__name__}", clz)

    @staticmethod
    def get(cmd) -> type:
        return getattr(Classes.cls, cmd, None)

    @staticmethod
    def match(mtc) -> type:
        mtc = mtc.lower()
        for clz in Classes.cls:
            if mtc == clz.split(".")[-1].lower():
                yield clz

    @staticmethod
    def remove(clz) -> None:
        delattr(Classes.cls, f"{clz.__module__}.{clz.__name__}")
