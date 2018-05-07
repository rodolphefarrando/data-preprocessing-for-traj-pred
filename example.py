
from myclass.Representation import *

matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True


## Data importation
biwi = Representation('../data/train/biwi/biwi_hotel.txt',dataset='biwi')
#stanf1 = Representation('../data/train/stanford/bookstore_0.txt',dataset='st1')
#stanf2 = Representation('../data/train/stanford/bookstore_1.txt',dataset='st2')
#stanf3 = Representation('../data/train/stanford/bookstore_2.txt',dataset='st3')
crowds1 = Representation('../data/train/crowds/arxiepiskopi1.txt',dataset='cr1')
crowds2 = Representation('../data/train/crowds/crowds_zara02.txt',dataset='cr2')
crowds3 = Representation('../data/train/crowds/crowds_zara03.txt',dataset='cr3')
crowds4 = Representation('../data/train/crowds/students001.txt',dataset='cr4')
crowds5 = Representation('../data/train/crowds/students003.txt',dataset='cr5')
mot = Representation('../data/train/mot/PETS09-S2L1.txt',dataset='mot')

## Get trajectory type to put into the right folder
for i in range(biwi.number_traj):
    biwi.trajectoryType(i)
for i in range(crowds1.number_traj):
    crowds1.trajectoryType(i)
for i in range(crowds2.number_traj):
    crowds2.trajectoryType(i)##
for i in range(crowds3.number_traj):
    crowds3.trajectoryType(i)
for i in range(crowds4.number_traj):
    crowds4.trajectoryType(i)
for i in range(crowds5.number_traj):
    crowds5.trajectoryType(i)
for i in range(mot.number_traj):
    mot.trajectoryType(i)


## Create the .txt files
biwi.writeTxt()
crowds1.writeTxt()
crowds2.writeTxt()
crowds3.writeTxt()
crowds4.writeTxt()
crowds5.writeTxt()
mot.writeTxt()




