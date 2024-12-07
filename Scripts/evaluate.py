import numpy as np
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


# Evaluation metrics
def evaluation(y_test,y_pred):
    print("Mean Absolute Error (MAE):", mean_absolute_error(y_test, y_pred))
    print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error (RMSE):", np.sqrt(mean_squared_error(y_test, y_pred)))
    print("R-squared (R2):", r2_score(y_test, y_pred))

 
def display_predictions(X_test,y_pred):
        """Display predictions for test samples."""
        for i in range(5):
            print(f"X test: {X_test.iloc[i].to_dict()} | Predicted: {y_pred[i]}")