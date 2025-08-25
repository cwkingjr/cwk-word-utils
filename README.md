# CWK Word Utilities

Nothing fancy here as it's just a place to stash some word-related tools so they can be generally available in different scenarios.

## Modules so far

### Term Tagging (term_tagging.py)

- get_content_tags
- get_content_tags_return_delimited

The idea here is to allow users to codify a list of tags and a list of search terms for each tag, and then run those against some text content. If any of the terms in the terms list for that tag match, then that tag will be included in a set of matched tags to return. The two functions below are basically to allow the user to decide how they want the set of matched tag strings to be returned, either as a Python List or as a delimited string, with the ability to specify the delimiter within a small selection of commonly used delimiters. A pipe char is the default because it tends to break fewer things, especially when dealing with CSV files.

Those two functions above can be used currently when passing in a list of `TagTerms`, consisting of `Tag` and `Terms`: see term_tagging_models. The reason for using `Tag`, `Terms`, and `TagTerms` is to provding `Pydantic` runtime validation of the incomming data.

Also, both of those get*content* functions are curried, so you can create partials from them to make your partialed function easier to call if you are using it in several places. Or, said another way, you can call one of those functions with your `TagTerms` list and generate a curried function that you can use the rest of the time where you only have pass in your content.

The tests for these functions show how to create and use a curried function.

### Sentiment (sentiment.py)

- get_sentiment_polarity

This function simply uses the `textblob` module to generate the polarity `[-1,1]` of the passed in text content.

### Word Count

- get_word_count_toolz
- get_word_count_counter

These functions use various text cleaning, stopword removal, and frequency/counting techniques to return the counts of words within a string text input. Have a look at the function docs within the module for more details.

## Tests can provide insight

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

text = "I love programming! It's so much fun."
sentiment_polarity = get_sentiment_polarity(text)
print(sentiment_polarity)
```

## Tag Terms

```python
from cwk_word_utils.term_tagging import (
    create_tag_terms,
    get_content_tags,
    get_content_tags_return_delimited,
)

## my data
my_content = "This is a letter of claim regarding an accident."

my_tag_terms = [
    create_tag_terms(tag_str="claims", terms_str_list=["insurance", "letter of claim", "documentation for claims"]),
    create_tag_terms(tag_str="injury", terms_str_list=["injury", "accident", "incident"]),
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
```

## Word Count

The word count functions attempt to remove stop words prior to doing the count
for the most common words. They accomplish stop word removal via the functions
in the remove_stop_words.py module. See that module for more details on stop
word removal.

```python
from cwk_word_utils.word_count import get_word_count_counter, get_word_count_toolz

text = "chair chair chair table table"

result = get_word_count_toolz(text)
#result == {"chair": 3, "table": 2,}

# defaults == 50 and "spacy"
result = get_word_count_counter(text)
result = get_word_count_counter(text, return_most_common=75)
result = get_word_count_counter(text, return_most_common=15, stop_word_lib="spacy")
result = get_word_count_counter(text, stop_word_lib="nltk")
result = get_word_count_counter(text, return_most_common=25, stop_word_lib="nltk")

#result == [("chair", 3),("table", 2),]
```
