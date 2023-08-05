import torch
import torch.nn as nn
import torch.nn.functional as F
from flight_maneuvers.utils import *

class SE3_ResNetBlock(torch.nn.Module):
    pass


class SE3_PreActResNetBlock(torch.nn.Module):
    pass


resnet_block_types = {
    "ResNetBlock": SE3_ResNetBlock,
    "PreActResNetBlock": SE3_PreActResNetBlock
}

class SE3_ResNet(torch.nn.Module):
    pass