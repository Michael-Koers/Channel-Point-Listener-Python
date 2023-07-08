import json
from types import SimpleNamespace

class Auth:

    def __init__(self, user: str = '', clientId: str = '', clientSecret: str = '', token: str = '', config_location: str = ''):
        self.__user = user
        self.__id = clientId
        self.__secret = clientSecret
        self.__token = token
        self.__config = "{}\\auth.json".format(config_location)

    def getId(self):
        return self.__id

    def getSecret(self):
        return self.__secret

    def getToken(self):
        return self.__token

    def getUser(self):
        return self.__user

    def setToken(self, token : str):
        self.__token = token

    def persist(self):
        jsonDump: str = json.dumps(self.__dict__, indent=4)

        with open(self.__config, 'w') as config_file:
            config_file.write(jsonDump)

    def load(self):
        with open(self.__config) as config_file:
            auth: Auth = json.loads(config_file.read(), object_hook=lambda d: SimpleNamespace(**d))
            self.__user = auth.__user
            self.__id = auth.__id
            self.__secret = auth.__secret
            self.__token = auth.__token
            print("Succesfully loaded Token from file")
