import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal


class Skydriver:
    g = 9.8
    m0 = 70
    mp = 15
    m = m0+mp
    r = 0.3
    S0 = np.pi*r**2
    R = 5
    S1 = np.pi*R**2
    ro = 1.3
    Cx0 = 0.5
    Cx1 = 1.28
    k0 = Cx0*ro*S0/2
    k1 = Cx1*ro*S1/2
    v0 = 0

    def __init__(self, H, tr) -> None:
        self.H = H
        self.tr = tr
