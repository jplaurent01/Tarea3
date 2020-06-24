# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:11:25 2020

@author: Jose Pablo
grupo 01
B63761
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from mpl_toolkits import mplot3d
import csv

#VARIABLES
Nx = 11 #cantidad de elementos en X
Ny = 21 #cantidad de elementos en y
cor = 0 #correlación
covar = 0 #covarianza

lxs = []#Vector de A
lys = []#Vector de B
lps = []#Vector de C


xs = []#Vector de A
ys = []#Vector de B
ps = []#Vector de C
############################################################################################
#Punto 1
xy = np.loadtxt('xy.csv', delimiter= ',', skiprows=1, usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 ) )
Fy = np.sum(xy, axis=0 ) #vector columnas
Fx = np.sum(xy, axis=1 ) #vector filas

X = [0]*Nx#vector de exis
Y = [0]*Ny#vector de yes

for i in range(Nx):
  X[i] = i + 5

for i in range(Ny):
  Y[i] = i + 5

#Se imprimen los datos del archivo xy.csv
fig1=plt.figure()
plt.plot(Y, Fy)
fig2=plt.figure()
plt.plot(X, Fx)

#Se crea una función gaussiana para obtener parámetros
def guass(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x - mu)**2/(2*sigma**2))

#Se hallan los parámetros de la curvas de mejor ajuste 
param1, _ = curve_fit(guass, X, Fx)#Parametros de FX
param2, _ = curve_fit(guass, Y, Fy)#Parametros de Fy


#Se imprimen parametros de funciones de densidad marginales
print("Punto 1 :")
print("Parámetros de curvas de mejor ajuste :")
print("Mu de Fx :", param1[0])
print("Sigma de Fx :", param1[1])
print("Mu de Fy :", param2[0])
print("Sigma de Fy :", param2[1])

#Se muestra en consola curvas de mejor ajuste
fig3=plt.figure()
plt.plot(X, guass(X, param1[0], param1[1]))#Curva de mejor ajuste para Fx
fig4=plt.figure()
plt.plot(Y, guass(Y, param2[0], param2[1]))#Curva de mejor ajuste para Fy

############################################################################################
#Punto 3
with open('xyp.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV,None)
    for row in readCSV:
        lxs.append(row[0])#asignar valor
        lys.append(row[1])#asignar valor
        lps.append(row[2])#asignar valor
    
#se convierten datos leidos a valores numericos punto flotante
xs = list(map(float, lxs)) 
ys = list(map(float, lys))
ps = list(map(float, lps))     
    
#Correlación 
for  i in range(len(ps)):
    cor += (xs[i]*ys[i])*ps[i]

#Covarianza
for  i in range(len(ps)):
    covar += ((xs[i] - param1[0])*(ys[i] - param2[0]))*ps[i]
    
#coeficiente de correlación
cofcorr=(covar)/(param1[1]*param2[1])

#Imprimir valores de correlación, covarianza y coeficiente de correlación
print('Punto 3 : ')
print('Correlación : ', cor)
print('Covarianza  :', covar)
print('Coeficiente de correlación : ', cofcorr)


#Punto 4:
fig5=plt.figure()
plt.rcParams["figure.figsize"] = 12.8, 9.6
ax = plt.axes(projection='3d')

def LoG(x, mu, sigma, y, mu1, sigma1 ):  
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x - mu)**2/(2*sigma**2)) * 1/(np.sqrt(2*np.pi*sigma1**2)) * np.exp(-(y - mu1)**2/(2*sigma1**2))

X2, Y2 = np.meshgrid(range(5, 16),range(5, 26) )#genera una cuadricula
Z2 = LoG(X2, param1[0], param1[1], Y2, param2[0], param2[1] )

ax = plt.axes(projection='3d')
ax.plot_surface(X2, Y2, Z2, cmap='jet')







