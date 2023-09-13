import numpy as np
import matplotlib as mp

opc = False

dt=0.02
vel=0.0
VMotor=0.0
valorM=0.0

referencia=0

e = [0.0 , 0.0 , 0.0]
u = [0.0 , 0.0 , 0.0]

kp = 0.0
ki = 0.0
kd = 0.0

Ts = 0.0

k1 = 0.0
k2 = 0.0
k3 = 0.0

kp = 1.4
ki = 3.0
kd = 0.05
Ts = 0.02

k1 = kp + Ts*ki + kd/Ts
k2 = -kp - 2.0*kd/Ts
k3 = kd/Ts

while not opc:
    if t1 - tiempo > 20000:
        tiempo = t1 


        e[0] = referencia - vel
        u[0] = k1*e[0] + k2*e[1] + k3*e[2] + u[1]

        e[2]=e[1]
        e[1]=e[0]
        u[1]=u[0]

        if u[0]>255 : u[0] = 255
        if u[0]<-255: u[0] = -255

        res = 0.0

        if u[0]>=0 : res = u[0]
        if u[0] < 0 : res = - u[0]


