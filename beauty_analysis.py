
import pandas as pd
import matplotlib.pyplot as plt

# Load product data
df = pd.read_csv("product_info.csv")

print("=" * 50)
print("BEAUTY PRODUCT DATA ANALYSIS")
print("=" * 50)

# Basic statistics
print("\nTotal products:", len(df))
print("Unique brands:", df["brand_name"].nunique())
print("Average rating:", round(df["rating"].mean(), 2))
print("Average price (USD):", round(df["price_usd"].mean(), 2))
print("Total missing values:", df.isnull().sum().sum())

# Top 10 highest-rated products
top_rated = df.dropna(subset=["rating"]).nlargest(10, "rating")

print("\nTOP 10 HIGHEST-RATED PRODUCTS")
print(
    top_rated[
        ["product_name", "brand_name", "rating", "reviews", "price_usd"]
    ].to_string(index=False)
)

# Top 10 most-loved brands
brand_stats = df.groupby("brand_name").agg(
    total_loves=("loves_count", "sum"),
    total_products=("product_id", "count"),
    avg_rating=("rating", "mean")
)

top_brands = brand_stats.nlargest(10, "total_loves")

print("\nTOP 10 MOST-LOVED BRANDS")
print(top_brands.round(2).to_string())

# Graph 1: Most-loved brands
top_brands["total_loves"].sort_values().plot(
    kind="barh", figsize=(10, 6),
    title="Top 10 Most-Loved Beauty Brands"
)
plt.xlabel("Total Loves")
plt.tight_layout()
plt.savefig("top_10_beauty_brands.png", dpi=150)
plt.close()

# Graph 2: Highest-rated products
rated = top_rated.sort_values("rating")
plt.figure(figsize=(10, 7))
plt.barh(rated["product_name"].str.slice(0, 35), rated["rating"])
plt.xlabel("Rating out of 5")
plt.title("Top 10 Highest-Rated Beauty Products")
plt.xlim(0, 5.2)
plt.tight_layout()
plt.savefig("top_10_rated_products.png", dpi=150)
plt.close()

print("\nAnalysis completed successfully!")
print("Graphs saved in the project folder.")
