# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = "1"


def doskip(txt, skip=[]):
    if not txt.strip():
        return True
    for skp in skip:
        if skp in txt:
            return True
    return False
