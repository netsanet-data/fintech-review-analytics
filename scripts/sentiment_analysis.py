import pandas as pd
from textblob import TextBlob

try:
    # Load cleaned reviews
    df = pd.read_csv("data/cleaned_reviews.csv")

    sentiment_labels = []
    sentiment_scores = []

    # Analyze sentiment
    for review in df["review_text"]:
        analysis = TextBlob(str(review))
        polarity = analysis.sentiment.polarity

        sentiment_scores.append(polarity)

        if polarity > 0:
            sentiment_labels.append("Positive")
        elif polarity < 0:
            sentiment_labels.append("Negative")
        else:
            sentiment_labels.append("Neutral")

    # Add new columns
    df["sentiment_label"] = sentiment_labels
    df["sentiment_score"] = sentiment_scores

    # Save results
    df.to_csv("data/sentiment_results.csv", index=False)

    print(df.head())

except Exception as e:
    print("Error during sentiment analysis:", e)