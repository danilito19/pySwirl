from unittest import TestCase

import pySwirl

class TestHello(TestCase):
    def test_is_string(self):
        s = pySwirl.hello()
        self.assertTrue(isinstance(s, basestring))