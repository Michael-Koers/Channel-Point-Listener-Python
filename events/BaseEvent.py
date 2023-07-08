import threading

class BaseEvent(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        self.fireEvent()

    def fireEvent(self):
        print("You need to override this method")