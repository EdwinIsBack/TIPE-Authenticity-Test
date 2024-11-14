import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import *
img = mpimg.imread('billet10e.png')
img2= mpimg.imread('billet10e2.png')
#Conversion si necessaire en tableau d'entiers
if img.dtype == np.float32: # Si ce n'est pas un tableau d'entiers
    img = (img * 255).astype(np.uint8)
if img2.dtype == np.float32:
    img2 = (img2 * 255).astype(np.uint8)

#Suppression du quatrième plan

img = img[:,:,:3]
img2 = img2[:,:,:3]
#Conversion image en niveau de gris
#R,G,B=img[:,:,0], img[:,:,1], img[:,:,2]
#R1,G1,B1=img2[:,:,0], img[:,:,1], img[:,:,2]
#print(R1)
imgGray=np.copy(img)
nb_lignes=img.shape[0]
nb_colonnes=img.shape[1]
nb_lignes2=img2.shape[0]
nb_colonnes2=img2.shape[1]
for i in range(nb_lignes):
    for j in range(nb_colonnes):
        r,v,b=img[i,j]
        g=r//3+v//3+b//3
        imgGray[i,j]=g,g,g
        if imgGray[i,j][0]<127:
            imgGray[i,j]=0,0,0
        else:
            imgGray[i,j]=255,255,255
imgGray2=np.copy(img2)
for i in range(nb_lignes2):
    for j in range(nb_colonnes2):
        r1,v1,b1=img2[i,j]
        g=r1//3+v1//3+b1//3
        imgGray2[i,j]=g,g,g
        if imgGray2[i,j][0]<127:
            imgGray2[i,j]=0,0,0
        else:
            imgGray2[i,j]=255,255,255
#print(imgGray)
#imgGray= 0.299*R + 0.587*G + 0.114*B
#imgGray2=np.copy(imgGray)
#imgGray2= 0.2989*R1 + 0.5870*G1 + 0.1140*B1
#print(type(imgGray2))
#dimensions de l'image originale


plt.imshow(imgGray)
plt.show()


plt.imshow(imgGray2)
plt.show()
#print(type(imgGray[0,0][0]))
#print(imgGray2)
#K PLUS PROCHES VOISINS SQRT((R-R)^^2+(V-V)^^2+(B-B)^^2) c est la distance
#regarder l ecart dcp et si il est petit on peu considerer que c est un vrai billet
dist=sqrt((imgGray[100][100][0]-imgGray2[100][100][0])**2+(imgGray[100][100][1]-imgGray2[100][100][1])**2+(imgGray[100][100][2]-imgGray2[100][100][2])**2)
print(dist)
#dr,dv,db=img2[0][0]-img[0][0]
#print(sqrt((dr**2)+(dv**2)+(db**2)))
