import os
import sys


def main(in_subt, out_subt):
    assert in_subt != ""
    assert out_subt != ""

    parser = Parser()
    normalizer = Normalizer()
    lemma_filter = Filter()
    new_sub = Subtitle()

    with open(in_subt, 'r') as f:
        text = f.read()
        parser.parse(text)
        normalizer.normalize(parser.get_text())
        lemma_filter.clean_lemmas(normalizer.get_lemmas())
        new_sub.create_subtitle(parser.get_times(), parser.get_text(),
                                lemma_filter.get_final_lemmas())
        new_sub.save_subtitle()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("You are missing the subtitle name.")
    in_subt = sys.argv[1]
    out_subt, extension = os.path.splitext(in_subt)
    print(out_subt, extension)
    out_subt += "_modified" + extension
    if len(sys.argv) == 3:
        out_subt = sys.argv[2]
    main(in_subt, out_subt)
    sys.exit()
