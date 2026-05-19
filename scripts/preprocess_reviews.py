import pandas as pd

try:
    # Load raw review data
    df = pd.read_csv("data/raw_reviews.csv")

    # Remove duplicate reviews using review_id
    df = df.drop_duplicates(subset=["review_id"])

    # Drop rows with missing review text or rating
    df = df.dropna(subset=["review_text", "rating"])

    # Normalize date format
    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

    # Save cleaned data
    df.to_csv("data/cleaned_reviews.csv", index=False)

    print("Preprocessing completed successfully!")

except Exception as e:
    print("Error during preprocessing:", e)