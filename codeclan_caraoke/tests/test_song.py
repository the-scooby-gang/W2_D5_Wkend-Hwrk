import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song('shocker', 'steel panther')

    def test_song_title(self):
        actual = self.song.title 
        self.assertEqual('shocker', actual)

    def test_song_artist(self):
        actual = self.song.artist
        self.assertEqual('steel panther', actual)

