# from models.HueConfig import HueConfig
# from events.lights.BaseLightEvent import BaseLightEvent
# import time
# import re

# class ColorEvent(BaseLightEvent):

#     hex_regex: str = r'(?:[0-9a-fA-F]{3}){1,2}$'

#     def __init__(self, hue_config : HueConfig, color):
#         super().__init__(hue_config)

#         match = re.search(self.hex_regex, color)

#         if match:
#             self.color_xy = self.converter.hex_to_xy(color)
#         else:
#             self.color_xy = self.converter.get_random_xy_color()

#     def fireEvent(self):

#         self.bridge.set_light(self.hue_left, 'xy',
#                               self.color_xy, transitiontime=10)
#         self.bridge.set_light(self.hue_right, 'xy',
#                               self.color_xy, transitiontime=10)

#         time.sleep(20)

#         self.bridge.activate_scene(scene_id=self.scene_stream, group_id=2)
