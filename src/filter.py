class Filter(object):
    """
    Filter those lemmas whose meanings are already known
    (according to the dictionary).
    """
    def __init__(self):
        self.dict = {}
        self.lemmas = []

    def load_dict(self):
        return

    def clean_lemmas(self, lemmas):
        return

    def get_final_lemmas(self):
        return self.lemmas
