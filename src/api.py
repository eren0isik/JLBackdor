import socket
import requests


class api:
    def __init__(self, uri) -> None:
        self.uri = uri

    def get(self, endif):
        self.endif = endif
        resuri = self.uri + self.endif
        res = requests.get(resuri)
        res = res.text
        return res