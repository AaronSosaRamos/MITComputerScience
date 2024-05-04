# -*- coding: utf-8 -*-
"""CM003 - Chapter 7 - Chaining.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1T_MRjcKTD34lMoZ4MDEMlJe6mj_Spf3w

#Chaining

#Stacking Models
"""

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import StackingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Load the California Housing dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define base models
base_models = [
    ('rf', RandomForestRegressor(n_estimators=10, random_state=42)),
    ('gb', GradientBoostingRegressor(n_estimators=10, random_state=42))
]

# Initialize the stacking regressor with a linear regression meta-model
stacking_regressor = StackingRegressor(estimators=base_models, final_estimator=LinearRegression())

# Train the stacking regressor
stacking_regressor.fit(X_train, y_train)

# Make predictions
y_pred_stacking = stacking_regressor.predict(X_test)

# Evaluate the model
mse_stacking = mean_squared_error(y_test, y_pred_stacking)
print(f"Stacking Regressor MSE: {mse_stacking}")

"""#Ensembling models"""

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
from sklearn.metrics import mean_squared_error

# Load the California Housing dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize base models
model_rf = RandomForestRegressor(n_estimators=10, random_state=42)
model_gb = GradientBoostingRegressor(n_estimators=10, random_state=42)

# Create a voting regressor
voting_regressor = VotingRegressor([('rf', model_rf), ('gb', model_gb)])

# Train the voting regressor
voting_regressor.fit(X_train, y_train)

# Make predictions
y_pred_voting = voting_regressor.predict(X_test)

# Evaluate the model
mse_voting = mean_squared_error(y_test, y_pred_voting)
print(f"Voting Regressor MSE: {mse_voting}")

"""#Combining models in a Pipeline"""

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# Load the California Housing dataset
data = fetch_california_housing()
X, y = data.data, data.target

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline with preprocessing and modeling steps
pipeline = Pipeline([
    ('scaler', StandardScaler()),  # Standardize features
    ('rf', RandomForestRegressor(n_estimators=10, random_state=42))  # Random Forest Regressor
])

# Train the pipeline (preprocessing + modeling)
pipeline.fit(X_train, y_train)

# Make predictions
y_pred_pipeline = pipeline.predict(X_test)

# Evaluate the pipeline
mse_pipeline = mean_squared_error(y_test, y_pred_pipeline)
print(f"Pipeline MSE: {mse_pipeline}")

"""#Oracle Inequalities in Empirical Risk Minimization (ERM)"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate synthetic data
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + np.random.randn(100)  # True relationship: y = 3*X + noise

# Define a linear regression model
model = LinearRegression()

# Fit the model (empirical risk minimization)
model.fit(X, y)

# Compute empirical risk (mean squared error)
y_pred = model.predict(X)
empirical_risk = mean_squared_error(y, y_pred)
print("Empirical Risk (MSE):", empirical_risk)

"""#Sparse Recovery"""

import cvxpy as cp

# Generate synthetic data for sparse recovery
np.random.seed(1)
n = 100
m = 50
A = np.random.randn(m, n)  # Measurement matrix
x_true = np.zeros(n)
x_true[:5] = np.random.randn(5)  # True sparse signal
y = A @ x_true + 0.1 * np.random.randn(m)  # Noisy measurements

# Solve the L1-regularized least squares problem (Lasso)
x = cp.Variable(n)
objective = cp.Minimize(cp.norm(A @ x - y, 2) + cp.norm(x, 1))
problem = cp.Problem(objective)

# Solve the problem
problem.solve()

# Recovered sparse solution
x_hat = x.value

# Print the recovered sparse solution
print("Recovered Sparse Solution:", x_hat)

"""#Probability in a Banach Space (Finite-Dimensional Case)"""

import numpy as np
from scipy.stats import multivariate_normal

# Define parameters
n = 3  # Dimension of the Banach space (e.g., Euclidean space R^n)
mean = np.zeros(n)  # Mean vector
covariance_matrix = np.eye(n)  # Identity covariance matrix (for simplicity)

# Generate random vectors from a multivariate normal distribution
num_samples = 1000
random_vectors = multivariate_normal.rvs(mean=mean, cov=covariance_matrix, size=num_samples)

# Compute sample mean and sample covariance
sample_mean = np.mean(random_vectors, axis=0)
sample_covariance = np.cov(random_vectors, rowvar=False)

# Print results
print("Sample Mean:")
print(sample_mean)
print("\nSample Covariance Matrix:")
print(sample_covariance)