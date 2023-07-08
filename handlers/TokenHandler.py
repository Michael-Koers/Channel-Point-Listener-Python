from models.Auth import Auth
import requests

class TokenHandler:

    url: str = "https://id.twitch.tv/oauth2/token"
    validate_url: str = "https://id.twitch.tv/oauth2/validate"
    revoke_url: str = "https://id.twitch.tv/oauth2/revoke"
    grant_type: str = "client_credentials"
    scope: str = "channel:read:redemptions"


    def __init__(self, auth: Auth):
        self.auth = auth


    def getToken(self):
        res = requests.post(self.url, params={
            "client_id": self.auth.getId(), 
            "client_secret": self.auth.getSecret(), 
            "grant_type": self.grant_type, 
            "scope": self.scope
            }, headers={'Content-type': 'application/json'})
        self.auth.setToken(res.json()["access_token"])

    def validate(self):
        if not self.auth.getToken():
            print("No token present, retrieving new token...")
            self.getToken()

        res = requests.get(self.validate_url, headers={
                           "Authorization": "Bearer {}".format(self.auth.getToken())})
        if res.status_code == 200:
            print("Successfully validated token")
            return True
        else:
            print("Token validation error {0}".format(res.json()))
            if 'Y' in input('Retry? [Y/N] : '):
                self.getToken()
                return self.validate()
            else:
                print("User choose not to re-attempt")
                return False

    def revoke(self):
        res = requests.post(self.revoke_url, params={
                            "client_id": self.auth.getId(), "token": self.auth.getToken()})
        if res.status_code == 200:
            print("Successfully revoked token")
            return True
        else:
            print("Failed to revoke token\n {1}".format(res.json()))
            return False
