import numpy as np
# Corrected step function (used 'i' incorrectly)
def step_function(x):
    return 1 if x >= 0 else 0
class Perception:  # Fixed spelling from 'perception' to 'Perceptron'
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.zeros(input_size)
        self.bias = 0
        self.lr = learning_rate
    def predict(self, x):  # Added missing colon
        summation = np.dot(x, self.weights) + self.bias
        return step_function(summation)
    def train(self, x, y, epochs=20):
        for epoch in range(epochs):
            print("\nEpoch:", (epoch + 1))
            for i in range(len(x)):
                y_pred = self.predict(x[i])
                error = y[i] - y_pred
                self.weights += self.lr * error * x[i]  # Fixed: use += to update weights
                self.bias += self.lr * error
                print(f"input: {x[i]}, predicted: {y_pred}, error: {error}, weights: {self.weights}, bias: {self.bias}")
# Input and Output
x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # Fixed: remove extra brackets, should be 1D array for indexing
# Instantiate and train
p = Perception(input_size=2)
p.train(x, y)
# Final predictions
print("\nFinal predictions:")
for i in range(len(x)):
    print(f"Input: {x[i]}, Predicted: {p.predict(x[i])}")
