import torch
import torch.nn as nn
import torch.optim as optim

class Classifier(nn.Module):
    def __init__(self):
        super(Classifier, self).__init__()
        self.fc = nn.Linear(784, 10)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = x.view(-1, 784)
        x = self.fc(x)
        x = self.softmax(x)
        return x

def train():
    # Training code goes here
    pass

def predict():
    # Prediction code goes here
    pass

