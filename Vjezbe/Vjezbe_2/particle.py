import math
import matplotlib.pyplot as plt

class Particle:
    
    def __init__(self, V0, θ, X0, Y0):

        self.V0 = V0
        self.θ = θ
        self.X0 = X0
        self.Y0 = Y0

        self.g = 9.81

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)

        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        self.X_list = [self.X]
        self.Y_list = [self.Y]

    def reset(self):
        
        self.V0 = None
        self.θ = None
        self.X0 = None
        self.Y0 = None

        self.X = None
        self.Y = None

        self.Vx = None
        self.Vy = None
        
        self.X_list = []
        self.Y_list = []

    def __move(self, dt):

        self.X = self.X + self.Vx * dt
        self.Y = self.Y + self.Vy * dt

        # Vx = konst.
        self.Vy = self.Vy - self.g * dt

        if self.Y >= self.Y0:
            self.X_list.append(self.X)
            self.Y_list.append(self.Y)

    def range(self, dt):

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)
        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        self.X_list = [self.X]
        self.Y_list = [self.Y]

        while self.Y >= self.Y0:

            self.__move(dt)

        return self.X_list[-1]

    def plot_trajectory(self, dt):

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)
        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        self.X_list = [self.X]
        self.Y_list = [self.Y]

        while self.Y >= self.Y0:

            self.__move(dt)

        plt.figure()
        plt.plot(self.X_list, self.Y_list)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.title("x - y graf")
        plt.grid(True)
        plt.show()