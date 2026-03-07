import matplotlib.pyplot as plt

while True:
    try:
        F = float(input("Unesi silu u N: "))
        m = float(input("Unesi masu u kg: "))

        if m <= 0:
            print("Masa ne smije biti manja ili jednaka 0!")
            continue

        break
    except:
        print("Pogrešan unos!")

t_list = []
x_list = []
v_list = []
a_list = []

def f(F, m):
    a = F/m
    dt = 0.01
    t = 0
    x = 0
    v = 0
    while t <= 10:
        v = v + a*dt
        x = x + v*dt
        t_list.append(t)
        x_list.append(x)
        v_list.append(v)
        a_list.append(a)
        t = t + dt

f(F, m)

def xt_graf (t_list, x_list):
    plt.figure()
    plt.plot(t_list, x_list)
    plt.xlabel("t (s)")
    plt.ylabel("x (m)")
    plt.title("x - t graf")
    plt.show()

def vt_graf (t_list, v_list):
    plt.figure()
    plt.plot(t_list, v_list)
    plt.xlabel("t (s)")
    plt.ylabel("v (m/s)")
    plt.title("v - t graf")
    plt.show()

def at_graf (t_list, a_list):
    plt.figure()
    plt.plot(t_list, a_list)
    plt.xlabel("t (s)")
    plt.ylabel("a (m/s^2)")
    plt.title("a - t graf")
    plt.show()    

xt_graf (t_list, x_list)
vt_graf (t_list, v_list)
at_graf (t_list, a_list)