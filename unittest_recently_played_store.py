import unittest
from RecentlyPlayedStore import RecentlyPlayedStore


class TestRecentlyPlayedStore(unittest.TestCase):
    recently_played_songs = RecentlyPlayedStore(3)
    ini_song_list = ['s1', 's2', 's3']
    ext_song_list = ['s4', 's5']

    def test_0_add_songs_user1(self):
        for song in self.ini_song_list:
            self.recently_played_songs.add_song(song, 'u1')
        self.assertEqual(self.recently_played_songs.store,
                         {'u1': ['s1', 's2', 's3']})

    def test_1_get_recently_played_songs_user1(self):
        self.assertEqual(self.recently_played_songs.get_recent_played_songs(
            'u1'), ['s1', 's2', 's3'])

    def test_2_add_new_songs_user1_store(self):
        self.recently_played_songs.add_song('s4', 'u1')
        print(self.recently_played_songs.store)
        self.assertEqual(self.recently_played_songs.store,
                         {'u1': ['s2', 's3', 's4']})

    def test_3_updated_recently_played_songs_user1(self):
        self.assertEqual(self.recently_played_songs.get_recent_played_songs(
            'u1'), ['s2', 's3', 's4'])

    def tearDown(self):
        self.recently_played_songs


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestRecentlyPlayedStore('test_0_add_songs_user1'))
    suite.addTest(TestRecentlyPlayedStore(
        'test_1_get_recently_played_songs_user1'))
    suite.addTest(TestRecentlyPlayedStore(
        'test_2_add_new_songs_user1_store'))
    suite.addTest(TestRecentlyPlayedStore(
        'test_3_updated_recently_played_songs_user1'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
