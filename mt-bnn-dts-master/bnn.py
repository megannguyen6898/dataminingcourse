import numpy as np

class Network:
    def __init__(self, Network_Layers, Inputs, activation, learn_rate):
        self.Inputs = Inputs 
        self.Network_Layers = Network_Layers #[Input, Hidden, Output]
        self.learn_rate = learn_rate
        for i in range(0, len(self.Network_Layers)-1):
            for x, y in range(zip(len(self.Network_Layers[i]), len(self.Network_Layers[i+1]))):
                self.W[y][x] =  np.zeros(x, y) #matrix - this is a single value in the matrix
                self.B[y] = np.zeros(y)
        self.activation = activation
    def activation_function(self, activation, x):
        if self.activation == "Sigmoid":
            activation_function = 1 / (1+ np.exp(-x))
        elif self.activation == "ReLU":
            activation_function = np.max(0, x)
        return activation_function
    def forward_propagation(self, X):
        inputs = X #input as output of previous layers, used as a list
        for i in range(0, len(self.Network_Layers)-1):
            new_inputs = []
            for x, y in range(zip(len(self.Network_Layers[i]), len(self.Network_Layers[i+1]))):
                self.z[y] = self.W[y][x] * inputs[x] - self.B[y]
                self.output[y] = self.activation_function(self.z[y])
                new_inputs.append(self.output[y])
            inputs = new_inputs
        return inputs
        
    def derived_activation(self, activation, Z):
        if self.activation == "Sigmoid":
            derived_activation = Z * (1 - Z)
        elif self.activation == "Softmax":
            derived_activation = np.exp(Z) / np.sum(np.exp(Z))
        return derived_activation
    def backward_propagation(self, Desired, Input):
        for i in reversed(range(0, len(self.Network_Layers)-1)):
            errors = []
            if i != len(self.Network_Layers[i])-1: #non-output layer
                for ry, rx in range(zip(len(self.Network_Layers[i]), len(self.Network_Layers[i+1]))):
                    error = 0
                    error = error + self.W[rx][ry] * self.output_delta[ry]
                errors.append(error)
            else:
                for ry in range(0, len(self.Network_Layers[i])-1):
                    error = (Desired[ry] - self.output[ry])
                    errors.append(error)
            for ry in range(0, len(self.Network_Layers[i])-1):
                self.output_delta[ry] = errors[ry] * self.derived_activation("Sigmoid", self.output[ry])
        #(self.out * (1 - self.out)) is the derivative of sigmoid fn aka slope of neuron's output value
        #out_delta is the error for each output neuron
      #The error signal for a neuron in the hidden layer is calculated as the weighted error of each neuron in the output layer
        #delta reflects the change the error implies on the neuron (e.g. the weight delta)
    def update_weight(self, inputs):
    #weight is a given weight, learning_rate is a parameter that you must specify, 
    #error is the error calculated by the backpropagation procedure for the neuron 
    #and input is the input value that caused the error
        for i in range(0, len(self.Network_Layers)-1):
            for x, y in range(zip(len(self.Network_Layers[i-1]), len(self.Network_Layers[i]))):
                if i != 0: #non input layer
                    inputs = self.output[x]
                    for j in range(len(inputs)):
                        self.W[y][j] += self.learn_rate * self.output_delta[y] * inputs[j]
                else:
                    self.W[y] += self.learn_rate * self.output_delta[y]
                self.B[y] += -1 * self.learn_rate * self.output_delta[y]
    def decode(self, W):
        w_size_1st_layer = self.Network_Layers[0] * self.Network_Layers[1]
        self.W1 = W[0: w_size_1st_layer]
        W_size_each_layer = []
        B_size_each_layer = []
        for i in range(0, len(self.Network_Layers)-1):
            W_size_ith_layer = self.Network_Layers[i] * self.Network_Layers[i+1] #size of i layer
            B_size_ith_layer = self.Network_Layers[i+1]
            W_size_each_layer.append(W_size_ith_layer)
            B_size_each_layer.append(B_size_ith_layer)
            self.B1 = W[sum(W_size_each_layer):sum(W_size_each_layer)+self.Network_Layers[1]].reshape(1, self.Network_Layers[1])
            for j in enumerate(W_size_each_layer): #enumerate is [count, item]
                W_i1th_th_layer = W[sum(W_size_each_layer[0:j[0]]):sum(W_size_each_layer[0:(j+1)[0]])]
                self.W_i1 = np.reshape(W_i1th_th_layer, (self.Network_Layers[i], self.Network_Layers[i+1]))
            for k in enumerate(B_size_each_layer):    
                B_i1th_th_layer = W[sum(W_size_each_layer)+sum(W_size_each_layer[0:k[0]]):sum(W_size_each_layer)+sum(W_size_each_layer[0:(k+1)[0]])]
                self.B_i1 = np.reshape(B_i1th_th_layer, self.Network_Layers[i+1])
        return W_size_each_layer, B_size_each_layer
    def encode(self, W):
        w1 = self.W1.ravel()
        w1 = w1.reshape(1, w1.shape[0])
        W_size_each_layer = self.decode(W)[0]
        B_size_each_layer = self.decode(W)[1]
        self.B1 = W[sum(W_size_each_layer):sum(W_size_each_layer)+self.Network_Layers[1]].reshape(1, self.Network_Layers[1])
        for i in range(0, len(self.Network_Layers)-1):
            for j in enumerate(W_size_each_layer): #enumerate is [count, item]
                W_i1th_th_layer = W[sum(W_size_each_layer[0:j[0]]):sum(W_size_each_layer[0:(j+1)[0]])]
                self.W_i1 = np.reshape(W_i1th_th_layer, (self.Network_Layers[i], self.Network_Layers[i+1]))
                w_i1 = self.W_i1.ravel()
                w_i1 = w_i1.reshape(1, w_i1.shape[0])
            for k in enumerate(B_size_each_layer):    
                B_i1th_th_layer = W[sum(W_size_each_layer)+sum(W_size_each_layer[0:k[0]]):sum(W_size_each_layer)+sum(W_size_each_layer[0:(k+1)[0]])]
                self.B_i1 = np.reshape(B_i1th_th_layer, (1, self.Network_Layers[i+1]))
        w = np.concatenate([w1.T, w_i1.T, self.B1.T, self.B_i1.T])
        w = w.reshape(-1)
        return w
    def langevin_gradient(self, W, data, depth):
        self.decode(W)  # method to decode w into W1, W2, B1, B2.
        size = data.shape[0] #number of rows

        Inputs = np.zeros((1, self.Network_Layers[0]))  # temp hold input
        Desired = np.zeros((1, self.Network_Layers[-1]))
        fx = np.zeros(size)

        for i in range(0, depth):
            for j in range(0, size):
                pat = j
                Inputs = data[pat, 0:self.Network_Layers[0]]
                Desired = data[pat, self.Network_Layers[0]:]
                self.forward_propagation(Inputs)
                self.backward_propagation(Desired, Inputs)
                self.update_weight(Inputs)
        w_updated = self.encode()

        return  w_updated