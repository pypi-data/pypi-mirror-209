# This file is placed in the Public Domain.
# pylint: disable=C,I,R,W,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import unittest


from genocide.objects import Object
from genocide.decoder import loads
from genocide.encoder import dumps


class TestDecoder(unittest.TestCase):

    def test_loads(self):
        obj = Object()
        obj.test = "bla"
        oobj = loads(dumps(obj))
        self.assertEqual(oobj.test, "bla")

    def test_doctest(self):
        """
            >>> from bsd.objects import Object, dumps, loads
            >>> obj = Object()
            >>> obj.test = "bla"
            >>> oobj = loads(dumps(obj))
            >>> oobj.test
            'bla'
        """
        self.assertTrue(True)
