# Regular EDA (Exploratory Data Analysis) and plotting libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Models from Scikit-Learn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB

# Model Evaluations
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import plot_roc_curve

df = pd.read_csv("dataset.csv")
# df.shape

X = df.drop("Disease", axis = 1)
y = df["Disease"]

cat_columns = X.select_dtypes(['object']).columns
X[cat_columns] = X[cat_columns].apply(lambda x: pd.factorize(x)[0])
# X.head(15)

result = pd.concat([y,X], axis =1, join='inner')
# result.head(5)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)

clf.predict(X_test) 

pickle.dump(clf, open("disease_predictor.pkl", 'wb'))
