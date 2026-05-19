# Fintech Review Analytics

## Project Overview
This project analyzes customer reviews from Ethiopian fintech mobile banking applications using data collection, preprocessing, sentiment analysis, and thematic analysis techniques.

The project focuses on three banks:
- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The reviews were collected from Google Play Store using the `google-play-scraper` library.

---

## Project Structure

fintech-review-analytics/
│
├── data/
├── notebooks/
├── scripts/
│   ├── scrape_reviews.py
│   ├── preprocess_reviews.py
│   ├── sentiment_analysis.py
│   └── thematic_analysis.py
│
├── tests/
├── .github/workflows/unittests.yml
├── requirements.txt
├── .gitignore
└── README.md

---

## Data Collection

The review data was collected using:
- google-play-scraper
- Google Play Store reviews

Collected fields include:
- review_id
- review_text
- rating
- date
- bank_name
- source

---

## Preprocessing Steps

The preprocessing script performs:
- duplicate removal using review_id
- missing value handling
- date normalization to YYYY-MM-DD format

---

## Sentiment Analysis

Sentiment analysis was implemented using TextBlob.

The script generates:
- sentiment_label
- sentiment_score

The reviews are classified as:
- Positive
- Negative
- Neutral

---

## Thematic Analysis

Thematic analysis was implemented using TF-IDF keyword extraction from scikit-learn.

Common keywords extracted include:
- banking
- transfer
- update
- mobile
- service

---

## Limitations

Some limitations encountered:
- Google Play reviews may contain spam or short comments
- Internet connectivity may affect scraping
- Some reviews are written in mixed languages

---

## Requirements

Install dependencies using:

pip install -r requirements.txt
## Database Engineering

PostgreSQL database integration was implemented using SQLAlchemy.

Files included:
- schema.sql
- scripts/database_insert.py

The database contains:
- banks table
- reviews table

---

## Visualizations

The project includes sentiment distribution visualizations generated using Matplotlib.

Generated charts:
- Sentiment distribution by bank
- Keyword/theme analysis charts