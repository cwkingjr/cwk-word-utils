import pytest
from cwk_word_utils.term_tag_models import Tag, Terms, TagTerms
from cwk_word_utils.term_tagging import (
    create_tag_terms,
    get_content_tags,
    get_content_tags_return_delimited,
)
import pandas as pd


@pytest.fixture(scope="session")
def content_str():
    return "This is a letter of claim regarding an accident."


@pytest.fixture(scope="session")
def tag_terms_list():
    return [
        TagTerms(
            tag=Tag(tag="claims"),
            terms=Terms(
                terms=["insurance", "letter of claim", "documentation for claims"],
            ),
        ),
        TagTerms(
            tag=Tag(tag="injury"),
            terms=Terms(terms=["injury", "accident", "incident"]),
        ),
    ]


@pytest.fixture(scope="session")
def dataframe_data():
    DATAFRAME_DATA = {
        "text_column": [
            "This is a letter of claim regarding an accident.",
            "No relevant terms here.",
            "An incident occurred leading to injury.",
        ]
    }
    return DATAFRAME_DATA


def test_create_tag_terms():
    my_tag_str = "mytest"
    my_terms_str_list = ["one", "two", "three"]
    my_tagterms_instance = create_tag_terms(
        tag_str=my_tag_str, terms_str_list=my_terms_str_list
    )
    assert (
        str(type(my_tagterms_instance))
        == "<class 'cwk_word_utils.term_tag_models.TagTerms'>"
    )
    assert my_tagterms_instance.tag.tag == my_tag_str
    assert my_tagterms_instance.terms.terms == my_terms_str_list


def test_get_content_tags(content_str, tag_terms_list):
    """Test the get_content_tags function that returns a python list of tag strs."""
    result = get_content_tags(tag_terms=tag_terms_list, content=content_str)
    assert isinstance(result, list)
    assert "claims" in result
    assert "injury" in result
    assert len(result) == 2  # noqa: PLR2004


def test_get_content_tags_return_delimited(content_str, tag_terms_list):
    """Test the get_content_tags_return_delimited function."""

    # Test with default delimiter
    result = get_content_tags_return_delimited(
        tag_terms=tag_terms_list, content=content_str
    )
    assert result == "claims|injury"

    # Test with custom delimiter
    result = get_content_tags_return_delimited(
        tag_terms=tag_terms_list, content=content_str, delimiter=";"
    )
    assert result == "claims;injury"

    # Test with invalid delimiter
    with pytest.raises(ValueError):
        get_content_tags_return_delimited(
            tag_terms=tag_terms_list, content=content_str, delimiter="invalid"
        )


def test_curried_get_content_tags_return_delimited(content_str, tag_terms_list):
    """Test a curried get_content_tags_return_delimited function."""
    get_tags_delimited = get_content_tags_return_delimited(tag_terms=tag_terms_list)
    result = get_tags_delimited(content=content_str)
    assert result == "claims|injury"


def test_curried_get_content_tags(content_str, tag_terms_list):
    """Test a curried get_content_tags function."""
    get_tags_list = get_content_tags(tag_terms=tag_terms_list)
    result_list = get_tags_list(content=content_str)
    assert isinstance(result_list, list)
    assert "claims" in result_list
    assert "injury" in result_list
    assert len(result_list) == 2  # noqa: PLR2004


def test_integration_with_pandas_not_curried(dataframe_data, tag_terms_list):
    """Test integration with pandas DataFrame."""

    df = pd.DataFrame(dataframe_data)
    df["tags"] = df["text_column"].apply(
        lambda x: get_content_tags_return_delimited(
            tag_terms=tag_terms_list, content=x
        ),
    )

    assert df.loc[0, "tags"] == "claims|injury"
    assert df.loc[1, "tags"] == ""
    assert df.loc[2, "tags"] == "injury"


def test_integration_with_pandas_curried(dataframe_data, tag_terms_list):
    """Test integration with pandas DataFrame using curried functions."""
    # Create curried function
    get_tags = get_content_tags(tag_terms=tag_terms_list)

    df = pd.DataFrame(dataframe_data)
    # Apply curried function
    df["tags"] = df["text_column"].apply(lambda x: get_tags(content=x))

    assert df.loc[0, "tags"] == ["claims", "injury"]
    assert df.loc[1, "tags"] == []
    assert df.loc[2, "tags"] == ["injury"]
