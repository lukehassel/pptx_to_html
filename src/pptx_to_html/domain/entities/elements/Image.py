import base64


class Image():
    def __init__(self, bytes):
        self.base = self.bytes_to_base64(bytes)

    def getBase(self):
        return self.base

    def bytes_to_base64(self, bytes):
        return base64.b64encode(bytes)
