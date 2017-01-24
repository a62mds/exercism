# Solution based on regex
import re


def rem_intro(word_prob):
    """
    Checks whether or not word_prob starts with 'What is '. If it does,
    word_prob is stripped of this introduction. If it doesn't, raises a
    ValueError indicating an invalid word problem.
    """
    intro_pattern = re.compile(r'^What is ')
    if re.match(intro_pattern, word_prob):
        return re.sub(intro_pattern, '', word_prob)
    else:
        raise ValueError('Word problem does not start with "What is "')

def rem_qmark(word_prob):
    """
    Checks whether or not word_prob ends with a question mark. if it does,
    word_prob is stripped of '?'. If it doesn't, raises a ValueError indicating
    an invalid word problem.
    """
    qmark_pattern = re.compile(r'\?$')
    if qmark_pattern.search(word_prob) is not None:
        return qmark_pattern.sub(lambda m: '', word_prob)
    else:
        raise ValueError('Word problem does not end with "?"')

def trans_ops(word_prob):
    """
    Translates english phrases 'plus', 'minus', 'multiplied by', and 'divided by'
    to their associated mathematical symbols '+', '-', '*', and '/', resp.
    """
    op_dict = {'plus' : '+', 'minus' : '-', 'multiplied by' : '*','divided by' : '/'}
    rep = dict((re.escape(k), v) for k, v in op_dict.iteritems())
    op_pattern = re.compile("|".join(rep.keys()))
    return op_pattern.sub(lambda m: rep[re.escape(m.group(0))], word_prob)

def verify_validity(word_prob):
    """
    Verifies that word_prob (assumed to have been stripped of the intro 'What is '
    and the ending '?', and to have had the english operation key phrases
    replaced by their mathematical symbols) has a valid syntax.
    """
    word_prob_pattern = re.compile(r'^-?\d+(\s(\+|-|\*|/)\s-?\d+)+$')
    if word_prob_pattern.match(word_prob):
        return word_prob
    else:
        raise ValueError('Invalid word problem')

def recursive_eval(num_prob):
    """
    Recursively evaluates numerical problem, calculating multiple operations in
    order they are encountered from left-to-right.
    """
    binary_op_pattern = re.compile(r'^-*\d+\s(\+|-|\*|/)\s-*\d+$')
    if binary_op_pattern.match(num_prob):
        return eval(num_prob)
    else:
        first_expr_pattern = re.compile(r'^-*\d+\s(\+|-|\*|/)\s-*\d+')
        return recursive_eval(first_expr_pattern.sub(lambda m: str(eval(m.group())), num_prob))

def calculate(word_prob):
    """
    Parses a mathematical word problem and returns the answer.
    """
    return recursive_eval(verify_validity(trans_ops(rem_qmark(rem_intro(word_prob)))))
