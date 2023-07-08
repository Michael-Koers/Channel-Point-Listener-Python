from models.HueConfig import HueConfig
from events.lights.BaseLightEvent import BaseLightEvent
import time

class Blackout(BaseLightEvent):

    def __init__(self, hue_config : HueConfig):
        super().__init__(hue_config)

    def fireEvent(self):
        
        self.bridge.set_light(self.hue_config.hue_strip, 'bri', 0,transitiontime=10)

        time.sleep(self.hue_config.event_duration)

        self.bridge.activate_scene(scene_id=self.hue_config.scene_stream,group_id=7)