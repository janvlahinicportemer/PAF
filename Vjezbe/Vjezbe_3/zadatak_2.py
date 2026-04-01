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
    
    def __move_RK4(self, dt):

        #####k1#####
        v1 = math.sqrt(self.Vx**2 + self.Vy**2)
        a1_x = - (self.b / self.m) * v1 * self.Vx
        a1_y = - self.g - (self.b / self.m) * v1 * self.Vy

        k1_X = self.Vx
        k1_Y = self.Vy
        k1_Vx = a1_x
        k1_Vy = a1_y

        #####k2#####
        Vx2 = self.Vx + k1_Vx * dt / 2
        Vy2 = self.Vy + k1_Vy * dt / 2

        v2 = math.sqrt(Vx2**2 + Vy2**2)
        a2_x = - (self.b / self.m) * v2 * Vx2
        a2_y = - self.g - (self.b / self.m) * v2 * Vy2

        k2_X = Vx2
        k2_Y = Vy2
        k2_Vx = a2_x
        k2_Vy = a2_y

        #####k3#####
        Vx3 = self.Vx + k2_Vx * dt / 2
        Vy3 = self.Vy + k2_Vy * dt / 2

        v3 = math.sqrt(Vx3**2 + Vy3**2)
        a3_x = - (self.b / self.m) * v3 * Vx3
        a3_y = - self.g - (self.b / self.m) * v3 * Vy3

        k3_X = Vx3
        k3_Y = Vy3
        k3_Vx = a3_x
        k3_Vy = a3_y

        #####k4#####
        Vx4 = self.Vx + k3_Vx * dt
        Vy4 = self.Vy + k3_Vy * dt

        v4 = math.sqrt(Vx4**2 + Vy4**2)
        a4_x = - (self.b / self.m) * v4 * Vx4
        a4_y = - self.g - (self.b / self.m) * v4 * Vy4

        k4_X = Vx4
        k4_Y = Vy4
        k4_Vx = a4_x
        k4_Vy = a4_y

        ############

        self.Vx = self.Vx + 1/6 * (k1_Vx + 2*k2_Vx + 2*k3_Vx + k4_Vx) * dt
        self.Vy = self.Vy + 1/6 * (k1_Vy + 2*k2_Vy + 2*k3_Vy + k4_Vy) * dt

        self.X = self.X + 1/6 * (k1_X + 2*k2_X + 2*k3_X + k4_X) * dt
        self.Y = self.Y + 1/6 * (k1_Y + 2*k2_Y + 2*k3_Y + k4_Y) * dt

        self.X_RK4_list.append(self.X)
        self.Y_RK4_list.append(self.Y)

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