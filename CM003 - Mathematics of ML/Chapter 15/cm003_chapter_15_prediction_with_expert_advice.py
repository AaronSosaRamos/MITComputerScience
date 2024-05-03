# -*- coding: utf-8 -*-
"""CM003 - Chapter 15 - Prediction with Expert Advice.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MzfZIUvCMpsiaxzGI5ymnALRh-UEJXFL

#Prediction with Expert Advice

#Online Learning
"""

import numpy as np
from sklearn.linear_model import SGDClassifier

# Define online learning parameters
num_features = 20
batch_size = 100
num_batches = 50  # Number of batches to simulate
evaluation_interval = 10  # Evaluate model performance every 'evaluation_interval' batches

# Initialize an SGDClassifier for binary classification
model = SGDClassifier(loss='log_loss', max_iter=1000, tol=1e-3)

# Simulate streaming data generator for a fixed number of batches
def generate_data_batches(num_batches, batch_size):
    for _ in range(num_batches):
        X_batch = np.random.rand(batch_size, num_features)
        y_batch = np.random.randint(0, 2, size=batch_size)  # Binary labels
        yield X_batch, y_batch

# Online learning loop
data_batches = generate_data_batches(num_batches, batch_size)

for i, (X_batch, y_batch) in enumerate(data_batches, 1):
    # Perform online learning on the current batch
    model.partial_fit(X_batch, y_batch, classes=np.unique(y_batch))

    # Evaluate model performance periodically
    if i % evaluation_interval == 0:
        # Simulate a validation set for evaluation
        X_validation = np.random.rand(batch_size, num_features)
        y_validation = np.random.randint(0, 2, size=batch_size)

        # Calculate validation accuracy
        accuracy = model.score(X_validation, y_validation)
        print(f"Batch {i}/{num_batches}, Validation Accuracy: {accuracy:.4f}")

print("Online learning process completed.")

"""#Online Shortest Path:"""

import networkx as nx
from heapq import heappush, heappop
from itertools import count
class OnlineShortestPath:
    def __init__(self):
        self.graph = nx.Graph()
        self.node_counter = count()  # Counter for unique node ids

    def add_edge(self, u, v, weight):
        # Add an edge to the graph
        if not self.graph.has_node(u):
            self.graph.add_node(u)
        if not self.graph.has_node(v):
            self.graph.add_node(v)
        self.graph.add_edge(u, v, weight=weight)

    def update_shortest_path(self, source, target):
        # Compute shortest path using Dijkstra's algorithm
        shortest_path = nx.shortest_path(self.graph, source=source, target=target, weight='weight')
        shortest_distance = nx.shortest_path_length(self.graph, source=source, target=target, weight='weight')
        return shortest_path, shortest_distance
# Create an instance of OnlineShortestPath
osp = OnlineShortestPath()

# Example: Add edges to the graph
osp.add_edge('A', 'B', 5)
osp.add_edge('B', 'C', 3)
osp.add_edge('C', 'D', 7)
osp.add_edge('D', 'A', 2)

# Update shortest path after adding edges
source_node = 'A'
target_node = 'D'
shortest_path, shortest_distance = osp.update_shortest_path(source_node, target_node)

print(f"Shortest Path from {source_node} to {target_node}: {shortest_path}")
print(f"Shortest Distance: {shortest_distance}")

"""#Dynamic Pricing"""

import random

class DynamicPricing:
    def __init__(self, initial_price):
        self.price = initial_price
        self.min_price = 10  # Minimum price
        self.max_price = 100  # Maximum price

    def update_price(self, demand_level):
        # Adjust price based on demand level
        if demand_level > 0.8:
            # High demand: Increase price
            self.price = min(self.price * 1.2, self.max_price)
        elif demand_level > 0.5:
            # Moderate demand: Keep price unchanged
            self.price = self.price
        else:
            # Low demand: Decrease price
            self.price = max(self.price * 0.8, self.min_price)

    def get_current_price(self):
        return self.price
def simulate_demand():
    # Simulate random demand level between 0 and 1
    return random.uniform(0, 1)
# Initialize DynamicPricing with an initial price
initial_price = 50
pricing_strategy = DynamicPricing(initial_price)

# Simulate dynamic pricing over time
num_iterations = 10

for i in range(num_iterations):
    demand_level = simulate_demand()
    pricing_strategy.update_price(demand_level)
    current_price = pricing_strategy.get_current_price()
    print(f"Iteration {i+1}: Demand Level = {demand_level:.2f}, Current Price = ${current_price:.2f}")

"""#Sequential Investment"""

import numpy as np

class SequentialInvestment:
    def __init__(self, num_assets):
        self.num_assets = num_assets
        self.total_investment = 0
        self.portfolio_value = 0

    def make_investment(self, investment_amounts):
        # Validate number of assets to invest in
        if len(investment_amounts) != self.num_assets:
            raise ValueError("Number of investment amounts must match the number of assets")

        # Simulate returns for each asset
        returns = np.random.uniform(low=0.8, high=1.2, size=self.num_assets)

        # Calculate portfolio value after investments
        self.portfolio_value = sum(investment_amounts * returns)

        # Update total investment
        self.total_investment += sum(investment_amounts)

    def get_portfolio_value(self):
        return self.portfolio_value

    def get_total_investment(self):
        return self.total_investment
# Initialize SequentialInvestment with the number of assets
num_assets = 3
investment_strategy = SequentialInvestment(num_assets)

# Simulate sequential investments over time
num_rounds = 5
initial_investment_amounts = np.array([1000, 2000, 1500])  # Initial investment amounts for each asset

print("Initial Investment Allocation:")
print(f"Asset 1: ${initial_investment_amounts[0]}")
print(f"Asset 2: ${initial_investment_amounts[1]}")
print(f"Asset 3: ${initial_investment_amounts[2]}")

for round in range(1, num_rounds + 1):
    print(f"\n--- Round {round} ---")

    # Simulate making investment decisions
    investment_strategy.make_investment(initial_investment_amounts)

    # Display results after each round
    portfolio_value = investment_strategy.get_portfolio_value()
    total_investment = investment_strategy.get_total_investment()

    print(f"Portfolio Value after Round {round}: ${portfolio_value:.2f}")
    print(f"Total Investment after Round {round}: ${total_investment:.2f}")

    # Update investment amounts for next round (randomize for simplicity)
    initial_investment_amounts = np.random.randint(500, 3000, size=num_assets)
    print(f"New Investment Allocation for Next Round:")
    print(f"Asset 1: ${initial_investment_amounts[0]}")
    print(f"Asset 2: ${initial_investment_amounts[1]}")
    print(f"Asset 3: ${initial_investment_amounts[2]}")

"""#PREDICTION WITH EXPERT ADVICE

#Cumulative Regret
"""

import numpy as np

class PredictionWithExpertAdvice:
    def __init__(self, num_experts):
        self.num_experts = num_experts
        self.weights = np.ones(num_experts)  # Initialize weights for experts
        self.predictions = []
        self.cumulative_regret = 0

    def predict(self):
        # Make prediction based on current expert weights (weighted majority vote)
        prediction = np.random.choice(self.num_experts, p=self.weights / np.sum(self.weights))
        self.predictions.append(prediction)
        return prediction

    def update_weights(self, expert_losses):
        # Update expert weights based on expert losses
        for i in range(self.num_experts):
            self.weights[i] *= np.exp(-expert_losses[i])

        # Normalize weights to ensure they sum up to 1 (for probability distribution)
        self.weights /= np.sum(self.weights)

    def calculate_regret(self, expert_losses):
        # Calculate cumulative regret based on expert losses
        best_expert_loss = min(expert_losses)
        algorithm_loss = sum(self.weights[i] * expert_losses[i] for i in range(self.num_experts))
        self.cumulative_regret += algorithm_loss - best_expert_loss

    def get_cumulative_regret(self):
        return self.cumulative_regret
# Initialize PredictionWithExpertAdvice with the number of experts
num_experts = 3
prediction_algorithm = PredictionWithExpertAdvice(num_experts)

# Simulate prediction with expert advice over time (multiple rounds)
num_rounds = 10
expert_losses = np.random.uniform(low=0, high=1, size=(num_experts,))  # Simulate random expert losses

for round in range(1, num_rounds + 1):
    print(f"\n--- Round {round} ---")

    # Make prediction using the algorithm
    algorithm_prediction = prediction_algorithm.predict()

    # Get expert loss for each expert
    expert_losses = np.random.uniform(low=0, high=1, size=(num_experts,))

    # Update weights based on expert losses
    prediction_algorithm.update_weights(expert_losses)

    # Calculate cumulative regret
    prediction_algorithm.calculate_regret(expert_losses)

    # Display cumulative regret after each round
    cumulative_regret = prediction_algorithm.get_cumulative_regret()
    print(f"Cumulative Regret after Round {round}: {cumulative_regret:.4f}")

print(f"\nTotal Cumulative Regret: {prediction_algorithm.get_cumulative_regret():.4f}")

"""#Exponential Weights"""

import numpy as np

class ExponentialWeights:
    def __init__(self, num_actions, learning_rate):
        self.num_actions = num_actions
        self.weights = np.ones(num_actions)  # Initialize weights for actions
        self.learning_rate = learning_rate

    def choose_action(self):
        # Make a weighted random choice of actions based on current weights
        action = np.random.choice(self.num_actions, p=self.weights / np.sum(self.weights))
        return action

    def update_weights(self, action, loss):
        # Update weights using exponential weighting rule
        update_factor = np.exp(-self.learning_rate * loss)
        self.weights[action] *= update_factor

        # Normalize weights to ensure they sum up to 1 (for probability distribution)
        self.weights /= np.sum(self.weights)
# Initialize ExponentialWeights with the number of actions and learning rate
num_actions = 3
learning_rate = 0.1
exp_weights_algorithm = ExponentialWeights(num_actions, learning_rate)

# Simulate the algorithm over time (multiple rounds)
num_rounds = 10

for round in range(1, num_rounds + 1):
    print(f"\n--- Round {round} ---")

    # Choose an action based on the current weights
    chosen_action = exp_weights_algorithm.choose_action()

    # Simulate loss for the chosen action (random for simplicity)
    action_loss = np.random.uniform(0, 1)

    # Update weights based on the action and loss
    exp_weights_algorithm.update_weights(chosen_action, action_loss)

    # Display current weights after each round
    print(f"Current Weights after Round {round}: {exp_weights_algorithm.weights}")

print("\nFinal Weights:")
print(exp_weights_algorithm.weights)