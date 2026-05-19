import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv("data/sentiment_results.csv")

    # Sentiment count by bank
    sentiment_counts = df.groupby(
        ["bank_name", "sentiment_label"]
    ).size().unstack()

    sentiment_counts.plot(kind="bar", stacked=True)

    plt.title("Sentiment Distribution by Bank")
    plt.xlabel("Bank")
    plt.ylabel("Number of Reviews")

    plt.tight_layout()

    plt.savefig("Sentiment_Distribution.png")

    print("Visualization generated successfully!")

except Exception as e:
    print("Visualization error:", e)