"""Count words in text using toolz. Taken directly from toolz documentation."""

from toolz import compose, frequencies
from toolz.curried import map


def stem(word):
    """Stem word to primitive form"""
    return word.lower().rstrip(",.!:;'-\"").lstrip("'\"")


wordcount = compose(frequencies, map(stem), str.split)


def get_word_count(text: str) -> dict:
    """Count words in text and return a dictionary with word counts"""
    return wordcount(text)
