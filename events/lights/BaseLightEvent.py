from models.HueConfig import HueConfig
from events.BaseEvent import BaseEvent
from phue import Bridge
from rgbxy import Converter

class BaseLightEvent(BaseEvent):

    def __init__(self, hue_config : HueConfig):
        super().__init__()

        self.hue_config = hue_config

        self.bridge = Bridge(self.hue_config.hue_ip ,username=self.hue_config.hue_user)
        self.converter = Converter()

    def fireEvent(self):
        print("LightsEvent - You need to override this method")
        
