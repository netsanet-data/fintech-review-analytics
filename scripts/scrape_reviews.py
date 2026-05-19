from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "Dashen": "com.dashen.dashensuperapp"
}

all_reviews = []

try:
    for bank, app_id in apps.items():

        result, _ = reviews(
            app_id,
            lang='en',
            country='et',
            sort=Sort.NEWEST,
            count=200
        )

        for review in result:
            all_reviews.append({
                "review_id": review["reviewId"],
                "review_text": review["content"],
                "rating": review["score"],
                "date": review["at"],
                "bank_name": bank,
                "source": "Google Play Store"
            })

    df = pd.DataFrame(all_reviews)

    print(df.head())

    df.to_csv("data/raw_reviews.csv", index=False)

    print("Scraping completed successfully!")

except Exception as e:
    print("Error during scraping:", e)