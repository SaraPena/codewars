"""
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""

import string

def is_pangram(s):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    t = []
    for l in s:
        if l in ".!,?1234567890":
            s.replace(l,"")
    for l in s:
        if t.count(l) == 0:
            t.append(l)
    if len(t) >= 26:
        return True
    else:
        return False
