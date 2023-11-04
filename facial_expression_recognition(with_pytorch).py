# Dataset available at kaggle
# https://www.kaggle.com/jonathanoheix/face-expression-recognition-dataset


# Imports"""

import numpy as np
import matplotlib.pyplot as plt
import torch

"""# Configurations"""

TRAINING_IMG_PATH = "/content/Facial-Expression-Dataset/train"
VALIDATION_IMG_PATH = "/content/Facial-Expression-Dataset/validation"

LEARNING_RATE = 0.001
BATCH_SIZE = 32
EPOCHS = 15

DEVICE = 'CUDA'
MODEL_NAME = 'EFFICIENTNET B0'

"""# Load Dataset"""

from torchvision.datasets import ImageFolder
from torchvision import transforms as T

train_augs = T.Compose([
    T.RandomHorizontalFlip(p = 0.5),
    T.RandomRotation(degrees=(-20, +20)),
    T.ToTensor()        #PIL/numpy.arr -> pytorch tensor(height, width, channel) -> (channel, height, width)
])

valid_augs = T.Compose([
    T.ToTensor()        #PIL/numpy.arr -> pytorch tensor(height, width, channel) -> (channel, height, width)
])

trainset = ImageFolder(TRAINING_IMG_PATH, transform= train_augs)
validset = ImageFolder(VALIDATION_IMG_PATH, transform= valid_augs)

print(f"Total no. of examples in trainset : {len(trainset)}")
print(f"Total no. of examples in validset : {len(validset)}")

print(trainset.class_to_idx)

#testNum = 0
#testNum = 9723
testNum = 3029


image, label = trainset[testNum]

plt.imshow(image.permute(1, 2, 0)) #will take the image in (h, w, c) format

plt.title(label)

"""# Load Dataset into Batches"""

from torch.utils.data import DataLoader





print(f"Total no. of batches in trainloader : {len(trainloader)}")
print(f"Total no. of batches in validloader : {len(validloader)}")

print(f"One image batch shape : {images.shape}")
print(f"One label batch shape : {labels.shape}")

"""# Create Model"""

import timm
from torch import nn





"""# Create Train and Eval Function"""

from tqdm import tqdm

def multiclass_accuracy(y_pred,y_true):
    top_p,top_class = y_pred.topk(1,dim = 1)
    equals = top_class == y_true.view(*top_class.shape)
    return torch.mean(equals.type(torch.FloatTensor))





"""# Create Training Loop"""





"""# Inference"""

def view_classify(img, ps):

    classes = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

    ps = ps.data.cpu().numpy().squeeze()
    img = img.numpy().transpose(1,2,0)

    fig, (ax1, ax2) = plt.subplots(figsize=(5,9), ncols=2)
    ax1.imshow(img)
    ax1.axis('off')
    ax2.barh(classes, ps)
    ax2.set_aspect(0.1)
    ax2.set_yticks(classes)
    ax2.set_yticklabels(classes)
    ax2.set_title('Class Probability')
    ax2.set_xlim(0, 1.1)

    plt.tight_layout()

    return None
