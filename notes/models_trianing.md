# steps
1. splitting the data
2. train the model
3. Tuning parameters
4. cross validation
---
# data preparation for training

### Splitting data
- We've seen that the dataset has imbalanced classes thus we need to keep the same initial distribution in the training and testing dataset. Solution: set the *stratify* parameter to the target column.
- Random state: since the random state must be a fixed just so that the train and test sets will be the same every time we try to split the data. I will set it to a random but **fixed** integer. 

### Training the model
- The weights are uniform because from the exploration, we found that there are some columns inversely related to churning but so important nevertheless.
- the metric is haming because ewe are dealing with categorical and boolean data mostly

- the data columns distributions is not normally shaped so we will use the MinMaxScaler

### Classification report: 
The model is doing good when the case is "NO" churning; 85% precision and 86% recall
But when there client is churning, the precision goes down to 60% and the recall to 56%

---
<br>
So overall knn does not suit this problem the best. We need to try and find a better model.