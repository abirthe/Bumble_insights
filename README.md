**README.md**

# 📊 Bumble App Review Analysis (Google Play Store)

A deep-dive into 167,000+ Google Play Store reviews of the **Bumble** dating app. This analysis focuses on user sentiment, engagement behavior, and Bumble's responsiveness to user feedback across time. The project provides rich visualizations and interprets key behavioral patterns behind review scores.

---

## 📁 Dataset Summary

* **Source**: Kaggle / Google Play Store
* **Total Reviews**: \~167,000
* **Important Fields**:

  * `score`: User rating (1 to 5)
  * `thumbsUpCount`: Number of helpful votes received
  * `content`: Text content of the review
  * `at`: Date the review was posted
  * `repliedAt`: Date Bumble replied (if any)

---

## ❓ Analytical Objectives

This project aims to answer:

* What is the distribution of review ratings?
* Which scores receive the most community engagement?
* How has sentiment evolved annually?
* Are certain review scores associated with longer comments?
* How responsive is Bumble to various rating levels?

---

## 🔍 Key Insights

### ⭐ Rating Trends

* **1-star ratings dominate** the review count and receive **the highest number of thumbs-up**, suggesting strong user agreement on negative experiences.
* **5-star reviews** follow in volume but with much lower engagement.

### 🕒 Sentiment Over Time

* Average review scores **peaked in 2019** but show a **steady decline through 2024**, hinting at user dissatisfaction or unmet expectations.

### ✍️ Review Depth

* **2-star and 3-star reviews** are generally **longer**, indicating users provide more detailed feedback when partially dissatisfied.

### 👍 Engagement Patterns

* **1-star reviews attract the highest number of likes**, highlighting that critical feedback is more supported or relatable among users.

### ⏱️ Response Dynamics

* Bumble **responds faster to higher-rated reviews**, with **reply time increasing significantly for 4- and 5-star reviews**, likely due to prioritizing critical feedback slower or possibly neglecting praise.
* **Many low-rated reviews remain unanswered**, with **1-star and 5-star reviews having the most unreplied cases**, showing inconsistency in response management.

---

## 📊 Visualizations (Located in `visualizations/` folder)

1. **Rating vs. Number of Reviews**
2. **Total Thumbs-Up per Review Score**
3. **Average Review Length by Score**
4. **Score Distribution per Year (Stacked Bar)**
5. **Average Review Score Over Time**
6. **Average Reply Time by Score**
7. **Count of Unreplied Reviews by Score**

Each plot was used to draw insights based on trends, anomalies, and behavioral indicators.

---

## 🚀 Getting Started

### 🔧 Requirements

* Python 3.x
* pandas
* matplotlib

### ▶️ Run Instructions

```bash
pip install pandas matplotlib
python Bumble_Insights_code.py
```

Ensure the dataset CSV is placed in the script directory or adjust the filepath accordingly.

---

## 📜 License

Licensed under the **GNU General Public License v3.0**. See the `LICENSE` file for more info.

---

## 👤 Author

**Abir**
Data Enthusiast | Exploring real-world feedback through visual and statistical narratives.

🔗 [LinkedIn](https://www.linkedin.com/in/abir-hossain-500756349/)
