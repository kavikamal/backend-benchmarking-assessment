""" anagrams
    Command line interface that accepts a word file and returns a dictionary of
    anagrams for that file.

    Module provides a function find_anagrams which can be used to do the same
    for an arbitrary list of strings.

"""
import sys


def alphabetize(string):
    """ alphabetize
        Given a string, return a string that includes the same letters in
        alphabetical order.

        Example:

        >>> print alphabetize('cab')
        abc

    """
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    """ find_anagrams

        Return a dictionary with keys that are alphabetized words and values
        that are all words that, when alphabetized, match the key.

        Example:

        >>> print find_anagrams(['cat', 'dog', 'act'])
        {'dgo': ['dog'], 'act': ['cat', 'act']}

    """
    # Works for short
    anagrams = {}
    for word in words:
        if alphabetize(word) in anagrams:
            anagrams[alphabetize(word)].append(word)
        else:
            anagrams[alphabetize(word)] = [word]
    # anagrams = dict((alphabetize(w), [].append(w)) for w in words)
    return anagrams


if __name__ == "__main__":
    # run find anagrams of first argument
    if len(sys.argv) < 2:
        print "Please specify a word file!"
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read().split()
            print find_anagrams(words)
