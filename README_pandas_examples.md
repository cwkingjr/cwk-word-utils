## Sentiment Polarity (returns range of -1 to 1)

```python
from cwk_word_utils.sentiment import get_sentiment_polarity
import pandas as pd

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
from cwk_word_utils.term_tagging import (
    create_tag_terms,
    get_content_tags,
    get_content_tags_return_delimited,
)

import pandas as pd

## my data
my_content = "This is a letter of claim regarding an accident."

my_tag_terms = [
    create_tag_terms(tag_str="claims", terms_str_list=["insurance", "letter of claim", "documentation for claims"]),
    create_tag_terms(tag_str="injury", terms_str_list=["injury", "accident", "incident"]),
]

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

## Word Count

```python
from cwk_word_utils.word_count import get_word_count_counter
import pandas as pd

my_df_data = {
    "text_column": [
        "chair chair chair table table lamp.",
        "lamp sits on the table beside the chair.",
        "there is a fork on the table beside the plate.",
    ]
}

df = pd.DataFrame(my_df_data)

# gather all text from a certain column of the dataframe
joined_string = df['text_column'].str.cat(sep=' ')

# process the info
print(get_word_count_counter(joined_string, return_most_common=2))

```
