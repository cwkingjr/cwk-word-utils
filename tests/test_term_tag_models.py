import pytest
from cwk_word_utils.term_tag_models import Tag, Terms, TagTerms, tag_terms


def test_tag_class():
    tag = Tag(tag="injury")
    assert type(tag) == Tag
    assert str(tag) == "Tag: injury"
    assert repr(tag) == "Tag(tag='injury')"


def test_terms_class():
    terms = Terms(terms=["injury", "accident", "incident"])
    assert type(terms) == Terms
    assert str(terms) == "Terms: ['injury', 'accident', 'incident']"
    assert repr(terms) == "Terms(terms=['injury', 'accident', 'incident'])"


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


def test_tag_terms():
    my_content = "This is a letter of claim regarding an accident."
    my_tag_terms = [
        TagTerms(
            tag=Tag(tag="injury"), terms=Terms(terms=["injury", "accident", "incident"])
        )
    ]
    tags = tag_terms(tag_terms=my_tag_terms, content=my_content)
    assert tags == "tags"
