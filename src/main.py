import os
import sys
from parser import Parser
from normalizer import Normalizer
from filter import Filter
from subtitle import Subtitle


def main(in_subt, out_subt):
    assert in_subt != ""
    assert out_subt != ""

    parser = Parser()
    normalizer = Normalizer()
    lemma_filter = Filter()

    try:
        f = open(in_subt, 'r')
        text = f.read()
        f.close()
    except IOError:
        sys.exit("The subtitle could not be found in the path you provided.")

    parser.parse(text)
    normalizer.normalize(parser.get_text())
    lemma_filter.clean_lemmas(normalizer.get_lemmas())
    new_sub = Subtitle(parser.get_times(), parser.get_text(),
                       lemma_filter.get_final_lemmas(), out_subt)
    new_sub.create_subtitle()
    new_sub.save()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("You are missing the subtitle name.")
    in_subt = sys.argv[1]
    out_subt, extension = os.path.splitext(in_subt)
    out_subt += "_modified" + extension
    if len(sys.argv) == 3:
        out_subt = sys.argv[2]
    main(in_subt, out_subt)
    sys.exit()
