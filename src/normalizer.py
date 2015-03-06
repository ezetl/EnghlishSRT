from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer


class Normalizer(object):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.tokens = []
        self.pos_tags = []
        self.words = []
        self.lemmas = []

    def tokenize(self, list_subs):
        for elem in list_subs:
            self.tokens.append(word_tokenize(elem))

    def do_pos_tag(self):
        self.pos_tags = self.pos_tags[:]
        for elem in self.tokens:
            self.pos_tags.append(pos_tag(elem))

    def filter_tags(self):
        self.words = self.words[:]
        for elem in self.pos_tags:
            w = []
            for tag in elem:
                if tag[1] in ['ADJ', 'ADV', 'NOUN', 'VERB']:
                    w.append(tag[0])
            self.words.append(w)

    def lemmatize(self):
        for elem in self.words:
            lem = []
            for word in elem:
                lem.append(self.lemmatizer.lemmatize(word))
            self.lemmas.append(lem)

    def normalize(self, list_subs):
        self.tokenize(list_subs)
        self.do_pos_tag()
        self.filter_tags()
        self.lemmatize()

    def get_lemmas(self):
        return self.lemmas

    def get_pos_tags(self):
        return self.pos_tags
