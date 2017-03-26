import re


def fold_right(op, seq, acc):
    return acc if len(seq)==0 else fold_right(op, seq[1:], op(acc, seq[0]))

def find_filenames(re_pattern, fnames):
    def is_match_in_file(fname):
        with open(fname, 'r') as fobj:
            return re.search(re_pattern, fobj.read()) is not None
    fnames = filter(is_match_in_file, fnames)
    return '\n'.join(fnames) + '\n' if len(fnames) > 0 else ''

def find_lines(re_pattern, fnames, flags):
    def accum_matches(existing, fname):
        def match_lines(is_inverted):
            has_match = lambda (_, line): re.search(re_pattern, line) is not None
            match_pred = has_match if not is_inverted else (lambda line: not has_match(line))
            with open(fname, 'r') as fobj:
                return (fname, filter(match_pred, enumerate(fobj.readlines())))
        return existing + [match_lines('-v' in flags)]
    def accum_match_text(existing, fname_matches):
        def match_formatter(match):
            index, text = match
            text = ('{}:'.format(index+1) if '-n' in flags else '') + text
            text = ('{}:'.format(fname) if len(fnames_matches) > 1 else '') + text
            return (index+1, text)
        def concat_match_text(linenums_linetxts):
            return ''.join(txt for _, txt in linenums_linetxts)
        fname, matches = fname_matches
        return existing + concat_match_text(map(match_formatter, matches))
    fnames_matches = fold_right(accum_matches, fnames, [])
    return fold_right(accum_match_text, fnames_matches, '')

def gen_pattern(pat_str, is_case_insensitive, match_whole_line):
    if match_whole_line: pat_str = r'^' + pat_str + r'$'
    return re.compile(pat_str, re.IGNORECASE) if is_case_insensitive else re.compile(pat_str)

def grep(pat_str, fnames, flagstr=None):
    flags = [] if flagstr is None else flagstr.split()
    re_pattern = gen_pattern(pat_str, '-i' in flags, '-x' in flags)
    return find_filenames(re_pattern, fnames) if '-l' in flags else find_lines(re_pattern, fnames, flags)
