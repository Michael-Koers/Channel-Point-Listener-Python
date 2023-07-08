from models.HueConfig import HueConfig
from events.BaseEvent import BaseEvent
from events.sounds.BaseSoundEvent import BaseSoundEvent
from events.tts.TtsEvent import TtsEvent
from events.lights.Blackout import Blackout
from events.lights.GreenScreen import GreenScreen
# from events.lights.ColorEvent import ColorEvent

class EventFactory:

    def __init__(self, hue_config : HueConfig):
        self.hue_config = hue_config

    def getEvent(self, data) -> BaseEvent:

        reward_title: str = data['reward']['title']
        reward_title_filename = reward_title.lower().replace(" ", "")
        redeemed_by: str = data['user']['display_name']

        print('{} redeemed {}({})'.format(
            redeemed_by, reward_title, reward_title_filename))

        # Get the correct event by redemption title.
        if("TTS" in reward_title):
            print("redeemed tts")
            # We only grab the user input here because for rewards with no user input, this key doesn't exist, and thus the method doesn't continue

            user_input: str = data['user_input']

            print("TTS event! User input: {}".format(user_input))
            return TtsEvent(redeemed_by, user_input)

        elif('Lights - ' in reward_title):

            title = reward_title.replace('Lights - ', '').lower().strip()
            print('Lights redeemed: {}'.format(title))

            if('blackout' in title):
                return Blackout(self.hue_config)
            
            # elif('color picker' in title):
            #     color: str = data['user_input']
            #     return ColorEvent(self.hue_config, color)
            
            elif('green screen stream' in title):
                return GreenScreen(self.hue_config)

            else:
                print('Unknown lights event...')

        else:
            print("redeemed sound")
            return BaseSoundEvent(data, reward_title_filename)
