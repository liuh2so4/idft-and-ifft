import time
import cmath
import random

#points of num
pn = 1024
half_pn = int(pn / 2)

#omega  from 0 to points of num
omega = [complex(0, 0) for i in range(pn)]
for i in range(0, pn):
    omega[i] = cmath.cos(2*cmath.pi*i/pn) + cmath.sin(2*cmath.pi*i/pn)*1j

#complex matrix for the first a to x
u = [[complex(1, 0) for i in range(2)]for j in range(2)]
u[1][1] = cmath.cos(2*cmath.pi*(pn/2)/pn) + cmath.sin(2*cmath.pi*(pn/2)/pn)*1j

#ifft
def ifft(arr, num):
    x = [complex(0, 0) for i in range(pn)]
    for i in range(0, int(half_pn/num)):
        for j in range(0, num):
            x[i*2*num+j] = arr[i*num+j] + omega[j] * arr[i*num+j+half_pn]
            x[i*2*num+j+num] = arr[i*num+j] + omega[j+num] * arr[i*num+j+half_pn]
    num *= 2
    if num < pn:
        ifft(x, num)
    return x

t = 0
ifft_cnt = 0
while t < 60:
    a = [0 for i in range(pn)]
    for i in range(0, pn):
        a[i] = round(random.random(), 5)
    x = [complex(0, 0) for i in range(pn)]
    s = [complex(0, 0) for i in range(pn)]
    curtime = time.time()
    for i in range(0, half_pn):
        x[i*2] = u[0][0]*a[i] + u[0][1]*a[i+half_pn]
        x[i*2+1] = u[1][0]*a[i] + u[1][1]*a[i+half_pn]
    s = ifft(x, 2)
    t += (time.time() - curtime)
    ifft_cnt += 1
print("times to do 1024-points ifft:{}".format(ifft_cnt))
