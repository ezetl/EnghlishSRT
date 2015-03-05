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

    def parse(self, text):
        self.times = self.times[:]
        self.text = self.text[:]
        return

    def get_times(self):
        return self.times

    def get_text(self):
        return self.text
