from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer


class Normalizer(object):
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.tokens = []
        self.pos_tags = []
        self.words = []
        self.lemmas = []
        # this is useful to use wordnet later on
        # J-> adjective, R-> adverb, N-> noun, V-> verb
        self.tags = {'J': 'a', 'R': 'r', 'N': 'n', 'V': 'v'}

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
                # we only check the first letter of the tag
                # the remaining letters are meaningless
                # for our purposes
                if tag[0] not in "%&'[]()!#$:;~{}|?-\/`.*+,.<=>@":
                    if tag[1] not in ['NNP', 'NNPS']:
                        if tag[1][0] in self.tags.keys():
                            w.append(tag)
            self.words.append(w)

    def lemmatize(self):
        for elem in self.words:
            lem = []
            for word in elem:
                if word:
                    lem.append((self.lemmatizer.lemmatize(word[0]),
                                self.tags[word[1][0]]))
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
