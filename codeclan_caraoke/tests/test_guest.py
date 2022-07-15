import unittest

from classes.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest('Daniel')

    def test_guest_name(self):
        actual = self.guest.name 
        self.assertEqual('Daniel', actual)
        
