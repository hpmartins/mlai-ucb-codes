# Practical Application 3: Comparing Classifiers

This is a comparison of the performance of different classifiers using a dataset from a Portuguese marketing  campaign related with bank deposit subscription. The data is available [here](https://archive.ics.uci.edu/dataset/222/bank+marketing) at the [UCI Machine Learning Repository](https://archive.ics.uci.edu/).

All code is in [this notebook](https://github.com/hpmartins/mlai-ucb-codes/blob/main/practical_applications/module_17/module_17_application.ipynb) in this repository.

## Findings

I have used Logistic Regression, KNN, Decision Tree, and SVM to try to model the marketing dataset. My main evaluation metric was recall due to the imbalanced target column and also to try to get a better prediction for positive outcomes (client subscribing to a term deposit). In all models, when available, I used the balanced class weight since only around 12% of the outcomes are positive.

The Logistic Regression model achieved moderate recall scores of approximately 0.646 on both training and test data, though it had low precision scores around 0.20, indicating a high number of false positives. Its accuracy was around 0.68 for both training and test sets. This suggests that while Logistic Regression was somewhat effective at identifying positive cases, it often misclassified negative cases as positive.

In contrast, the K-Nearest Neighbors (KNN) classifier showed high accuracy scores above 0.95 on both datasets and recall scores of approximately 0.75, but precision was around 0.85, which indicates a better balance between false positives and true positives compared to Logistic Regression. The Decision Tree classifier had lower accuracy (around 0.44) but high recall scores above 0.84, making it very sensitive in identifying positive cases, though with lower precision (~0.15), leading to many false positives. The SVM performed similarly to the Decision Tree with accuracy around 0.48 and recall around 0.82, maintaining consistent performance even with a smaller subset of the data. These results suggest that while KNN provided a good balance, the Decision Tree and SVM were highly effective in maximizing recall at the expense of precision and overall accuracy.