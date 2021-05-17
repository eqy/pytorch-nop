import torch

def conv2d():
  a = torch.tensor([0.0], device='cuda')
  a = a.reshape((1, 1, 1, 1))
  conv = torch.nn.Conv2D(in_channels=1, out_channels=1, kernel_size=1)
  b = conv(a)

def cholesky():
  a = torch.eye(1, device='cuda')
  a.cholseky()

if __name__ == '__main__':
  conv2d()
  cholesky()
