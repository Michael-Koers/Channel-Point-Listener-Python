import requests
from models.Channel import Channel 
from models.Auth import Auth

class ChannelHandler:

    url : str = "https://api.twitch.tv/helix/search/channels"
    channel : str = "ancientd00m"
    userId: str = "54600501"

    def getChannel(self, auth : Auth) -> Channel:
        res = requests.get(self.url, headers={"client-id": auth.getId(), "Authorization": "Bearer {}".format(auth.getToken())}, params={"query": self.channel})
        res_json = res.json()["data"]
        
        # Extract channel from Channel array
        return Channel([idx for idx in res_json if idx['display_name'] == 'ancientd00m'][0])

        