import re


def rem_intro(word_prob):
    intro_pattern = re.compile(r'^What is ')
    if re.match(intro_pattern, word_prob):
        return re.sub(intro_pattern, '', word_prob)
    else:
        raise ValueError('Word problem does not start with "What is "')

def rem_qmark(word_prob):
    qmark_pattern = re.compile(r'\?$')
    if qmark_pattern.search(word_prob) is not None:
        return qmark_pattern.sub(lambda m: '', word_prob)
    else:
        raise ValueError('Word problem does not end with "?"')

def trans_ops(word_prob):
    op_dict = {'plus' : '+', 'minus' : '-', 'multiplied by' : '*','divided by' : '/'}
    rep = dict((re.escape(k), v) for k, v in op_dict.iteritems())
    op_pattern = re.compile("|".join(rep.keys()))
    return op_pattern.sub(lambda m: rep[re.escape(m.group(0))], word_prob)

def verify_validity(word_prob):
    word_prob_pattern = re.compile(r'^-?\d+(\s(\+|-|\*|/)\s-?\d+)+$')
    if word_prob_pattern.match(word_prob):
        return word_prob
    else:
        raise ValueError('Invalid word problem')

def recursive_eval(num_prob):
    binary_op_pattern = re.compile(r'^-*\d+\s(\+|-|\*|/)\s-*\d+$')
    if binary_op_pattern.match(num_prob):
        return eval(num_prob)
    else:
        first_expr_pattern = re.compile(r'^-*\d+\s(\+|-|\*|/)\s-*\d+')
        return recursive_eval(first_expr_pattern.sub(lambda m: str(eval(m.group())), num_prob))

def calculate(word_prob):
    print(word_prob)
    num_prob = verify_validity(trans_ops(rem_qmark(rem_intro(word_prob))))
    ans = recursive_eval(num_prob)
    print('{0} = {1}'.format(num_prob, ans))
    return ans


word_prob = "What is -3 plus 7 multiplied by -2?"
calculate(word_prob)
