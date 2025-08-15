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

- extract_sentiment_polarity

This function simply uses the `textblob` module to generate the polarity `[-1,1]` of the passed in text content.

## Docs

Please just see the tests in this repo for examples of how to use these functions.

## Tests

So far I'm trying to include tests for these modules that show how to use them with a `Pandas Dataframe`.
