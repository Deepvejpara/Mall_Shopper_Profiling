Here is a summary of the Exploratory Data Analysis (EDA) based on the provided notebook cells.

## **Data Cleaning & Preparation**

* The `CustomerID` column was dropped from the dataset as it is merely an identifier[cite: 2].
* Columns were renamed for easier programmatic access: `Annual Income (k$)` to `AnnualIncome`, and `Spending Score (1-100)` to `SpendingScore`[cite: 2].
* The cleaned dataset consists of 200 entries and 4 columns: one categorical (`Gender`) and three numerical (`Age`, `AnnualIncome`, `SpendingScore`)[cite: 2].
* Based on the initial statistics, the numerical data does not contain significant outliers[cite: 2].
* Future preprocessing steps will include Label Encoding for the categorical column and Feature Scaling for the numerical columns[cite: 2].

---

## **Numerical Dataset Statistics**

The statistical summary of the 200 customers reveals the following baseline metrics[cite: 2]:

| Feature | Minimum | Mean | Maximum |
| :--- | :--- | :--- | :--- |
| **Age** | 18.00 | 38.85 | 70.00 |
| **AnnualIncome (k$)** | 15.00 | 60.56 | 137.00 |
| **SpendingScore (1-100)** | 1.00 | 50.20 | 99.00 |

---

## **Categorical Distribution: Gender**

The customer base shows a nearly 60-40 split favoring female shoppers[cite: 2]:
* **Female:** 112 customers[cite: 2]
* **Male:** 88 customers[cite: 2]

---

## **Univariate Distribution Insights**

The plotted distributions for the numerical features highlight several key trends about the mall's customer base:

* **Age:** The customer distribution peaks around the 30 to 35 age range[cite: 2]. The data is slightly right-skewed, trailing off as ages approach 70, though there is a notable spike in younger customers between 18 and 20[cite: 2].
* **Annual Income:** Income follows a fairly normal, though slightly right-skewed, distribution[cite: 2]. The majority of customers earn between 40k and 80k annually, while a smaller group of high earners stretches the distribution up to nearly 140k[cite: 2].
* **Spending Score:** Spending scores show a massive, distinct peak right in the middle around 40 to 50[cite: 2]. Outside of this central peak, the distribution remains relatively uniform across both the higher and lower score ranges[cite: 2].