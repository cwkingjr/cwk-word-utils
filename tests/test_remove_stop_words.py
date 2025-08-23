
from cwk_word_utils.remove_stop_words import (
    remove_stopwords_nltk,
    remove_stopwords_spacy,
)


def test_remove_stopwords_nltk():
    text = "This is a sample sentence showing stopword removal."
    result = remove_stopwords_nltk(text)
    expected = ["sample", "sentence", "showing", "stopword", "removal", "."]
    assert result == expected


def test_remove_stopwords_spacy():
    text = "This is a sample sentence showing stopword removal."
    result = remove_stopwords_spacy(text)
    expected = ["sample", "sentence", "showing", "stopword", "removal", "."]
    assert result == expected
