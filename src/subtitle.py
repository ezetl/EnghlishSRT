import codecs
from nltk.corpus import wordnet as wn
from filter import DICT_FILENAME


class Subtitle(object):
    """
    This is the new subtitle that has to be saved.
    All the formatting and the inclusion of definitions in the final subtitle
    go here.
    """
    def __init__(self, indexes=[], times=[], text=[],
                 lemmas=[], dic={}, filename="s.srt"):
        self.indexes = indexes
        self.times = times
        self.text = text
        self.lemmas = lemmas
        self.dic = dic
        self.filename = filename
        self.new_defs = []

    def search_definitions(self):
        # lemmas is a list of lists of (word, pos_tag) elements
        for l in self.lemmas:
            defs = []
            for lem in l:
                key = lem[0]+'.'+lem[1]
                value = wn.synset(lem[0]+'.'+lem[1]+'01').definition()
                defs.append((key, value))
            self.new_defs.append(defs)

    def create_subtitle(self):
        self.search_definitions()
        s = u''
        for i, elem in enumerate(self.indexes):
            s += elem + u'\r\n'
            s += self.times[i] + u'\r\n'
            if self.defs[i]:
                for d in self.defs[i]:
                    s += u'{\a10}' + d[0] + u' : ' + d[1] + u'\r\n'
            s += self.text[i] + u'\r\n\r\n'

        with codecs.open(self.filename, 'w', encoding='utf8') as f:
            f.write(s)

    def update_dict(self):
        for elem in self.new_defs:
            for k, v in elem:
                self.dic[k] = v

        with open(DICT_FILENAME, 'w') as f:
            for elem in self.dic.keys():
                f.write(elem + ': ' + self.dic[elem] + u'\r\n')
