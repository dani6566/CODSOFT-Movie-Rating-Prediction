#Random forest Regression
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

def train_model(X_train,y_train):
    rf_model = RandomForestRegressor(random_state=42)
    rf_model.fit(X_train,y_train)
    return rf_model


def feature_important(rf_model,X):
    # Assuming rf_model is the trained RandomForestRegressor
    feature_importances = pd.Series(rf_model.feature_importances_, index=X.columns)
    feature_importances.sort_values(ascending=True).plot(kind='barh', figsize=(10, 6), color='skyblue')
    plt.title('Feature Importance')
    plt.xlabel('Importance')
    plt.ylabel('Feature')
    plt.show()


def prediction(rf_model , X_test):
    #predictions
    y_pred = rf_model.predict(X_test)
    return y_pred