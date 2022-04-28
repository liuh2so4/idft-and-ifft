import random
import time
import math

#points of num
pn = 1024

#real and unreal matirx
real = [[0 for i in range(pn)]for j in range(pn)]
unreal = [[0 for i in range(pn)]for j in range(pn)]
for i in range(0, pn):
    for j in range(0, pn):
        real[i][j] = round(math.cos(2*math.pi*i*j/pn), 1)
        unreal[i][j] = round(math.sin(2*math.pi*i*j/pn), 10)

#idft
t = 0
idft_cnt = 0
while t < 60:
    #a choose from [0, 1] randomly
    a = [0]*pn
#    for i in range(0, pn):
#        a[i] = random.random()
    a = [1, 2, 3, 4]
    s_real = [0]*pn
    s_unreal = [0]*pn
    curtime = time.time()
    for i in range(0, pn):
        for j in range(0, pn):
            s_real[i] += a[j]*real[i][j]
            s_unreal[i] += a[j]*unreal[i][j]
    t += (time.time() - curtime)
    idft_cnt += 1
print("times to do 1024-points idft:{}".format(idft_cnt))
