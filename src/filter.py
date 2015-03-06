DICT_FILENAME = "../dict/english.dict"


class Filter(object):
    """
    Filter those lemmas whose meanings are already known
    (according to the dictionary).
    The dictionary must have every definition in his own separate line.
    Also, each definition has to be like:
        word:meaning
    """
    def __init__(self):
        self.dict = {}
        self.lemmas = []

    def load_dict(self):
        f = open(DICT_FILENAME, 'r')
        words = f.read().splitlines()
        for elem in words:
            k, v = elem.split(':', 1)
            self.dict[k.strip()] = v.strip()

    def clean_lemmas(self, lemmas):
        self.lemmas = self.lemmas[:]
        keys = self.dict.keys()
        for elem in lemmas:
            final_lemmas = []
            for w in elem:
                if w not in keys:
                    final_lemmas.append(w)
            self.lemmas.append(final_lemmas)

    def get_final_lemmas(self):
        return self.lemmas
