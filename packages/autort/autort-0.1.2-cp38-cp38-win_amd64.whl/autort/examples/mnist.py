#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR

def parse_args():
    parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
    parser.add_argument('--batch-size', type=int, default=64, metavar='N',
                        help='input batch size for training (default: 64)')
    parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
                        help='input batch size for testing (default: 1000)')
    parser.add_argument('--epochs', type=int, default=14, metavar='N',
                        help='number of epochs to train (default: 14)')
    parser.add_argument('--lr', type=float, default=1.0, metavar='LR',
                        help='learning rate (default: 1.0)')
    parser.add_argument('--gamma', type=float, default=0.7, metavar='M',
                        help='Learning rate step gamma (default: 0.7)')
    parser.add_argument('--dry-run', action='store_true', default=False,
                        help='quickly check a single pass')
    parser.add_argument('--seed', type=int, default=1, metavar='S',
                        help='random seed (default: 1)')
    parser.add_argument('--log-interval', type=int, default=10, metavar='N',
                        help='how many batches to wait before logging training status')
    parser.add_argument('--save-model', action='store_true', default=False,
                        help='For Saving the current Model')
    parser.add_argument('--train', action='store_true', default=False,
                        help='run in train mode instead of inference')
    parser.add_argument('--use_cuda', action='store_true', default=False,
                        help='enable CUDA training instead of DirectX')
    parser.add_argument('--use_cpu', action='store_true', default=False,
                        help='enable CPU training instead of DirectX')
    return parser.parse_args()

args = parse_args()

if args.use_cuda:
  device = torch.device("cuda")
elif args.use_cpu:
  device = torch.device("cpu")
else:
  import autort
  device = autort.device()


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 512)
        self.fc2 = nn.Linear(512, 512)
        self.fc3 = nn.Linear(512, 10)

    def forward(self, x):
        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)
        x = F.relu(x)
        x = self.fc3(x)
        output = F.log_softmax(x, dim=1)
        return output

torch.manual_seed(args.seed)

x = torch.ones([5, 28 * 28], device=device)
y = torch.ones([x.size(0)], dtype=torch.int64, device=device)

model = Net().to(x.device)

optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)


for i in range(20):
  if not args.train:
    output = model(x)
    print(f'Eval-{i}: Result = {output.cpu()}')
  else:
    optimizer.zero_grad()
    output = model(x)
    loss = F.nll_loss(output, y)
    loss.backward()
    print(f'Train-{i}: Result = {loss.cpu().view([])}')
    optimizer.step()
