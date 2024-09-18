from .layers import *
class Model:
    def __init__(self):
        self.layers = []

    def __init__(self, inital_layers): # creates a neural network with format [[in_size1,out_size1],[in_size2,out_size2],...,[in_sizeN,out_sizeN]
        Model()
        for layer in inital_layers:
            self.layers.append(Dense(layer[0],layer[1]))

    def add_layer(self, layer):
        self.layers.append(layer)
        
    def forward(self,inputs):
        for layer in self.layers:
            input = layer.forward(input)
        return input

