import numpy as np
from numpy.linalg import norm
from math import *
import matplotlib.pyplot as plt
# vsetko je v SI jednotkach


# time
dt=0.1
N=int(300*1/dt)



# constants

m=0.100
g=9.81
l=0.06 #toto treba ceknut este
r=0.04
Io=m*0.5*r**2

T=15 #asi tak 12 az 18 to moze byt by som povedal, potrebuje spresnenie
k=2*pi**2*Io/(T**2)
c=0.00007

# variables
ax=0.1
av=0

px=pi*2*20
pv=0

Lx=Io*(radians(7200))
Lv=0

print(tan(ax),ax)

x_list = np.zeros((N, 2))
l_list = np.zeros((N,2))
p_list=np.zeros((N,2))

for i in range(N):
    pv=m*g*l*(tan(ax))/Lx
    # print("blbl",pv)
    av=-k*px*cos(ax)/Lx     -c*pv*cos(ax)/Lx
    Lv=-k*px*sin(ax)        -c*pv*sin(ax)

    # pv = m * g * l * ax / Lx
    # print(pv)
    # av = - k * px * ax / Lx  # -c*pv*cos(ax)/Lx
    # Lv = -k * px * ax  # -c*pv*sin(ax)


    px=px+pv*dt
    ax=ax+av*dt
    Lx=Lx+Lv*dt


    x_list[i] = [degrees(abs(ax)), i * dt]
    l_list[i]=[Lx,i*dt]
    p_list[i]=[px,i*dt]


plt.plot(x_list[:, 1], x_list[:, 0])
# plt.plot(l_list[:, 1], l_list[:, 0])
# plt.plot(p_list[:, 1], p_list[:, 0])
plt.show()
