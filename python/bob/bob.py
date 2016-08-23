# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re


def is_yelled(greeting):
    has_alpha_char = bool(re.search(ur'[A-Z]', greeting))
    is_all_caps = greeting.isupper()
    return has_alpha_char and is_all_caps

def is_asked(greeting):
    # Ensure greeting is not empty and check last char for question mark
    return False if not greeting else greeting[-1] == '?'

def is_whitespace(greeting):
    # local greeting is just hey's greeting with leading and trailing whitespace
    # removed --> will be empty string if hey's greeting was all whitespace
    return True if not greeting else False

def hey(greeting):
    ugreeting = greeting.strip()
    if is_yelled(ugreeting):
        return u"Whoa, chill out!"
    elif is_asked(ugreeting):
        return u"Sure."
    elif is_whitespace(ugreeting):
        return u"Fine. Be that way!"
    else:
        return u"Whatever."
