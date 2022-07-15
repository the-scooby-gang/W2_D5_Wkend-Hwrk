class Room:
    def __init__ (self, room_number, limit):
        self.room_number = room_number
        self.room_limit = limit #How many people can fit in a room 
        self.guest_list = [] #How many people are in that room [list]
        self.song_list = [] #Is my song title and artist in this list
    
    #function to check how many guests are in the room#
    #function to check people into the room#
    #function to check guests out
    #function to add song to room

    #check guest size

    def check_guest_size(self):
        return len(self.guest_list)

    def add_guest(self, guest):
        self.guest_list.append(guest)

    def remove_guest(self, guest):
        self.guest_list.remove(guest)

    def check_list_for_song(self, song_to_find):
        for song in self.song_list:
            if song == song_to_find:
                return True

    def add_song(self, song):
        self.song_list.append(song)
        




    


    

    
        




