# model_training.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
import eli5
from eli5.sklearn import PermutationImportance
from sklearn.preprocessing import MinMaxScaler
from matplotlib.colors import LinearSegmentedColormap

data = pd.read_csv("../data/customer_data.csv").set_index('customerID')
df = data.copy()

def datapreparation(df=df):
    df.TotalCharges = df.TotalCharges.replace(" ", np.nan)
    df.TotalCharges.fillna(0, inplace=True)
    df.TotalCharges = df.TotalCharges.astype(float)
    cols1 = ['Partner', 'Dependents', 'PaperlessBilling', 'Churn', 'PhoneService']
    for col in cols1:
        df[col] = df[col].apply(lambda x: 0 if x == "No" else 1)
    df.gender = df.gender.apply(lambda x: 0 if x == "Male" else 1)
    df.MultipleLines = df.MultipleLines.map({'No phone service': 0, 'No': 0, 'Yes': 1})
    cols2 = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    for col in cols2:
        df[col] = df[col].map({'No internet service': 0, 'No': 0, 'Yes': 1})
    df = pd.get_dummies(df, columns=['InternetService', 'Contract', 'PaymentMethod'], drop_first=True)
    return df

df = datapreparation()

def split_data():
    columns = df.columns
    X = df.drop(columns=["Churn"])
    Y = df["Churn"]
    return train_test_split(X, Y, test_size=0.2, random_state=100, stratify=df.Churn)

pipeline = Pipeline([
    ('scaler', MinMaxScaler()),
    ('knn', KNeighborsClassifier())
])

def grid_searchCV(pipeline, x_train, y_train):
    param_grid = {
        'knn__n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 75], 
        'knn__weights': ['uniform', 'distance'],                    
        'knn__metric': ['euclidean', 'manhattan', 'hamming']                   
    }
    grid_search = GridSearchCV(estimator=pipeline, 
                               param_grid=param_grid, 
                               cv=5, 
                               verbose=1, 
                               n_jobs=-1)
    grid_search.fit(x_train, y_train)
    return grid_search.best_estimator_

def accuracy(model, x_predict, y_test):
    accuracy = model.score(x_predict, y_test)
    print(f"{model} accuracy is: {accuracy}")

x_train, x_test, y_train, y_test = split_data()
model = grid_searchCV(pipeline, x_train, y_train) 

perm = PermutationImportance(model, random_state=1).fit(x_test, y_test)
eli5.show_weights(perm, feature_names=x_test.columns.tolist())

y_predict = model.predict(x_test)
print(f"accuracy score is:{accuracy_score(y_test, y_test)}")

cm = confusion_matrix(y_test, y_predict)
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
my_cmap = LinearSegmentedColormap.from_list("custom_pals", colors, N=256)
sns.heatmap(cm, cmap=my_cmap)
plt.title("Confusion matrix")
plt.show()

report_dictionary = classification_report(y_test, y_predict, output_dict=True)
print(pd.DataFrame(report_dictionary).transpose())