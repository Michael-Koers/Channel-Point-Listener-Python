import json
from models import HueConfig
from types import SimpleNamespace

class HueConfigService:

    def __init__(self, config_location: str):
        self.__config = "{}\\hue_conf.json".format(config_location)

    def persist(self, config: HueConfig):
        jsonDump: str = json.dumps(config.__dict__, indent=4)

        with open(self.__config, 'w') as config_file:
            config_file.write(jsonDump)

    def load(self) -> HueConfig:
        with open(self.__config) as config_file:
            config: HueConfig = json.loads(
                config_file.read(), object_hook=lambda d: SimpleNamespace(**d))
            print("Succesfully loaded Hue config from file")
            return config
