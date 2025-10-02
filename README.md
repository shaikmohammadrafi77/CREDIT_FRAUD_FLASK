Credit Card Fraud Detection Using Machine Learning
📌 Project Overview

Credit card fraud is a growing issue worldwide, with billions of dollars lost each year due to fraudulent transactions. This project applies machine learning algorithms to detect fraudulent credit card transactions. By analyzing historical transaction data, the system can classify whether a new transaction is fraudulent (1) or genuine (0).

The project is based on the Credit Card Fraud Dataset (2013) from Kaggle, which contains anonymized transactions of European cardholders over two days.

🎯 Goals

Detect fraudulent credit card transactions effectively.

Compare different ML algorithms to determine the most accurate and efficient model.

Reduce false positives and false negatives to improve customer trust.

📂 Dataset

Source: Kaggle – Credit Card Fraud Detection Dataset

Records: 284,808 transactions

Features: 31 attributes

28 numerical attributes (transformed using PCA for confidentiality)

Time – seconds elapsed between transactions

Amount – transaction amount

Class – Target label (1 = Fraud, 0 = Not Fraud)

Fraudulent Transactions: 492 (0.172%)

Highly imbalanced dataset

🛠️ Methodology
1. Data Processing

Data cleaning and handling missing values

Feature scaling (important for algorithms like KNN, SVM, Logistic Regression)

Splitting dataset into training and testing sets

2. Algorithms Used

K-Nearest Neighbors (KNN)

Tested with K=3 and K=7

Achieved 100% accuracy with very low misclassification

Logistic Regression (LR)

A probability-based model

Training Accuracy: 93.51%

Testing Accuracy: 91.88%

Support Vector Machine (SVM)

Excellent for high-dimensional data

Accuracy: 97.59%

Decision Tree (DT)

Easy to interpret, handles categorical & numerical data

Accuracy: 100%

3. Model Evaluation

Metrics Used: Accuracy, Confusion Matrix, ROC Curve

Best Performers:

KNN & Decision Tree (100%)

SVM close behind (97.59%)

Logistic Regression performed the lowest (91.88%)
