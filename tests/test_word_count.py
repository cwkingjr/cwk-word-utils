import pytest
from cwk_word_utils.word_count import get_word_count


@pytest.fixture
def sample_text():
    return "This cat jumped over this other cat!"


def test_get_word_count(sample_text):
    expected_result = {"this": 2, "cat": 2, "jumped": 1, "over": 1, "other": 1}
    assert get_word_count(sample_text) == expected_result


def test_get_word_count_empty_string():
    assert get_word_count("") == {}
