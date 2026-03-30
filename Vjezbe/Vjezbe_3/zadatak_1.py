import math
import matplotlib.pyplot as plt

class Projectile:
    
    def __init__(self, V0, θ, X0, Y0, m, b, c):

        self.V0 = V0
        self.θ = θ
        self.X0 = X0
        self.Y0 = Y0

        self.g = 9.81
        self.m = m
        self.b = b
        self.c = c

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)

        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        self.a_x = -(self.b*self.Vx + self.c*self.Vx*abs(self.Vx))/self.m
        self.a_y = -self.g - (self.b*self.Vy + self.c*self.Vy*abs(self.Vy))/self.m

        self.X_list = [self.X]
        self.Y_list = [self.Y]

    def __move(self, dt):

        self.a_x = -(self.b*self.Vx + self.c*self.Vx*abs(self.Vx))/self.m
        self.a_y = -self.g - (self.b*self.Vy + self.c*self.Vy*abs(self.Vy))/self.m
        
        self.Vx = self.Vx + self.a_x * dt
        self.Vy = self.Vy + self.a_y * dt

        self.X = self.X + self.Vx * dt
        self.Y = self.Y + self.Vy * dt

        self.X_list.append(self.X)
        self.Y_list.append(self.Y)

    def range(self, dt):

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)
        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        self.a_x = -(self.b*self.Vx + self.c*self.Vx*abs(self.Vx))/self.m
        self.a_y = -self.g - (self.b*self.Vy + self.c*self.Vy*abs(self.Vy))/self.m
        
        self.X_list = [self.X]
        self.Y_list = [self.Y]

        while self.Y >= 0:

            self.__move(dt)

        return self.X_list[-2]

    def plot_trajectory(self, dt):

        self.X = self.X0
        self.Y = self.Y0

        θ_radian = math.radians(self.θ)
        self.Vx = self.V0 * math.cos(θ_radian)
        self.Vy = self.V0 * math.sin(θ_radian)

        self.a_x = -(self.b*self.Vx + self.c*self.Vx*abs(self.Vx))/self.m
        self.a_y = -self.g - (self.b*self.Vy + self.c*self.Vy*abs(self.Vy))/self.m

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
0 = float(input("Unesi 0: "))
X0 = float(input("Unesi X0: "))
Y0 = float(input("Unesi Y0: "))
m = float(input("Unesi m: "))
b = float(input("Unesi b: "))
c = float(input("Unesi c: "))

p = Projectile(V0, 0, X0, Y0, m, b, c)
p.plot_trajectory(dt)