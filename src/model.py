import pickle
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import log_loss, make_scorer

from DataPreparation import fc, ffc


df = pd.DataFrame(list(ffc.find()))
df['likes_last_post'].fillna(0, inplace = True)
df_dropped = df.dropna()
df_dropped['is_business_account'] = df_dropped['is_business_account'].astype(int)
df_dropped['is_joined_recently'] = df_dropped['is_joined_recently'].astype(int)
df_dropped['is_private'] = df_dropped['is_private'].astype(int)

X = df_dropped.iloc[:,[2,3,6,7,8,9]]
y = df_dropped.iloc[:, 5]


# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
    



# best model
def fit_best_rf_model(X_train, y_train):
    random_forest_grid = {'max_depth': [3, 4, None],
                        'max_features': ['sqrt', 'log2', None],
                        'min_samples_split': [2, 4],
                        'min_samples_leaf': [1, 2, 4],
                        'bootstrap': [True, False],
                        'n_estimators': [40, 80, 100, 120, 140, 160],
                        'random_state': [359]}

    rf_gridsearch = GridSearchCV(RandomForestClassifier(),
                                random_forest_grid,
                                n_jobs=-1,
                                verbose=True,
                                scoring='neg_log_loss')
    rf_gridsearch.fit(X_train, y_train)

    print("best parameters:", rf_gridsearch.best_params_)

    best_rf_model = rf_gridsearch.best_estimator_

    best_rf_model.fit(X_train, y_train)
    return best_rf_model


best_rf_model = fit_best_rf_model(X_train, y_train)

# save model to pickle
filename = 'finalized_model.sav'
pickle.dump(best_rf_model, open(filename, 'wb'))