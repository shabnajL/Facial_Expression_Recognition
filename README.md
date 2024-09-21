# Facial_Expression_Recognition
# Dataset available at kaggle
https://www.kaggle.com/jonathanoheix/face-expression-recognition-dataset
#-------------------------------------------------------------------------------

Steps included:
1. Importing necessary package
2. Setting up the (co-lab) system
3. Importing Data
4. Putting the Dataset into Groups.
5. Creating the Model
6. Design the Train and Eval Process
7. Creating a Training Loop
#-------------------------------------------------------------------------------

Total no. of examples in trainset : 28821
Total no. of examples in validset : 7066

{'angry': 0, 'disgust': 1, 'fear': 2, 'happy': 3, 'neutral': 4, 'sad': 5, 'surprise': 6}

![image](https://github.com/user-attachments/assets/f14af0ea-3335-4171-bf23-55d8435ca595)


Total no. of batches in trainloader : 901
Total no. of batches in validloader : 221


EPOCH[TRAIN]1/15: 100%|██████████| 901/901 [13:11<00:00,  1.14it/s, loss=0.826885, accuracy=0.694552]
EPOCH[VALID]1/15: 100%|██████████| 221/221 [00:42<00:00,  5.23it/s, loss=1.013705, accuracy=0.638520]
BEST WEIGHTS SAVED.
EPOCH[TRAIN]2/15: 100%|██████████| 901/901 [13:02<00:00,  1.15it/s, loss=0.799865, accuracy=0.703464]
EPOCH[VALID]2/15: 100%|██████████| 221/221 [00:40<00:00,  5.48it/s, loss=0.997784, accuracy=0.633669]
BEST WEIGHTS SAVED.
EPOCH[TRAIN]3/15: 100%|██████████| 901/901 [13:05<00:00,  1.15it/s, loss=0.775841, accuracy=0.711602]
EPOCH[VALID]3/15: 100%|██████████| 221/221 [00:40<00:00,  5.42it/s, loss=0.992747, accuracy=0.646297]
BEST WEIGHTS SAVED.
EPOCH[TRAIN]4/15: 100%|██████████| 901/901 [13:08<00:00,  1.14it/s, loss=0.751623, accuracy=0.722768]
EPOCH[VALID]4/15: 100%|██████████| 221/221 [00:39<00:00,  5.53it/s, loss=0.991767, accuracy=0.649669]
BEST WEIGHTS SAVED.
EPOCH[TRAIN]5/15: 100%|██████████| 901/901 [13:02<00:00,  1.15it/s, loss=0.739648, accuracy=0.729188]
EPOCH[VALID]5/15: 100%|██████████| 221/221 [00:40<00:00,  5.50it/s, loss=1.210786, accuracy=0.586169]
EPOCH[TRAIN]6/15: 100%|██████████| 901/901 [12:58<00:00,  1.16it/s, loss=0.743632, accuracy=0.726357]
EPOCH[VALID]6/15: 100%|██████████| 221/221 [00:40<00:00,  5.45it/s, loss=1.019200, accuracy=0.642632]
EPOCH[TRAIN]7/15: 100%|██████████| 901/901 [12:53<00:00,  1.16it/s, loss=0.687787, accuracy=0.747465]
EPOCH[VALID]7/15: 100%|██████████| 221/221 [00:41<00:00,  5.30it/s, loss=1.033776, accuracy=0.643687]
EPOCH[TRAIN]8/15: 100%|██████████| 901/901 [12:59<00:00,  1.16it/s, loss=0.670102, accuracy=0.753690]
EPOCH[VALID]8/15: 100%|██████████| 221/221 [00:42<00:00,  5.24it/s, loss=1.035283, accuracy=0.648495]
EPOCH[TRAIN]9/15: 100%|██████████| 901/901 [12:58<00:00,  1.16it/s, loss=0.643459, accuracy=0.763470]
EPOCH[VALID]9/15: 100%|██████████| 221/221 [00:42<00:00,  5.24it/s, loss=1.069206, accuracy=0.649093]
EPOCH[TRAIN]10/15: 100%|██████████| 901/901 [13:13<00:00,  1.14it/s, loss=0.619384, accuracy=0.772452]
EPOCH[VALID]10/15: 100%|██████████| 221/221 [00:42<00:00,  5.23it/s, loss=1.076534, accuracy=0.653019]
EPOCH[TRAIN]11/15: 100%|██████████| 901/901 [13:17<00:00,  1.13it/s, loss=0.597464, accuracy=0.782010]
EPOCH[VALID]11/15: 100%|██████████| 221/221 [00:42<00:00,  5.17it/s, loss=1.090667, accuracy=0.649300]
EPOCH[TRAIN]12/15: 100%|██████████| 901/901 [13:08<00:00,  1.14it/s, loss=0.608411, accuracy=0.777255]
EPOCH[VALID]12/15: 100%|██████████| 221/221 [00:42<00:00,  5.24it/s, loss=1.127293, accuracy=0.643752]
EPOCH[TRAIN]13/15: 100%|██████████| 901/901 [13:15<00:00,  1.13it/s, loss=0.568877, accuracy=0.792554]
EPOCH[VALID]13/15: 100%|██████████| 221/221 [00:41<00:00,  5.32it/s, loss=1.147480, accuracy=0.639793]
EPOCH[TRAIN]14/15: 100%|██████████| 901/901 [13:14<00:00,  1.13it/s, loss=0.545598, accuracy=0.801033]
EPOCH[VALID]14/15: 100%|██████████| 221/221 [00:42<00:00,  5.20it/s, loss=1.074095, accuracy=0.656859]
EPOCH[TRAIN]15/15: 100%|██████████| 901/901 [13:11<00:00,  1.14it/s, loss=0.527560, accuracy=0.804503]
EPOCH[VALID]15/15: 100%|██████████| 221/221 [00:41<00:00,  5.28it/s, loss=1.120600, accuracy=0.641522]
![image](https://github.com/user-attachments/assets/18c6c085-d6aa-44e7-87b0-3d0febe8bb40)





![image](https://github.com/user-attachments/assets/acd52984-76d9-4d61-b3f7-875dddca19e9)
![image](https://github.com/user-attachments/assets/0cbb6fe6-99c7-468e-ba1d-393d318e9a94)
![image](https://github.com/user-attachments/assets/6792a4d0-70da-4eb6-b272-d2d9695f8d02)


