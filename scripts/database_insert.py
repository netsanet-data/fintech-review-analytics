import pandas as pd
from sqlalchemy import create_engine

try:
    # PostgreSQL connection
    engine = create_engine(
        "postgresql://postgres:password@localhost:5432/fintech_reviews"
    )

    # Load cleaned data
    df = pd.read_csv("data/sentiment_results.csv")

    # Insert into database
    df.to_sql("reviews", engine, if_exists="append", index=False)

    print("Data inserted successfully!")

except Exception as e:
    print("Database insertion error:", e)