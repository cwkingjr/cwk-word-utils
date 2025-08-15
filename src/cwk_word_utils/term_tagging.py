"""Library for matching terms in text and tagging them with their corresponding tags."""

from toolz import curry

from cwk_word_utils.term_tag_models import TagTerms


@curry
def get_content_tags(tag_terms: list[TagTerms], content: str) -> list[str]:
    """Tag terms in the content based on the provided tag_terms and return list of tag strs."""
    found_tags = set()
    for tag_term in tag_terms:
        for term in tag_term.terms.terms:
            if term.lower() in content.lower():
                found_tags.add(tag_term.tag.tag)
    return sorted(found_tags)


@curry
def get_content_tags_return_delimited(
    tag_terms: list[TagTerms],
    content: str,
    delimiter: str = "|",
) -> str:
    """Tag terms in the content and return tag strs as a delimited string."""
    if delimiter not in ["|", ",", ";", ":", " "]:
        msg = "Delimiter must be one of '|', ',', ';', ':', or ' '"
        raise ValueError(msg)
    tags = get_content_tags(tag_terms, content)
    return delimiter.join(tags)
