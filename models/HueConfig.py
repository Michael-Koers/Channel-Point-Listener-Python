# This class cannot have any methods as it acts as a container config (due to JSON serialization/deserialization)
# oude scene : UTS2O7dR35STKMM
class HueConfig:

    def __init__(self):
        self.scene_stream: str = ''
        self.default_brightness: int = 0
        self.hue_left: str = ''
        self.hue_right: str = ''
        self.hue_strip: str = ''
        self.hue_ip: str = ''
        self.hue_user : str = ''
        self.event_duration : int = 0
