> **Try it out live:** 
>[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mallshopperprofiling-6ah2wdyqtkejkpsryiklb3.streamlit.app/)

[Project_Overview]([https://drive.google.com/file/d/FILE_ID/view?usp=sharing](https://drive.google.com/drive/folders/1O3iRH-VSd7jtpULtAuZxcoTNcIfelcJq?usp=drive_link))

# 🛍️ Mall Shopper Profiling (Customer Segmentation)

A Machine Learning project that segments mall customers into distinct groups based on their purchasing behavior using multiple clustering techniques.

---

## 📌 Project Overview

This project applies different **unsupervised learning algorithms** to analyze customer behavior:

- K-Means Clustering  
- DBSCAN (Density-Based Clustering)  
- Agglomerative Hierarchical Clustering  

The goal is to identify meaningful customer groups for better business decision-making.

---

## 🎯 Objective

- Segment mall customers into groups  
- Compare clustering algorithms  
- Visualize patterns in customer spending behavior  

---

## 🧠 Models Used

- K-Means Clustering  
- DBSCAN  
- Agglomerative Clustering (Ward Linkage)  

---

## 📊 Dataset Features

| Feature | Description |
|--------|------------|
| Annual Income (k$) | Customer income |
| Spending Score (1-100) | Spending behavior |

---

## 📷 Results & Visualizations

### 🔹 K-Means Clustering
![KMeans](figure/kmean.png)

---

### 🔹 DBSCAN Clustering
![DBSCAN](figure/DBSCAN.png)

---

### 🔹 Hierarchical Clustering (Dendrogram)
![Dendrogram](figure/dendrogram.png)

---

### 🔹 Agglomerative Clustering Results
![Agglomerative](figure/hier.png)

---

## 📌 Key Insights

- K-Means gives clear segmentation into 5 clusters  
- DBSCAN identifies noise (outliers) effectively  
- Hierarchical clustering helps visualize cluster formation  

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
```

```bash
streamlit run app/streamlit_app.py
```

---

## 📚 Future Improvements

- Add more features like Age & Gender  
- Improve DBSCAN tuning (eps, min_samples)  
- Deploy using Streamlit Cloud  

---

## 👨‍💻 Author

**Deep Vejpara**  
LinkedIn: https://www.linkedin.com/in/deep-vejpara-7a764a366/  

---

⭐ If you like this project, give it a star!
