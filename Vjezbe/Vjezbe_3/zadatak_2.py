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

    #################################################################################################################################################################################################################################################

    def __move_EM(self, dt):

        v = math.sqrt(self.Vx**2 + self.Vy**2)
        a_x = - (self.b / self.m) * v * self.Vx
        a_y = - self.g - (self.b / self.m) * v * self.Vy 

        self.Vx = self.Vx + a_x * dt
        self.Vy = self.Vy + a_y * dt

        self.X = self.X + self.Vx * dt
        self.Y = self.Y + self.Vy * dt

        self.X_EM_list.append(self.X)
        self.Y_EM_list.append(self.Y)

    #################################################################################################################################################################################################################################################
    

    #################################################################################################################################################################################################################################################

    def plot_trajectory(self, dt):

        ##############################################################################################

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)
        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        self.X_EM_list = [self.X]
        self.Y_EM_list = [self.Y]

        while self.Y >= 0:

            self.__move_EM(dt)

        ##############################################################################################3

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)
        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        self.X_RK4_list = [self.X]
        self.Y_RK4_list = [self.Y]

        while self.Y >= 0:

            self.__move_RK4(dt)

        ##############################################################################################

        plt.figure()
        plt.plot(self.X_EM_list, self.Y_EM_list, label="EM")
        plt.plot(self.X_RK4_list, self.Y_RK4_list, label="RK4")
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.title("x - y graf")
        plt.grid(True)
        plt.legend()
        plt.show()


dt = 0.01

V0 = 10
θ = 45
X0 = 0
Y0 = 0
m = 1

ro = 10
Cd = 1
A = 0.5

b = (ro * Cd * A) / 2

p = Projectile(V0, θ, X0, Y0, m, b)
p.plot_trajectory(dt)