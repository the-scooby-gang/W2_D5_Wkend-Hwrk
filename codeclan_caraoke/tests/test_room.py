import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 2)
        self.guest1 = Guest('Daniel')
        self.guest2 = Guest('Aimee')
        self.guest3 = Guest('Olivia')
        self.song = Song('shocker', 'steel panther')


    def test_room_number(self):
        actual = self.room.room_number
        self.assertEqual(1, actual)

    #function to check how many guests are in the room
    #function to check people into the room
    #function to check guests out
    #function to add song to room

    def test_can_add_person_to_room(self):
        self.room.add_guest(self.guest1)
        self.assertEqual(1, self.room.check_guest_size())

    def test_can_remove_persom_from_room(self):
        self.room.add_guest(self.guest2)
        self.assertEqual(1, self.room.check_guest_size())
        self.room.remove_guest(self.guest2)
        self.assertEqual(0, self.room.check_guest_size())

    def test_can_add_song_to_room(self):
        self.room.add_song(self.song)
        self.assertEqual(True, self.room.check_list_for_song(self.song))







