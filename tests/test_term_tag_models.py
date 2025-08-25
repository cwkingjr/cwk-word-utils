from cwk_word_utils.term_tag_models import Tag, Terms, TagTerms
import pytest


def test_tag_class():
    tag = Tag(tag="injury")
    assert type(tag) == Tag
    assert str(tag) == "Tag: injury"
    assert repr(tag) == "Tag(tag='injury')"


def test_tag_not_str():
    with pytest.raises(ValueError):
        Tag(tag=42)


def test_terms_class():
    terms = Terms(terms=["injury", "accident", "incident"])
    assert type(terms) == Terms
    assert str(terms) == "Terms: ['injury', 'accident', 'incident']"
    assert repr(terms) == "Terms(terms=['injury', 'accident', 'incident'])"


def test_terms_not_str_list():
    with pytest.raises(ValueError):
        Terms(terms=[2, 3, 4])


def test_tag_terms_class():
    tag_terms = TagTerms(
        tag=Tag(tag="injury"),
        terms=Terms(terms=["injury", "accident", "incident"]),
    )
    assert type(tag_terms) == TagTerms
    assert (
        str(tag_terms)
        == "TagTerms(tag=Tag: injury, terms=Terms: ['injury', 'accident', 'incident'])"
    )
    assert (
        repr(tag_terms)
        == "TagTerms(tag=Tag(tag='injury'), terms=Terms(terms=['injury', 'accident', 'incident']))"
    )
