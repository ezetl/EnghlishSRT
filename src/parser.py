import re


class Parser(object):
    """
    Simple parser for subtitles in .srt format.
    'times' and 'text' are arrays that contain the times
    of appearance of each text and the text itself, respectively.
    """
    def __init__(self, subtitle=""):
        self.subtitle = subtitle  # raw text containing all the subtitles
        self.times = []
        self.text = []
        self.index = []

    def parse(self, text):
        self.times = self.times[:]
        self.text = self.text[:]
        self.index = self.index[:]
        splits = [s.strip() for s in re.split(r'\n\s*\n', text) if s.strip()]
        regex = re.compile(r'''(?P<index>\d+).*?(?P<times>\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3})\s*.*?\s*(?P<text>.*)''', re.DOTALL)
        for s in splits:
            r = regex.search(s)
            if r:
                self.index.append(r.group('index'))
                self.times.append(r.group('times'))
                self.text.append(r.group('text'))

    def get_times(self):
        return self.times

    def get_text(self):
        return self.text

    def get_indexes(self):
        return self.index
