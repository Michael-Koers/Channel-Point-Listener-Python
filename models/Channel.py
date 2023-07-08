class Channel:

    def __init__(self, channel):
        self.id = channel["id"]
        self.is_live = channel["is_live"]

        # Other fields are language, displayname, game id, thumbnail url, title, started at