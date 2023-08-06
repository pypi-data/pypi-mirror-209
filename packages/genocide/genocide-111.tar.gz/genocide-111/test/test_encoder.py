# This file is placed in the Public Domain.
# pylint: disable=C0114,C0115,C0116


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1



import unittest


from genocide.objects import Object
from genocide.encoder import dumps


VALIDJSON = '{"test": "bla"}'


class TestEncoder(unittest.TestCase):


    def test_dumps(self):
        obj = Object()
        obj.test = "bla"
        self.assertEqual(dumps(obj), VALIDJSON)
