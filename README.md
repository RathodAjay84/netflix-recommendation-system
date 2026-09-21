# 🎬 Netflix Recommendation System

## 📌 Overview
This project is built using the **Netflix Prize Dataset** to perform **data analysis and build a movie recommendation system** using Machine Learning.

The system analyzes user rating patterns and recommends movies using **Collaborative Filtering (SVD)**.

---

## 🚀 Features
- Data Cleaning & Preprocessing  
- Handling Missing Values  
- Exploratory Data Analysis (EDA)  
- Ratings Distribution Visualization  
- Filtering Low-Activity Users & Movies  
- Recommendation System using SVD  
- Personalized Movie Recommendations  

---

## 📂 Project Structure

# 🎬 Netflix Recommendation System

## 📌 Overview
This project is built using the **Netflix Prize Dataset** to perform **data analysis and build a movie recommendation system** using Machine Learning.

The system analyzes user rating patterns and recommends movies using **Collaborative Filtering (SVD)**.

---

## 🚀 Features
- Data Cleaning & Preprocessing  
- Handling Missing Values  
- Exploratory Data Analysis (EDA)  
- Ratings Distribution Visualization  
- Filtering Low-Activity Users & Movies  
- Recommendation System using SVD  
- Personalized Movie Recommendations  

---

## 📂 Project Structure

netflix-project/

data/
  combined_data_1.txt
  movie_titles.csv

src/
  app.py

outputs/
  netflix_ratings_distribution.png
  recommendation.png

README.md
requirements.txt


---
## 📥 Dataset

The dataset is too large to upload on GitHub.

Download from:
https://www.kaggle.com/datasets/netflix-inc/netflix-prize-data

After downloading, place it inside:
data/combined_data_1.txt

---

## 📈 Key Insights
- Total Customers: **475,257**  
- Active Customers: **470,758**  
- Total Ratings: **24M+**  

### ⭐ Ratings Distribution
- Most ratings are between **3 and 4**
- Very few extreme ratings (1 or 5)

---

## 📊 Visualization

### Ratings Distribution
![Ratings Distribution](outputs/netflix_ratings_distribution.png)

---

## 🧠 Recommendation System Workflow

![Recommendation System](outputs/recommendation.png)

---

## 🤖 Model Details

### Algorithm Used:
- **SVD (Singular Value Decomposition)** from Surprise library  

### Why SVD?
- Handles large sparse datasets  
- Learns hidden patterns between users and movies  
- Used in real-world recommendation systems  

---

## 📉 Data Filtering Strategy
To improve performance:
- Removed low-rated movies  
- Removed inactive users  

### Thresholds:
- Movies below **60th percentile (~908 ratings)** removed  
- Users below **60th percentile (~36 ratings)** removed  

---

## 🎯 Sample Recommendations

| Movie ID | Estimated Rating |
|----------|-----------------|
| 5        | 3.92            |
| 18       | 3.85            |
| 8        | 3.80            |

---

## ▶️ How to Run

### 1. Install dependencies


### 2. Run the project


---

## 🛠️ Tech Stack
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-Surprise  

---

## 💡 Future Improvements
- Build Streamlit Web App  
- Improve recommendation accuracy  
- Add user interface  
- Use deep learning models  

---

## 👨‍💻 Author
**Ajay Rathod**  
B.Tech CSE (AI & ML)

---

## ⭐ Conclusion
This project demonstrates how a real-world recommendation system works using collaborative filtering. It includes complete workflow from data preprocessing to model building and evaluation.
