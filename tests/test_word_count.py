import pytest
from cwk_word_utils.word_count import (
    get_word_count_toolz,
    seq_of_str_to_str,
    get_word_count_counter,
)


@pytest.fixture
def sample_text():
    return "This cat jumped over this other cat!"


def test_get_word_count_counter_list_input_raises():
    with pytest.raises(ValueError):
        get_word_count_counter(["one", "two"])


def test_get_word_count_counter_unknown_lib_raises():
    with pytest.raises(ValueError):
        get_word_count_counter("chair chair", stop_word_lib="bogus")


def test_get_word_count_counter_non_int_raises():
    with pytest.raises(ValueError):
        get_word_count_counter("chair chair", return_most_common="ONE")


def test_get_word_count_counter_nltk():
    my_text = "chair chair chair table table"
    assert get_word_count_counter(my_text, stop_word_lib="nltk") == [
        ("chair", 3),
        ("table", 2),
    ]


def test_get_word_count_counter_spacy():
    my_text = "chair chair chair table table"
    assert get_word_count_counter(my_text, stop_word_lib="spacy") == [
        ("chair", 3),
        ("table", 2),
    ]


def test_get_word_count_toolz(sample_text):
    expected_result = {"this": 2, "cat": 2, "jumped": 1, "over": 1, "other": 1}
    assert get_word_count_toolz(sample_text) == expected_result


def test_get_word_count_empty_string():
    assert get_word_count_toolz("") == {}


def test_seq_of_str_to_str():
    seq_of_str = ["one", "two"]
    assert seq_of_str_to_str(seq_of_str) == "one two"
