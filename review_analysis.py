
import pandas as pd
import glob
import os

files = sorted(glob.glob("reviews_*.csv"))

total_rows = 0
rating_sum = 0
rating_count = 0
recommended_sum = 0
recommended_count = 0
missing_review_text = 0
missing_rating = 0

print("CUSTOMER REVIEW ANALYSIS")
print("=" * 40)

for file in files:
    print("Processing:", file)

    for chunk in pd.read_csv(file, chunksize=100000):
        total_rows += len(chunk)

        ratings = pd.to_numeric(chunk["rating"], errors="coerce")
        rating_sum += ratings.sum()
        rating_count += ratings.notna().sum()
        missing_rating += ratings.isna().sum()

        recommended = pd.to_numeric(
            chunk["is_recommended"], errors="coerce"
        )
        recommended_sum += recommended.sum()
        recommended_count += recommended.notna().sum()

        missing_review_text += chunk["review_text"].isna().sum()

print("\nANALYSIS RESULTS")
print("=" * 40)
print("Review files:", len(files))
print("Total reviews:", f"{total_rows:,}")

if rating_count:
    print("Average rating:", round(rating_sum / rating_count, 2))

if recommended_count:
    print(
        "Recommendation rate (%):",
        round(100 * recommended_sum / recommended_count, 2)
    )

print("Missing ratings:", f"{missing_rating:,}")
print("Missing review texts:", f"{missing_review_text:,}")

print("\nReview analysis completed!")
