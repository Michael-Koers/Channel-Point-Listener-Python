from api.FifteenAPI import FifteenAPI
from events.BaseEvent import BaseEvent
import vlc
import time
import os

class TtsEvent(BaseEvent):

    def __init__(self, user, user_input: str):
        super().__init__()
        
        self.max_text_len = 40

        self.user_input = user_input.split(':',1)[1]
        self.voice = user_input.split(':',1)[0]
        self.user = user
        self.tts_api = FifteenAPI(show_debug=True)
        self.dir = r"C:\Users\Michael\Documents\Github\Channel-Point-Listener-Python\events\tts\tmp"

    def fireEvent(self):

        file_path = "{}\\{}.wav".format(self.dir, self.user)
        self.tts_api.save_to_file(self.voice, "Contextual", self.user_input[:self.max_text_len - 1], "events\\tts\\tmp\\{}".format(self.user))

        player = vlc.MediaPlayer(file_path)
        player.play()

        while player.is_playing:
            time.sleep(10)
