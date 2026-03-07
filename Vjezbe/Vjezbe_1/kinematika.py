import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m):

    t_list = []
    x_list = []
    v_list = []
    a_list = []

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

    #xt_graf
    plt.plot(t_list, x_list)
    plt.xlabel("t (s)")
    plt.ylabel("x (m)")
    plt.title("x - t graf")
    plt.show()

    #vt_graf
    plt.plot(t_list, v_list)
    plt.xlabel("t (s)")
    plt.ylabel("v (m/s)")
    plt.title("v - t graf")
    plt.show()

    #at_graf
    plt.plot(t_list, a_list)
    plt.xlabel("t (s)")
    plt.ylabel("a (m/s^2)")
    plt.title("a - t graf")
    plt.show()    