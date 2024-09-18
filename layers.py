import torch

class Dense:
    
    def __init__(self, input_size, output_size):
        self.weights = torch.randn(input_size,output_size, requires_grad=True) # creates inoput x output sized matrix of weights with ranodm numbers
        self.biases = torch.zeros(output_size, requires_grad=True) # creates output sized vector for biases initally 0
    
    def forward(self, input): # moves to next layer
        return torch.matmul(input,self.weights) + self.biases
