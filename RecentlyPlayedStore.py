class RecentlyPlayedStore:
    def __init__(self, num_songs_per_user=None, initial_capacity=3) -> None:
        if num_songs_per_user == None:
            self.num_songs_per_user = initial_capacity
        else:
            self.num_songs_per_user = num_songs_per_user
        self.store = {}

    def add_song(self, song_id, user_id):
        if self.store.get(user_id) == None:
            self.store[user_id] = []
        self.store[user_id].append(song_id)
        self.store[user_id] = self.store[user_id][-self.num_songs_per_user:]

    def get_recent_played_songs(self, user_id):
        try:
            user_songs = self.store[user_id]
        except KeyError:
            return ("No such user found")

        return user_songs

    def get_num_users(self):
        return len(self.store)

    def increase_capacity(self, capacity):
        self.num_songs_per_user = capacity


if __name__ == '__main__':
    recent_play_store = RecentlyPlayedStore()
