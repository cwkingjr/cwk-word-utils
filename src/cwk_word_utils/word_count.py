"""Count words in text using toolz. Taken directly from toolz documentation."""

from toolz import compose, frequencies, curry
from toolz.curried import map
from collections import Counter
from cwk_word_utils.remove_stop_words import (
    remove_stopwords_nltk,
    remove_stopwords_spacy,
)
from typing import Any


def stem(word):
    """Stem word to primitive form"""
    return word.lower().rstrip(",.!:;'-\"").lstrip("'\"")


@curry
def seq_of_str_to_str(seq: Any) -> str:
    """Included in function so function can be put into compose."""
    return " ".join(list(seq))


def get_word_count_toolz(text: str) -> dict:
    """Count words in text and return a dictionary with word counts.

    Uses composition of stem and toolz frequencies function.
    """
    wordcount = compose(frequencies, map(stem), str.split)
    return wordcount(text)


def get_word_count_counter(
    text: str, return_most_common: int = 50, stop_word_lib="spacy"
) -> list[tuple[str, int]]:
    """Counts words in text and returns a dictionary with words as the
    keys and the counts as the values.

    Uses composition of local `stem` function and the itertools Counter.

    Uses `nltk` or `spacy` to remove stop words, which you can choose via
    `stop_word_lib="nltk"` or `stop_word_lib="spacy"`. These require that
    you have downloaded the associated stop word files, which you can find
    out about in the remove_stop_words.py module.

    You can also select how many of the top values you want to return from
    the Counter by setting the return_most_common setting to an integer,
    as in `return_most_common=23`.
    """
    if isinstance(text, list):
        msg = f"Expected a str and you provided a list: {text}"
        raise ValueError(msg)

    if not isinstance(return_most_common, int):
        msg = (
            f"Expected an int return_most_common and you provided: {return_most_common}"
        )
        raise ValueError(msg)

    if stop_word_lib == "nltk":
        wordcount_no_stop = compose(
            remove_stopwords_nltk, seq_of_str_to_str, map(stem), str.split
        )
    elif stop_word_lib == "spacy":
        wordcount_no_stop = compose(
            remove_stopwords_spacy, seq_of_str_to_str, map(stem), str.split
        )

    else:
        msg = f"Expected stop_word_lib of nltk or spacy but got '{stop_word_lib}'"
        raise ValueError(msg)

    counter = Counter(wordcount_no_stop(text))

    return counter.most_common(return_most_common)
