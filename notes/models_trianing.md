# steps
1. splitting the data
2. train the model
3. Tuning parameters
4. cross validation
---
# Evaluate the Predictions
Now you compare your predictions (y_pred) with the actual true labels you held back (y_test). This is where the evaluation metrics come in.
Your Typical Order of Evaluation:
(a) accuracy_score(y_test, y_pred): Start here for a quick, high-level sense of performance. But remember its weakness with imbalanced data.
(b) confusion_matrix(y_test, y_pred): Use this next to see the raw numbers of your model's successes and failures (True Positives, False Positives, etc.). It provides deep insight.
(c) classification_report(y_test, y_pred): This is your primary summary tool. It gives you the precision, recall, and f1-score for each class, all in one neat report. This is often the most valuable printout for understanding overall performance.
(d) roc_auc_score(y_test, y_pred_proba): Use this to get a single, robust score that measures how well your model separates the classes, regardless of the classification threshold. Note: You must use the predicted probabilities (y_pred_proba), not the final predictions (y_pred).