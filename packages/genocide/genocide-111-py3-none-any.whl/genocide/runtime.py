# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import os
import time


from .default import Default


Cfg = Default()
Cfg.debug = False
Cfg.mod = "cmd,irc,mdl,rss"
Cfg.name = "genocide"
Cfg.silent = False
Cfg.skip = "PING,PONG"
Cfg.verbose = False
Cfg.wd = os.path.expanduser(f"~/.{Cfg.name}")


date = time.ctime(time.time()).replace('  ', ' ')
