import vlc
import time
import glob
from os import path
from events.BaseEvent import BaseEvent

class BaseSoundEvent(BaseEvent):

    def __init__(self, data, songname):
        super().__init__()
        
        self.data = data
        self.dir = r"C:\Users\Michael\Documents\Github\Channel-Point-Listener-Python\events\sounds\sfx"
        self.songname = songname

    def fireEvent(self):

        song_path = "{}\\{}.*".format(self.dir, self.songname)
        song_file = glob.glob(song_path)[0]

        if((song_file is not None) and (path.exists(song_file))):
            print(song_file)
            player = vlc.MediaPlayer(song_file)
            player.play()

            while player.is_playing:
                time.sleep(10)
