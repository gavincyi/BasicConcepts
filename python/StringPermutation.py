#!/bin/python

def Permutation(prefix, s):
    """
    Print out all the character combination of a given string.
    For example, for the input aabcd, the result is
        
    """
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(0, len(s)):
            Permutation(prefix + s[i], s[0:i] + s[i+1:])

if __name__ == '__main__':
    s = "aabcd"
    Permutation("", s)
