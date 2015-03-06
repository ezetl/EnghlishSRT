import codecs


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

    def look_definitions(self):
        return

    def create_subtitle(self):
        return

    def save(self):
        with codecs.open(self.filename, 'w', encoding='utf8') as f:
            f.write(self.final_text)

    def get_subtitle(self):
        return self.final_text
