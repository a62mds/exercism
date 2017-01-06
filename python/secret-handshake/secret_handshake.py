# List of allowed actions that may compose a hshk
_actions = ['wink', 'double blink', 'close your eyes', 'jump']
# Returned when an invalid input is provided
_invalid_code = '0'
_invalid_hshk = []
# Indicate order of handshake
_fwd_order = 'fwd'
_bwd_order = 'bwd'

def is_subseq(subseq, superseq):
    """Accepts as input two lists 'subseq' and 'superseq' and decides whether
    'subseq' is an ordered subsequence of 'superseq'. Obtained from
    http://stackoverflow.com/questions/8024052/comparing-element-order-in-python-lists
    """
    start = 0
    try:
        for ee in subseq:
            start = superseq.index(ee, start) + 1
    except ValueError:
        return False
    return True

def standardized_code(code):
    """Accepts input as either an integer or the binary representation of an
    integer in the form of a string of '1's and '0's.

    Ensures the input is valid and that the numeric value of the input lies
    within the range of allowed values.

    Returns either the char '0' indicating that the input was invalid, or a
    string of '1's and '0's of length len(_actions)+1, left-padded with zeros if
    necessary.
    """
    # Determine the range of allowed numeric values for the input
    max_int = sum(2**ii for ii in range(len(_actions) + 1))
    allowed_ints = range(1, max_int + 1)
    # Helper functions for verifying the validity of the input
    def is_valid_int(ntgr):
        return isinstance(ntgr, int) and ntgr in allowed_ints
    def is_valid_bstr(bstr):
        if not isinstance(bstr, str): return False
        in_range = len(bstr) <= len(_actions) + 1
        if not in_range: return False
        is_binary = all(dd in ['0', '1'] for dd in bstr)
        return is_binary
    # Test for type and validity of input and return appropriate binary string
    if is_valid_int(code):
        return '{:b}'.format(code).zfill(len(_actions) + 1)
    elif is_valid_bstr(code):
        return code.zfill(len(_actions) + 1)
    else: return _invalid_code

def handshake(code):
    """Accepts input as either an integer or the binary representation of an
    integer in the form of a string of '1's and '0's.

    Ensures input is valid using the function 'standardized_code', which
    returns a string 'scode' of '1's and '0's with a standard length, dependent
    on the length of the list '_actions' of allowed hshk actions. This
    result, i.e. binary number, is reversed so that it may be read from left to
    right in the same way the list '_actions' is read. Each bit, say the i^th
    bit from the left, in 'scode' corresponds to the action in '_actions' with
    index i.

    If 'scode' indicates that the input was invalid, an empty list is returned.
    Otherwise, the reversed, standardized biinary string is read one bit at a
    time, and the hshk sequence is generated step-by-step.

    The length of 'scode' is always one greater than the length of the list
    '_actions'. (This is guaranteed by the function 'standardized_code'.) The
    right-most bit of 'scode' indicates whether the sequence generated should be
    reversed: if it is '1', the sequence should be reversed; if it is '0', the
    sequence should be returned as-is.
    """
    # Get standardized binary string and reverse it to easily read left-ro-right
    scode = standardized_code(code)[::-1]
    if scode == _invalid_code: return _invalid_hshk
    # If input was valid, generate the list of actions that correspond to the
    # input 'code' by reading through the list '_actions' of allowed actions and
    # appending each action whose corresponding bit in 'scode' is '1'
    _hshk = [_actions[ii] for ii in range(len(_actions)) if scode[ii]=='1']
    # If the right-most bit in 'scode' is '0', return 'hshk' as-is; else, reverse
    # it and return that
    return _hshk if scode[-1]=='0' else _hshk[::-1]

def standardized_hshk(hshk):
    """Accepts as input a sequence of actions.

    Ensures the sequence of actions forms a valid handshake by first ensuring
    each action is in the list '_actions' and then ensuring that the actions
    occur in an allowed order: either 1) in the same order they occur in the
    list '_actions'; or 2) in the reverse order to that in which they occur in
    '_actions'.

    Generates a standardized handshake 'shshk' by reading through '_actions' and
    adding each action also in 'hshk' to the 'shshk'. When an action in
    '_action' is not also in 'hshk', the empty string '' is added to 'shshk' as
    a placeholder, ensuring that 'shshk' and '_actions' have the same length.

    Determines whether the actions in 'hshk' occur in the same order as they do
    in '_actions', or in the reverse order. In case they have the same order,
    the value '_fwd_order' is added to 'shshk'; in case their orders are
    reversed, the value '_bwd_order' is added to 'shshk'. In either case, the
    returned list has length one greater than the length of '_actions'. In case
    the order of actions in 'hshk' matches either of these two cases, the
    sequence is invalid, and a value of '_invalid_hshk' is returned.
    """
    # Helper functions for ensuring the order of the actions in 'hshk' is valid
    def in_fwd_order(acts): return is_subseq(acts, _actions)
    def in_bwd_order(acts): return is_subseq(acts[::-1], _actions)
    # Generate standardized handshake sequence
    shshk = [a if a in hshk else '' for a in _actions]
    # Ensure each action in the input is in '_actions'
    if not all(a in _actions for a in hshk): return _invalid_hshk
    # Ensure the order of the actions is valid
    if in_fwd_order(hshk):
        return shshk + [_fwd_order]
    elif in_bwd_order(hshk):
        return shshk + [_bwd_order]
    else:
        return _invalid_hshk

def code(hshk):
    """Accepts as input a sequence of actions.

    Standardizes the input and stores the result in 'shshk'. If the input was
    invalid, returns the value '_invalid_code'. If the code was valid, generates
    a string '_code' consisting of '1's and '0's representing the binary
    representation of the handshake, with each bit indicating whether a
    particular action is involved in the handshake.

    The right-most element of 'shshk' contains a value of either '_fwd_order' or
    '_bwd_order', indicating whether the handshake sequence occurs in the same
    order as in the sequence '_actions', or in the reverse order. In the first
    case, any extraneous zeros are removed from the left of '_code' before it is
    returned. In the second (reverse order) case, the length of '_code' is
    increased by one by adding a '1' onto the left of '_code', indicating the
    reversal of order.
    """
    shshk = standardized_hshk(hshk)
    if shshk == _invalid_hshk: return _invalid_code
    # If handshake was valid, translate the sequence into its binary
    # representation
    _code = ''.join(['0' if a == '' else '1' for a in shshk[:-1]][::-1])
    # Indicate order of sequence by setting the "order bit" appropriately
    return _code.lstrip('0') if shshk[-1] == _fwd_order else '1'+_code
