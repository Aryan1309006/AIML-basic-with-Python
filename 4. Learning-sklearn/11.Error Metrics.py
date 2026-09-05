# Import error metrics
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    root_mean_squared_error
)

# ---------------- Actual Values ----------------
real_scores = [90, 60, 80, 100]

# ---------------- Predicted Values ----------------
model_guesses = [85, 70, 70, 95]

# ---------------- MAE ----------------
# Mean Absolute Error
# Finds average absolute difference

mae = mean_absolute_error(real_scores, model_guesses)

# ---------------- MSE ----------------
# Mean Squared Error
# Squares mistakes to punish large errors

mse = mean_squared_error(real_scores, model_guesses)

# ---------------- RMSE ----------------
# Root Mean Squared Error
# Gives error in original unit

rmse = root_mean_squared_error(real_scores, model_guesses)

# Display results
print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)


"""
---------------- Error Metrics ----------------

1. MAE (Mean Absolute Error)
   - Simple average error
   - Uses absolute values

2. MSE (Mean Squared Error)
   - Squares errors
   - Large mistakes get higher penalty

3. RMSE (Root Mean Squared Error)
   - Square root of MSE
   - Gives real-world error value

"""