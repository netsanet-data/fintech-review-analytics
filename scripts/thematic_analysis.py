import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

try:
    # Load cleaned review data
    df = pd.read_csv("data/cleaned_reviews.csv")

    # TF-IDF keyword extraction
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=20
    )

    X = vectorizer.fit_transform(df["review_text"].astype(str))

    keywords = vectorizer.get_feature_names_out()

    print("Top Keywords:")
    print(keywords)

except Exception as e:
    print("Error during thematic analysis:", e)