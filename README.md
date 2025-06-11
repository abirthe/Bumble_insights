**README.md**

# 🔍 Bumble Reviews - Exploratory Data Analysis

This project analyzes over 160,000 user reviews of the Bumble app from the Google Play Store. The goal is to explore trends in user satisfaction, engagement, and company response behavior.

---

## 📄 Dataset Overview

* **Source**: Google Play Store (via Kaggle)
* **Rows**: 167,000+
* **Fields**: `score`, `thumbsUpCount`, `at` (date), `content`, `repliedAt`

---

## 💡 Key Questions

* What ratings do users leave most often?
* Which reviews get the most thumbs-up?
* How do ratings change over the years?
* How quickly does Bumble reply to reviews?
* Are longer reviews tied to certain star ratings?

---

## 🔍 Key Insights

* **1-star reviews** receive the **most thumbs-up**, showing community alignment on negative feedback.
* Average review scores have **declined slightly since 2019**.
* **3-star reviews** tend to be longer and more thoughtful.
* Bumble tends to **reply faster** to higher-rated reviews.
* Many **1- and 2-star reviews** go unanswered.

---

## 📈 Visual Highlights

* Histogram of review counts by score
* Time-series plot of average score by year
* Average reply time per score (in days)
* Distribution of review lengths by score

All plots are saved in the `visualizations/` folder.

---

## ⚙️ How to Run

```bash
pip install pandas matplotlib
python Bumble_Insights_code.py
```

Make sure the dataset is placed in the `data/` folder or update the script path accordingly.

---

## ✍️ License

This project is licensed under the **GNU General Public License v3.0**.

---

## 🚀 Author

**\[Abir]** - Data Enthusiast | Exploring product feedback at scale.
