__author__ = 'Jose'

import csv
import random
import array

#Ruta de la carpeta
ruta = 'C://Users//Jose//Desktop//Practica 1 - IA//'

#Nombre de los archivos csv
ficherox = 'VariablesX.csv'
ficheroy = 'VariablesY.csv'

#Ruta completa de los archivos csv
objx = ruta + ficherox
objy = ruta + ficheroy

#Variables m y n
m = 0
n = 0

#Matriz
matriz = []

with open(objx) as lecturaX:
    reader = csv.reader(lecturaX, delimiter=",")
    matriz = list(reader)

    #cantidad de columnas
    temp = (str(matriz[0])).split()
    m = len(temp) + 1

    #cantidad de filas
    n = len(matriz)
print ('M = %i' % m)
print ('N = %i' % n)
print ('----------------------------------------------------------------------------------------')

with open(objy) as lecturaY:
    reader = csv.reader(lecturaY, delimiter=",")
    listay = list(reader)
lecturaY.close()

print('VariablesX.csv = %s' % matriz)
print('VariablesY.csv = %s' % listay)
print ('----------------------------------------------------------------------------------------')

sumah = 0.0
cadenah = 'Hipotesis h(x) = '
listah = [0,0,0,0,0]
x = 0
z = 0
for x in range (n):
    for z in range (m-1):
        cadenah += ' + ' + str(matriz[x][z]) + '*' + str(random.randint(-20,20))
        sumah += ( float(matriz[x][z]) * random.randint(-20,20))
    listah[x] = sumah
    print ('%s = %f' % (cadenah, sumah))
    cadenah = 'Hipotesis h(x) = '
    sumah = 0.0

print ('----------------------------------------------------------------------------------------')
print('Lista de Hipotesis h(x) = %s ' % listah)

print ('----------------------------------------------------------------------------------------')
sumac = 0.0
x = 0
for x in range (n):
    sumac += ((1/(2*float(m)))*(9.5)*2)
print('Función de Costo J(Theta) = %f' % sumac)



