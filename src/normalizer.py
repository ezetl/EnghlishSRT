import nltk


class Normalizer(object):
    def __init__(self):
        self.tokens = []
        self.pos_tags = []
        self.lemmas = []

    def tokenize(self, text):
        return

    def do_pos_tag(self):
        return

    def filter_tags(self):
        return

    def lemmatize(self):
        return

    def normalize(self, text):
        self.tokens = self.tokenize(text)
        self.pos_tags = self.do_pos_tag()
        self.filter_tags()
        self.lemmatize()

    def get_lemmas(self):
        return self.lemmas
