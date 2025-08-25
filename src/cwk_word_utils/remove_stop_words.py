from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import spacy
from toolz import curry

# https://www.nltk.org/data.html


@curry
def remove_stopwords_nltk(string_of_words, nltk_corpus_language="english") -> list:
    """Removes stopwords using nltk stopwords and word_tokenize.

    Requires that `nltk` corpus `stopwords` and `punkt` have been previously
    downloaded and installed on your system in the location identified by
    the nltk data link below. Or, you can put the data somewhere else and
    inform nltk via enviroment variables. See how to set those up in the
    data link: https://www.nltk.org/data.html.

    You can download the files manually with python via:
    import nltk
    nltk.download("stopwords")
    nltk.download("punkt")

    A quick way to do this, if you have uv installed, is to put that info above,
    into a get_nltk_data.py file, then run this command:
    `uv run --isolated --with nltk python3 ./get_nltk_data.py`.
    """

    # Get English stopwords and tokenize
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(string_of_words.lower())

    # Remove stopwords
    filtered_tokens = [word for word in tokens if word not in stop_words]

    return filtered_tokens


@curry
def remove_stopwords_spacy(string_of_words) -> list:
    """Removed stop words using spacy nlp.

    Loads spacy en_core_web_sm, gets tokens from text via spacy nlp, and filters
    out stop words.
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(string_of_words)

    filtered_words = [token.text for token in doc if not token.is_stop]
    return filtered_words
