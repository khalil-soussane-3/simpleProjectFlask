import numpy as np 

class Perceptron:
    def __init__(self,threshold):
        self.threshold = threshold
        
    def predict(self, inputs,weights):
        weighted_sum = np.dot(inputs,weights) 
        if weighted_sum > self.threshold:
            return 1
        else:
            return 0



class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.b1 = np.zeros(self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)
        self.b2 = np.zeros(self.output_size)

    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        y_pred = self.sigmoid(self.z2)
        return y_pred
  
    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def predict(self, X):
        y_pred = self.forward(X)
        return np.argmax(y_pred, axis=1)




class HopfieldNetwork:
    def __init__(self, num_neurons):
        self.num_neurons = num_neurons
        self.weights = np.random.randn(num_neurons, num_neurons)

    def recall(self, pattern, max_iter=100):
        for i in range(max_iter):
            units = np.dot(self.weights, pattern)
            units = np.where(units > 0, 1, -1)
        if np.array_equal(units, pattern):
            return units
        pattern = units
        return units


class Kohonen:
    def __init__(self, n_dim, n_neurons):
        self.n_dim = n_dim
        self.n_neurons = n_neurons
        self.weights = np.random.rand(n_neurons, n_dim)
    def predict(self, X):
        # predict the class labels for a new set of data
        y_pred = []
        for x in X:
            distances = np.linalg.norm(self.weights - x, axis=1)
            winning_neuron = np.argmin(distances)
            y_pred.append(winning_neuron)
        return y_pred
            