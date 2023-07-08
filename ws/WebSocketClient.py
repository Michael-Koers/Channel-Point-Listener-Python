from models import HueConfig
from events.lights.HueConfigService import HueConfigService
from ws.KeepAliveThread import KeepAliveThread
from events.EventFactory import EventFactory
from events.BaseEvent import BaseEvent
import websocket
import json

class WebSocketClient:

    def __init__(self, uri: str, channel_id: str, token: str):
        self.uri = uri
        self.channel_id = channel_id
        self.token = token
        self.hue_config: HueConfig = HueConfigService(r'C:\Users\Michael\Documents\Github\Channel-Point-Listener-Python\config').load()
        self.event_factory = EventFactory(self.hue_config)

    def on_message(self, message):
        print("### MESSAGE ###")

        msg = json.loads(message)
        msg_type = msg['type']

        if msg_type == 'RESPONSE':
            print("Received RESPONSE")
            self.keepAlive = KeepAliveThread(self.ws, 10)
            self.keepAlive.start()

        elif msg_type == 'RECONNECT':
            print("Received RECONNECT")
            self.reconnect()

        elif msg_type == 'PONG':
            print("Received PONG")

        elif msg_type == "MESSAGE":
            print("Received Redemption")
            msg_data = json.loads(msg['data']['message'])['data']['redemption']
            event: BaseEvent = self.event_factory.getEvent(msg_data)
            event.start()

        else:
            print("Unexpected message: {}".format(message))


    def on_error(self, error):
        print("### error ###")
        if(type(error) != KeyboardInterrupt):
            print("restarting...")
            # Stop previous keepAlive thread
            self.reconnect()
        else:
            print("User interrupted, exiting...")
            self.on_close()
            self.disconnect()
            raise error

    def on_close(self):
        # Interrupt the KeepAlive thread
        self.keepAlive.runKeepAlive.set()
        print("### closed ###")

    def on_open(self):
        print("### open ###")
        print("Sending listening event")

        # Create Websocket Message to start listening to Channel point redemptions
        ws_message = """
        {{
            "type": "LISTEN",
            "nonce": "abc123",
            "data": {{
                    "topics": ["channel-points-channel-v1.{0}"],
                    "auth_token": "{1}"
                }}
        }}
        """.format(self.channel_id, self.token)

        self.ws.send(ws_message)

    def connect(self):
        # websocket.enableTrace(True)

        self.ws = websocket.WebSocketApp(self.uri,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         on_open=self.on_open)

        self.ws.run_forever()

    def disconnect(self):
        self.ws.close()

    def reconnect(self):
        self.disconnect()
        self.keepAlive.runKeepAlive.set()
        self.connect()