import math
import matplotlib.pyplot as plt

class Projectile:
    
    def __init__(self, V0, θ, X0, Y0, m, b):

        self.V0 = V0
        self.θ = θ
        self.X0 = X0
        self.Y0 = Y0

        self.g = 9.81
        self.m = m
        self.b = b

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)

        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        v = math.sqrt(self.Vx**2 + self.Vy**2)
        self.a_x = - (self.b / self.m) * v * self.Vx
        self.a_y = - self.g - (self.b / self.m) * v * self.Vy 

        self.X_list = [self.X]
        self.Y_list = [self.Y]

    def __move(self, dt):

        v = math.sqrt(self.Vx**2 + self.Vy**2)
        self.a_x = - (self.b / self.m) * v * self.Vx
        self.a_y = - self.g - (self.b / self.m) * v * self.Vy 

        self.Vx = self.Vx + self.a_x * dt
        self.Vy = self.Vy + self.a_y * dt

        self.X = self.X + self.Vx * dt
        self.Y = self.Y + self.Vy * dt

        self.X_list.append(self.X)
        self.Y_list.append(self.Y)

    def plot_trajectory(self, dt):

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)
        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        v = math.sqrt(self.Vx**2 + self.Vy**2)
        self.a_x = - (self.b / self.m) * v * self.Vx
        self.a_y = - self.g - (self.b / self.m) * v * self.Vy 

        self.X_list = [self.X]
        self.Y_list = [self.Y]

        while self.Y >= 0:

            self.__move(dt)

        plt.figure()
        plt.plot(self.X_list, self.Y_list)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.title("x - y graf")
        plt.grid(True)
        plt.show()


dt = float(input("Unesi dt: "))

V0 = float(input("Unesi V0: "))
θ = float(input("Unesi θ: "))
X0 = float(input("Unesi X0: "))
Y0 = float(input("Unesi Y0: "))
m = float(input("Unesi m: "))

ro = float(input("Unesi ρ: "))
Cd = float(input("Unesi Cd: "))
A = float(input("Unesi A: "))

b = (ro * Cd * A) / 2

p = Projectile(V0, θ, X0, Y0, m, b)
p.plot_trajectory(dt)