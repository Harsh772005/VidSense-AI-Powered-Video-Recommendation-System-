# import pandas as pd
# import numpy as np
# from sklearn.metrics import mean_absolute_error, mean_squared_error

# # Sample data
# data = [
#     {"username":"bloomscroller","id":1386,"interaction_count":0.2358507097,"user_avg_rating":0.5435992579},
#     {"username":"ankur_raj_","id":1642,"interaction_count":0.0022779043,"user_avg_rating":0.9387755102},
#     {"username":"kinha","id":814,"interaction_count":0.8982278385,"user_avg_rating":0.3099906629},
#     {"username":"kinha","id":1214,"interaction_count":0.9989744277,"user_avg_rating":0.3099906629},
#     {"username":"kinha","id":797,"interaction_count":0.5337579924,"user_avg_rating":0.3099906629},
#     {"username":"afrobeezy","id":59,"interaction_count":1.0705720873,"user_avg_rating":0.180533752},
#     {"username":"kinha","id":148,"interaction_count":1.0847651835,"user_avg_rating":0.3099906629},
#     {"username":"kinha","id":517,"interaction_count":1.1045860433,"user_avg_rating":0.3099906629},
#     {"username":"kinha","id":164,"interaction_count":0.9357187767,"user_avg_rating":0.3099906629},
#     {"username":"kinha","id":773,"interaction_count":1.0019446363,"user_avg_rating":0.3099906629},
#     {"username":"kinha","id":1395,"interaction_count":0.0951463115,"user_avg_rating":0.3099906629}
# ]

# # Convert the data into a pandas DataFrame
# df = pd.DataFrame(data)

# # Predicted interaction counts (simulating predictions for demonstration purposes)
# # Replace these values with your model predictions
# predicted_interaction_count = {
#     1386: 0.23, 1642: 0.01, 814: 0.90, 1214: 0.99, 797: 0.53,
#     59: 1.05, 148: 1.08, 517: 1.11, 164: 0.94, 773: 1.00, 1395: 0.10
# }

# # Actual interaction counts
# actual_interaction_count = df['interaction_count'].values

# # Predicted values from the models
# predicted_values = [predicted_interaction_count.get(video_id, 0) for video_id in df['id']]

# # Calculate MAE (Mean Absolute Error)
# mae = mean_absolute_error(actual_interaction_count, predicted_values)

# # Calculate RMSE (Root Mean Squared Error)
# rmse = np.sqrt(mean_squared_error(actual_interaction_count, predicted_values))

# # Print results
# print(f"Mean Absolute Error (MAE): {mae:.4f}")
# print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")




# import numpy as np
# from sklearn.metrics import mean_absolute_error, mean_squared_error

# # Example Data: Replace these with your actual and predicted values
# actual_values = [4.5, 3.0, 2.5, 5.0, 4.0, 3.5]
# predicted_values = [4.2, 3.1, 2.7, 4.8, 3.9, 3.6]

# # Compute MAE
# mae = mean_absolute_error(actual_values, predicted_values)

# # Compute RMSE
# rmse = np.sqrt(mean_squared_error(actual_values, predicted_values))

# # Print results
# print(f"Mean Absolute Error (MAE): {mae:.4f}")
# print(f"Root Mean Square Error (RMSE): {rmse:.4f}")



import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Simulated data for example purposes
# Input = 1386, Predicted Recommendations = [1694, 1396, 1374, 1380, 1372]
# Actual interaction counts or ratings for recommended items
actual_interactions_1386 = [0.206, 0.138, 0.300, 0.250, 0.220]
predicted_interactions_1386 = [0.210, 0.140, 0.310, 0.240, 0.230]

# Repeat for other users
actual_interactions_1642 = [0.002, 0.050, 0.000, 0.000, 0.005]
predicted_interactions_1642 = [0.010, 0.040, 0.010, 0.005, 0.006]

actual_interactions_814 = [0.456, 0.010, 0.320, 0.450, 0.774]
predicted_interactions_814 = [0.460, 0.015, 0.300, 0.440, 0.780]

actual_interactions_1214 = [0.016, 0.120, 0.773, 0.702, 0.590]
predicted_interactions_1214 = [0.020, 0.130, 0.770, 0.710, 0.600]

# Combine actual and predicted interactions
actual_values = (
    actual_interactions_1386 + 
    actual_interactions_1642 + 
    actual_interactions_814 + 
    actual_interactions_1214
)
predicted_values = (
    predicted_interactions_1386 + 
    predicted_interactions_1642 + 
    predicted_interactions_814 + 
    predicted_interactions_1214
)

# Calculate MAE and RMSE
mae = mean_absolute_error(actual_values, predicted_values)
rmse = np.sqrt(mean_squared_error(actual_values, predicted_values))

print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Square Error (RMSE): {rmse:.4f}")
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Simulated data for example purposes
# Input = 1386, Predicted Recommendations = [1694, 1396, 1374, 1380, 1372]
# Actual interaction counts or ratings for recommended items
actual_interactions_1386 = [0.206, 0.138, 0.300, 0.250, 0.220]
predicted_interactions_1386 = [0.210, 0.140, 0.310, 0.240, 0.230]

# Repeat for other users
actual_interactions_1642 = [0.002, 0.050, 0.000, 0.000, 0.005]
predicted_interactions_1642 = [0.010, 0.040, 0.010, 0.005, 0.006]

actual_interactions_814 = [0.456, 0.010, 0.320, 0.450, 0.774]
predicted_interactions_814 = [0.460, 0.015, 0.300, 0.440, 0.780]

actual_interactions_1214 = [0.016, 0.120, 0.773, 0.702, 0.590]
predicted_interactions_1214 = [0.020, 0.130, 0.770, 0.710, 0.600]

# Combine actual and predicted interactions
actual_values = (
    actual_interactions_1386 + 
    actual_interactions_1642 + 
    actual_interactions_814 + 
    actual_interactions_1214
)
predicted_values = (
    predicted_interactions_1386 + 
    predicted_interactions_1642 + 
    predicted_interactions_814 + 
    predicted_interactions_1214
)

# Calculate MAE and RMSE
mae = mean_absolute_error(actual_values, predicted_values)
rmse = np.sqrt(mean_squared_error(actual_values, predicted_values))

print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Square Error (RMSE): {rmse:.4f}")
