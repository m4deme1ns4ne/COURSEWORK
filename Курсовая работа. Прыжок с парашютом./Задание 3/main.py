import matplotlib.pyplot as plt
import numpy as np


class RocketSimulation:
    def __init__(self):
        # Исходные параметры модели
        self.g = 9.8
        self.m0 = 70
        self.mp = 15
        self.m = self.m0 + self.mp
        self.r = 0.3
        self.S0 = np.pi * self.r ** 2
        self.R = 5
        self.S1 = np.pi * self.R ** 2
        self.ro = 1.3
        self.Cx0 = 0.5
        self.Cx1 = 1.28
        self.k0 = self.Cx0 * self.ro * self.S0 / 2
        self.k1 = self.Cx1 * self.ro * self.S1 / 2
        self.H = 46
        self.tr = 3
        self.v0 = 0

        # Расчёт математической (теоретической) модели
        self.T = 500
        self.N = 20000
        self.dt = self.T / self.N
        self.y = np.zeros(self.N)
        self.v = np.zeros(self.N)
        self.t = np.zeros(self.N)
        self.y[0] = self.H
        self.v[0] = self.v0
        self.t[0] = 0

    def calculate_trajectory(self):
        k = self.k0
        for i in range(self.N - 1):
            if self.t[i] >= self.tr:
                k = self.k1
            self.y[i + 1] = self.y[i] + self.v[i] * self.dt
            self.v[i + 1] = self.v[i] - (self.g + k / self.m * abs(self.v[i]) * self.v[i]) * self.dt
            if self.y[i + 1] < 0:
                break
            self.t[i + 1] = self.t[i] + self.dt

    def plot_velocity_vs_height(self):
        i = np.argmax(self.y < 0)
        
        plt.title("v = v(y)")
        plt.xlabel('y, м', fontsize=14)
        plt.ylabel('v, м/с', fontsize=14)
        plt.plot(self.y[:i], self.v[:i])
        plt.grid()
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    rocket = RocketSimulation()
    rocket.calculate_trajectory()
    rocket.plot_velocity_vs_height()
