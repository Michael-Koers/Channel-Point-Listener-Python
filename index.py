from handlers.TokenHandler import TokenHandler
from models.Auth import Auth
from ws.WebSocketClient import WebSocketClient

def main():

    print("Channel Redemption Listener v0.2.0")
    # If Token no longer accepted:
    # 1. Grab client id (second entry below)
    # 2. Go to https://twitchapps.com/tokengen/
    # 3. Fill in client id and for scope "channel:read:redemptions"
    # 4. Paste token in last entry below
    auth : Auth = Auth(config_location=r'C:\Users\Michael\Documents\Github\Channel-Point-Listener-Python\config')
    auth.load()

    # Validate token
    tokenHandler : TokenHandler = TokenHandler(auth)
    if not tokenHandler.validate():
        print("Token validation failed, exiting program")
        quit()

    # Persist in case new valid token was supplied
    auth.persist()

    wsClient = WebSocketClient("wss://pubsub-edge.twitch.tv", auth.getUser(), auth.getToken())
    wsClient.connect()

if __name__ == "__main__":
    main()
