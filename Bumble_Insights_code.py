import pandas as pd
import matplotlib.pyplot as plt
import os
# ----------------------------------------
# STEP 1: Reading Data.py & Initial Exploration
# ----------------------------------------

print("STEP 1: Reading Bumble Google Play Store Review Data.py")

try:
    bumble_data = pd.read_csv(r"D:\Data Science\Bumble_Insights\Bumble_insights\bumble_google_play_reviews.csv")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()


print("\nChecking for missing values (any):")
print(bumble_data.isna().any())

print("\nTotal missing values per column:")
print(bumble_data.isna().sum())

# ----------------------------------------
# STEP 2: Cleaning Data.py
# ----------------------------------------

print("\nSTEP 2: Cleaning data (removing nulls and duplicates)")

# Remove duplicate reviews based on 'reviewId'
bumble_data.drop_duplicates(subset=['reviewId'], inplace=True)

# Fill NaNs with appropriate default values
bumble_data["content"] = bumble_data["content"].fillna("")
bumble_data["reviewCreatedVersion"] = bumble_data["reviewCreatedVersion"].astype(str).fillna("unknown")
bumble_data["appVersion"] = bumble_data["appVersion"].astype(str).fillna("unknown")
bumble_data["replyContent"] = bumble_data["replyContent"].fillna("")

# Convert date columns before filling
bumble_data["at"] = pd.to_datetime(bumble_data["at"], errors='coerce')
bumble_data["repliedAt"] = pd.to_datetime(bumble_data["repliedAt"], errors='coerce')

# Fill missing repliedAt with corresponding 'at' date
bumble_data["repliedAt"] = bumble_data["repliedAt"].fillna(bumble_data["at"])

print("\nAny nulls left after cleaning?")
print(bumble_data.isna().any())

print("\nDataset info after cleaning:")
print(bumble_data.info())

# ----------------------------------------
# STEP 3: Descriptive Statistics & Analysis
# ----------------------------------------

print("\nSTEP 3: Descriptive Statistics of Review Scores")

score_mean = bumble_data["score"].mean()
score_std = bumble_data["score"].std()
score_counts = bumble_data["score"].value_counts().sort_index()
score_counts_amount = bumble_data["score"].value_counts(normalize=True).sort_index()
score_mode = bumble_data["score"].mode()[0]

print(f"Average score: {score_mean:.2f}")
print(f"Standard deviation: {score_std:.2f}")

# Ensure 'visualizations/' directory exists
os.makedirs("visualizations", exist_ok=True)

# --- Load and preprocess your data here ---
# bumble_data = pd.read_csv(...)
# Assume 'bumble_data' and 'score_counts' are already prepared as per your script

# -------------------------
# Plot 1: Review count per score
print("\nReview count per score:")
print(score_counts)

plt.figure(figsize=(8, 6))
score_counts.plot(kind='bar', rot=0, color='skyblue', edgecolor='black')
plt.xlabel("Review Score", fontsize=12)
plt.ylabel("Number of Reviews", fontsize=12, color="darkblue")
plt.title("Rating vs Number of Reviews", fontsize=16, color="darkred")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("visualizations/review_count_per_score.png", dpi=300)
plt.show()

# -------------------------
# Plot 2: Total thumbs up per score
print("\nTotal thumbs up per score:")
thumbs_up_by_score = bumble_data.groupby("score")["thumbsUpCount"].sum().sort_index()
print(thumbs_up_by_score)

plt.figure(figsize=(8,5))
thumbs_up_by_score.plot(kind='bar', color='lightgreen', edgecolor='black', rot=0)
plt.xlabel("Review Score")
plt.ylabel("Total Thumbs Up")
plt.title("Total Thumbs Up per Review Score")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("visualizations/thumbs_up_per_score.png", dpi=300)
plt.show()

# ----------------------------------------
# Extract review year from datetime
bumble_data['review_year'] = bumble_data["at"].dt.year
bumble_data_year = bumble_data.dropna(subset=['review_year'])

# -------------------------
# Plot 3: Average review score per year
avg_score_per_year = bumble_data_year.groupby("review_year")["score"].mean()
print("\nAverage review score per year:")
print(avg_score_per_year)

plt.figure(figsize=(10,5))
avg_score_per_year.plot(marker='o', linestyle='-')
plt.xlabel("Year")
plt.ylabel("Average Review Score")
plt.title("Average Review Score Over Years")
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("visualizations/avg_score_per_year.png", dpi=300)
plt.show()

# -------------------------
# Plot 4: Number of each score per year
score_dist_per_year = bumble_data_year.groupby("review_year")["score"].value_counts().unstack(fill_value=0).sort_index()
print("\nNumber of each score per year:")
print(score_dist_per_year)

plt.figure(figsize=(12,6))
score_dist_per_year.plot(kind='bar', stacked=True, colormap='tab20', edgecolor='black', rot=0)
plt.xlabel("Year")
plt.ylabel("Number of Reviews")
plt.title("Score Distribution per Year (Stacked Bar)")
plt.legend(title="Score", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("visualizations/score_dist_per_year.png", dpi=300)
plt.show()

# -------------------------
# Plot 5: Average review length by score
bumble_data["review_len"] = bumble_data["content"].apply(len)
avg_review_len_by_score = bumble_data.groupby("score")["review_len"].mean().sort_index()
print("\nAverage review length by score:")
print(avg_review_len_by_score)

plt.figure(figsize=(8,6))
avg_review_len_by_score.plot(kind='bar', color='lightblue', edgecolor='black', rot=0)
plt.xlabel("Review Score")
plt.ylabel("Average Review Length (characters)")
plt.title("Average Review Length by Score")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("visualizations/avg_review_length_by_score.png", dpi=300)
plt.show()

# -------------------------
# Plot 6: Average reply time by score (excluding not replied items)
bumble_data["reply_time"] = bumble_data["repliedAt"] - bumble_data["at"]
positive_reply_time = bumble_data[bumble_data["reply_time"] > pd.Timedelta(0)].copy()
avg_reply_time_by_score = positive_reply_time.groupby("score")["reply_time"].mean().sort_index()
print("\nAverage reply time by score (excluding not replied items):")
print(avg_reply_time_by_score)

avg_reply_time_days = avg_reply_time_by_score.dt.total_seconds() / (3600 * 24)

plt.figure(figsize=(8,6))
avg_reply_time_days.plot(kind='bar', color='lightcoral', edgecolor='black', rot=0)
plt.xlabel("Review Score")
plt.ylabel("Average Reply Time (days)")
plt.title("Average Reply Time by Review Score (excluding not replied items)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("visualizations/avg_reply_time_by_score.png", dpi=300)
plt.show()

# -------------------------
# Plot 7: Count of reviews without replies grouped by score
has_not_replied = bumble_data[bumble_data["reply_time"] == pd.Timedelta(0)]
no_reply_counts = has_not_replied.groupby("score")["repliedAt"].count().sort_index()
print("\nCount of reviews without replies grouped by score:")
print(no_reply_counts)

plt.figure(figsize=(8,5))
no_reply_counts.plot(kind='bar', color='orange', edgecolor='black', rot=0)
plt.xlabel("Review Score")
plt.ylabel("Count of Reviews Without Replies")
plt.title("Count of Reviews Without Replies by Score")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("visualizations/reviews_without_replies_by_score.png", dpi=300)
plt.show()
