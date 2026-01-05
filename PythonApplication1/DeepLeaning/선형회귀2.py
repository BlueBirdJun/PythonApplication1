import torch

y=torch.tensor([10,20,30])
y=y.unsqueeze(1)
y.shape

print(y.shape)