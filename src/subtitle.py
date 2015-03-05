class Subtitle(object):
    """
    This is the new subtitle that has to be saved.
    All the formatting and the inclusion of definitions in the final subtitle
    go here.
    """
    def __init__(self, times=[], text=[], lemmas=[], filename="sub.srt"):
        self.times = times
        self.text = text
        self.final_text = ""
        self.lemmas = lemmas
        self.filename = filename

    def create_subtitle(self):
        return

    def save(self):
        with open(self.filename, 'w') as f:
            f.write(self.final_text)

    def get_subtitle(self):
        return self.final_text
