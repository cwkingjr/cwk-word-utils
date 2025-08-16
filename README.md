# CWK Word Utilities

Nothing fancy here as it's just a place to stash some word-related tools so they can be generally available in different scenarios.

## Modules so far

### Term Tagging (term_tagging.py)

- get_content_tags
- get_content_tags_return_delimited

The idea here is to allow users to codify a list of tags and a list of search terms for each tag, and then run those against some text content. If any of the terms in the terms list for that tag match, then that tag will be included in a set of matched tags to return. The two functions below are basically to allow the user to decide how they want the set of matched tag strings to be returned, either as a Python List or as a delimited string, with the ability to specify the delimiter within a small selection of commonly used delimiters. A pipe char is the default because it tends to break fewer things, especially when dealing with CSV files.

Those two functions above can be used currently when passing in a list of `TagTerms`, consisting of `Tag` and `Terms`, (see term_tagging_models) but I will add functionality to make creating lists `TagTerms` easier to generate. I also want to add functionality for working with a `TOML` config file so non-dev users can do the upkeep on their desired tags and terms, and then we can suck that config file in and generate `TagTerms` from it. The reason for using `Tag`, `Terms`, and `TagTerms` is to provding `Pydantic` validation of the incomming data.

Also, both of those get_content\* functions are curried, so you can create partials from them to make your partialed function easier to call if you are using it in several places. Or, said another way, you can call one of those functions with your `TagTerms` list and generate a curried function that you can use the rest of the time where you only have pass in your content.

The tests for these functions show how to create and use a curried function.

### Sentiment (sentiment.py)

- get_sentiment_polarity

This function simply uses the `textblob` module to generate the polarity `[-1,1]` of the passed in text content.

## Tests

Sometimes looking at the tests in the tests directory will help with understanding as the asserts in the tests show the expected outputs for various calls.

## Installation

This library is not published on PyPI, so to install it as a dependency, add this to your pyproject.toml:

```toml
"cwk-word-utils @ git+https://github.com/cwkingjr/cwk-word-utils.git@main",
```

# Examples

## Sentiment Polarity (returns range of -1 to 1)

```python
from cwk_word_utils.sentiment import get_sentiment_polarity

import pandas as pd

# simple call
text = "I love programming! It's so much fun."
sentiment_polarity = get_sentiment_polarity(text)
print(sentiment_polarity)

# applying to dataframe
df = pd.DataFrame(
    {
        "description": [
            "I love programming! It's so much fun.",
            "Programming is so hard and frustrating at times.",
        ]
    }
)

df["sentiment"] = df["description"].apply(get_sentiment_polarity)

print(df)
```

## Tag Terms

```python
from cwk_word_utils.term_tag_models import Tag, Terms, TagTerms
from cwk_word_utils.term_tagging import (
    get_content_tags,
    get_content_tags_return_delimited,
)

import pandas as pd

## my data
my_content = "This is a letter of claim regarding an accident."
my_tag_terms = [
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

## simple calls

# returns Python list of tag strs
result_list = get_content_tags(tag_terms=my_tag_terms, content=my_content)

# returns pipe "|" (default) delimited str of tag strs
result_str = get_content_tags_return_delimited(tag_terms=my_tag_terms, content=my_content)

# returns a colon delimited str of tag strs
result_str = get_content_tags_return_delimited(tag_terms=my_tag_terms, content=my_content, delimiter=":")

## currying

# creates a curried function that includes the tag_terms assignment
get_tags_curried = get_content_tags(tag_terms=my_tag_terms)

# returns Python list of tag strs
result_list = get_tags_curried(content=my_content)

## dataframe calls

# applying to dataframe
my_df_data = {
    "text_column": [
        "This is a letter of claim regarding an accident.",
        "No relevant terms here.",
        "An incident occurred leading to injury.",
    ]
}

df = pd.DataFrame(my_df_data)

# non-curried call
df["tags"] = df["text_column"].apply(
    lambda x: get_content_tags(tag_terms=my_tag_terms, content=x)
    )

# curried call
# create curried function
get_tags = get_content_tags(tag_terms=my_tag_terms)
# apply curried function
df["tags"] = df["text_column"].apply(lambda x: get_tags(content=x))
```
