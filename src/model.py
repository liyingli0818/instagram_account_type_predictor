import pandas as pd
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt
from scipy.special import comb

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import log_loss, make_scorer
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV




# train test split
data = pd.read_csv('../data_cleaned.csv')
X = data.iloc[:, [3,5,6,7,8,10,11]]
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
    

# logistic regression
def fit(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

def predict_proba(X_test, X, y, model):
    y_pred = model.predict_proba(X_test)
    cv_logloss = -cross_val_score(model, X, y, scoring = 'neg_log_loss', cv = 10).mean()
    return y_pred, cv_logloss


# random forest
def fit(X_train, y_train):
    rf = RandomForestClassifier(n_estimators=100,
                            n_jobs=-1,
                            random_state=1)
    rf.fit(X_train, y_train)
   
def predict_proba(X_test, X, y, model):
    y_pred = rf.predict_proba(X_test)[:, 1]
    cv_logloss_rf1 = -cross_val_score(rf, X_train, y_train, cv = 10, scoring = 'neg_log_loss').mean()
    return y_pred, cv_logloss_rf1



# best model
random_forest_best

random_forest_grid = {'max_depth': [3, 4, None],
                      'max_features': ['sqrt', 'log2', None],
                      'min_samples_split': [2, 4],
                      'min_samples_leaf': [1, 2, 4],
                      'bootstrap': [True, False],
                      'n_estimators': [20, 40, 80, 100],
                      'random_state': [359]}

rf_gridsearch = GridSearchCV(RandomForestClassifier(),
                             random_forest_grid,
                             n_jobs=-1,
                             verbose=True,
                             scoring='neg_log_loss')
rf_gridsearch.fit(X_train, y_train)

print("best parameters:", rf_gridsearch.best_params_)
best_rf_model = rf_gridsearch.best_estimator_

#gradient descent

