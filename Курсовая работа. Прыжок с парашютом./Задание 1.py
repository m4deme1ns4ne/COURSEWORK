import numpy as np
from my_class import Skydriver


class Skydriver1(Skydriver):
    def __init__(self, H, tr) -> None:
        super().__init__(H, tr)

    def task_1(self):
        T = 500
        N = 20000
        dt = T/N
        y = np.zeros(N)
        v = np.zeros(N)
        t = np.zeros(N)
        y[0] = self.H
        v[0] = Skydriver.v0
        t[0] = 0
        k = Skydriver.k0
        for i in range(N-1):
            if t[i]>=self.tr:
                k = Skydriver.k1
            y[i+1] = y[i]+v[i]*dt
            v[i+1] = v[i]-(Skydriver.g+k/Skydriver.m*abs(v[i])*v[i])*dt
            if y[i+1]<0:
                break
            t[i+1] = t[i]+dt


skydriver1 = Skydriver1(H=1000, tr=5)
skydriver1.task_1()