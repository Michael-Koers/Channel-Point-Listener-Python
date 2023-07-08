from models.HueConfig import HueConfig
from events.lights.BaseLightEvent import BaseLightEvent
import time

class GreenScreen(BaseLightEvent):

    def __init__(self, hue_config : HueConfig):
        super().__init__(hue_config)

    def fireEvent(self):
        
        green : str = self.converter.hex_to_xy('00FF00')

        self.bridge.set_light(self.hue_config.hue_left, 'xy', green, transitiontime=10)
        self.bridge.set_light(self.hue_config.hue_right, 'xy', green, transitiontime=10)

        time.sleep(self.hue_config.event_duration)

        self.bridge.activate_scene(scene_id=self.hue_config.scene_stream,group_id=2)