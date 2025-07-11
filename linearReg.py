import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'hrs_studied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'final_score': [30, 35, 40, 50, 65, 70, 75, 80, 85, 95],
}

df = pd.DataFrame(data)

# Features and label
x = df[['hrs_studied']]
y = df[['final_score']]

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

# Train model
model = LinearRegression()
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Evaluation
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('R2 Score:', r2_score(y_test, y_pred))

# Predict for new input
new_hours = pd.DataFrame([[7.5]], columns=['hrs_studied'])  # ✅ fixed column name
prediction = model.predict(new_hours)  # ✅ correct variable name
print('Predicted Score for 7.5 hours:', prediction[0][0])
