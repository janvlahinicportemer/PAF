import matplotlib.pyplot as plt

q_e = -1.602e-19 #(u C)
q_p = +1.602e-19 #(u c)

m = 9.109e-31 #(u kg)

x0 = 0 #(u m)
y0 = 0 #(u m)
z0 = 0 #(u m)

v_x0 = 1e6 #(u m/s)
v_y0 = 0.5e6 #(u m/s)
v_z0 = 0.2e6 #(u m/s)

E_x = [0, 100, 200, 300, 400, 500] #(u V/m)
E_y = [0, 50, 150, 250, 300, 350] #(u V/m)
E_z = [0, 0, 50, 100, 150, 200] #(u V/m)

B_x = [0, 0, 0, 0, 0] #(u T)
B_y = [0, 0, 0, 0, 0] #(u T)
B_z = [1e-3, 5e-3, 1e-2, 2e-2, 5e-2] #(u T)

dt = 1e-12 #(u s)
T = 5e-8 #(u s)
N = int(T / dt)

def gibanje_elektron (q_e, m, x, y, z, v_x, v_y, v_z, E_x, E_y, E_z, B_x, B_y, B_z, dt, N):
    
    x_lista = []
    y_lista = []
    z_lista = []
    t_lista = []

    for i in range(N):

        a_x = (q_e/m) * (E_x + v_y*B_z - v_z*B_y)
        a_y = (q_e/m) * (E_y + v_z*B_x - v_x*B_z)
        a_z = (q_e/m) * (E_z + v_x*B_y - v_y*B_x)

        v_x = v_x + a_x * dt
        v_y = v_y + a_y * dt
        v_z = v_z + a_z * dt

        x = x + v_x * dt
        y = y + v_y * dt
        z = z + v_z * dt

        x_lista.append(x)
        y_lista.append(y)
        z_lista.append(z)
        t_lista.append(i*dt)
    
    return x_lista, y_lista, z_lista, t_lista

def gibanje_pozitron (q_p, m, x, y, z, v_x, v_y, v_z, E_x, E_y, E_z, B_x, B_y, B_z, dt, N):
    
    x_lista = []
    y_lista = []
    z_lista = []
    t_lista = []

    for i in range(N):

        a_x = (q_p/m) * (E_x + v_y*B_z - v_z*B_y)
        a_y = (q_p/m) * (E_y + v_z*B_x - v_x*B_z)
        a_z = (q_p/m) * (E_z + v_x*B_y - v_y*B_x)

        v_x = v_x + a_x * dt
        v_y = v_y + a_y * dt
        v_z = v_z + a_z * dt

        x = x + v_x * dt
        y = y + v_y * dt
        z = z + v_z * dt

        x_lista.append(x)
        y_lista.append(y)
        z_lista.append(z)
        t_lista.append(dt*i)

    return x_lista, y_lista, z_lista, t_lista

#################################################################################################################################################################################################################################################

for i in range (len(B_x)):

    x_lista_e, y_lista_e, z_lista_e, t_lista = gibanje_elektron (q_e, m, x0, y0, z0, v_x0, v_y0, v_z0, E_x[i], E_y[i], E_z[i], B_x[i], B_y[i], B_z[i], dt, N)
    x_lista_p, y_lista_p, z_lista_p, t_lista = gibanje_pozitron (q_p, m, x0, y0, z0, v_x0, v_y0, v_z0, E_x[i], E_y[i], E_z[i], B_x[i], B_y[i], B_z[i], dt, N)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(x_lista_e, y_lista_e, z_lista_e, label="Elektron")
    ax.plot(x_lista_p, y_lista_p, z_lista_p, label="Pozitron")

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_title(f"xyz-graf\nE=({E_x[i]}, {E_y[i]}, {E_z[i]}) V/m\n B=({B_x[i]}, {B_y[i]}, {B_z[i]}) T")
    ax.legend()
    plt.show()

#################################################################################################################################################################################################################################################