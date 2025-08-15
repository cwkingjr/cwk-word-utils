from cwk_word_utils.sentiment import extract_sentiment_polarity
import pandas as pd


def test_extract_sentiment_polarity_positive():
    text = "I love programming! It's so much fun."
    sentiment = extract_sentiment_polarity(text)
    assert sentiment > 0


def test_extract_sentiment_polarity_negative():
    text = "Programming is so hard and frustraing at times."
    sentiment = extract_sentiment_polarity(text)
    assert sentiment < 0


def test_extract_sentiment_polarity_with_pandas():
    """Mostly here to show users how to use with pandas."""
    df = pd.DataFrame(
        {
            "description": [
                "I love programming! It's so much fun.",
                "Programming is so hard and frustrating at times.",
            ]
        }
    )
    df["sentiment"] = df["description"].apply(extract_sentiment_polarity)

    assert df.loc[0, "sentiment"] > 0
    assert df.loc[1, "sentiment"] < 0
