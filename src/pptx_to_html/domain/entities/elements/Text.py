class Text():

    def __init__(self, size, text):
        self.text = text
        self.size = size
        self.tag = self.getTag(size)

    def get_size(self):
        return self.size

    def get_text(self):
        return self.text

    def getTag(self, size):
        tag = ""
        if size > 26:
            tag = "h1"
        elif 18 <= size <= 26:
            tag = "h2"
        elif 14 <= size <= 18:
            tag = "h3"
        elif 12 <= size <= 14:
            tag = "p"
        elif 10 <= size <= 12:
            tag = "p"
        elif 0 <= size <= 10:
            tag = "p"
        else:
            tag = "p"

        return tag



