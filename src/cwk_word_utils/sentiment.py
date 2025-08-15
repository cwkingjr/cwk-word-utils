"""Sentiment analysis utilities."""

from textblob import TextBlob


def extract_sentiment_polarity(text: str):
    """Extract sentiment polarity using textblob: range [-1, 1]."""
    tb = TextBlob(text)
    return tb.sentiment.polarity
