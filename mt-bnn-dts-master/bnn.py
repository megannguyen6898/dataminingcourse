import numpy as np

class Network:
    def __init__(self, Inputs, activation):
        self.Inputs = Inputs
        self.Network_Layers = self.Network_Layers #[Input, Hidden, Output]
        for i in range(0, len(self.Network_Layers)-1):
            for x, y in range(zip(self.Network_Layers[i], self.Network_Layers[i+1])):
                self.W[x, y] =  np.zeros(self.Network_Layers[i], self.Network_Layers[i+1])
                self.B[y] = np.zeros(self.Network_Layers[i+1])
        self.activation = activation
    def activation_function(self, activation, X):
        if self.activation == "Sigmoid":
            activation_function = 1 / (1+ np.exp(-X))
        elif self.activation == "ReLU":
            activation_function = np.max(0, X)
        return activation_function
    def forward_propagation(self, X):
        inputs = X #input as output of previous layers
        for i in range(0, len(self.Network_Layers)-1):
            new_inputs = []
            for x, y in range(zip(self.Network_Layers[i-1], self.Network_Layers[i])):
                z = self.W[x, y].dot(inputs) - self.B[y]
                self.output[y] = self.activation_function(z)
                new_inputs.append(self.output[y])
            inputs = new_inputs
        return inputs
        
    def derived_activation(self, activation, Z):
        if self.activation == "Sigmoid":
            derived_activation = Z * (1 - Z)
        elif self.activation == "ReLU":
            if Z < 0:
                derived_activation = 0
            elif Z >0:
                derived_activation = 1
        return derived_activation
    def backward_propagation(self, Network_Layers, Desired, Input):
        for i in reversed(range(len(Network_Layers))):
            for x, y in range(zip(self.Network_Layers[i-1], self.Network_Layers[i])):
                if i == len(Network_Layers)-1: #output layer
                    output_delta = (Desired - self.output[y]) * self.derived_activation("Sigmoid", self.output[y])
                else:
        #(self.out * (1 - self.out)) is the derivative of sigmoid fn aka slope of neuron's output value
        #out_delta is the error for each output neuron
                    hidden_delta = np.zeros(self.Network_Layers[i-1])
        #The error signal for a neuron in the hidden layer is calculated as the weighted error of each neuron in the output layer
                    hidden_delta = output_delta[y].dot(self.W[x, y]) * self.derived_activation("Sigmoid", self.output[y])
        #delta reflects the change the error implies on the neuron (e.g. the weight delta)
    def update_weight(self, Network_Layers, inputs, learn_rate):
        for i in range(len(Network_Layers)):
            for x, y in range(zip(self.Network_Layers[i-1], self.Network_Layers[i])):
                if i != 0:
                    inputs = self.output[x]
                    for j in range(len(inputs)):
                        self.W[j, y] += self.lrate * self.output_delta[y] * inputs[j]
                    self.W[-1] += learn_rate * self.output_delta[y]
