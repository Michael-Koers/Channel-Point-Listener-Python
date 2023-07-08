from datetime import datetime
import threading
import time

class KeepAliveThread(threading.Thread):

    def __init__(self, ws, interval = 300):
        threading.Thread.__init__(self)
        self.ws = ws
        self.runKeepAlive = threading.Event()
        self.timeout = interval

    def run(self):
        print("Starting KeepAlive")
        self.ping()
        print("Exiting KeepAlive")

    def ping(self):
        while not self.runKeepAlive.is_set():
            print("Sending PING at {}".format(datetime.now().strftime("%H:%M:%S")))
            self.ws.send(' { "type": "PING" } ')
            self.runKeepAlive.wait(timeout=self.timeout)

    def stop(self):
        self.runKeepAlive.set()