from seminar_1 import *
from seminar_2 import *

def RK4(t_old, dt, r_old, v_old):

    Y_old = np.array([r_old[0], r_old[1], r_old[2], v_old[0], v_old[1], v_old[2]])

    k1 = F(t_old, Y_old)
    k2 = F(t_old + dt/2, Y_old + dt*k1/2)
    k3 = F(t_old + dt/2, Y_old + dt*k2/2)
    k4 = F(t_old + dt, Y_old + dt*k3)

    Y_new = Y_old + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

    return Y_new

#############################################################################################################################3

def F(t, Y):

    r_komet = Y[0:3]
    v_komet = Y[3:6]

    a_komet = akceleracija(t, r_komet)

    dY_dt = np.array([v_komet[0], v_komet[1], v_komet[2], a_komet[0], a_komet[1], a_komet[2]])

    return dY_dt

#############################################################################################################################

def akceleracija(t, r_komet):

    ax_total = 0
    ay_total = 0
    az_total = 0

    x_komet = r_komet[0]
    y_komet = r_komet[1]
    z_komet = r_komet[2]

    for ID in ID_valid_list:

        state_vector, _ = sp.spkezr(str(ID), t, referentni_sustav, abcorr, ishodište)
        x, y, z, vx, vy, vz = state_vector

        dx = x - x_komet
        dy = y - y_komet
        dz = z - z_komet

        R_j = np.sqrt(dx**2 + dy**2 + dz**2)

        GM = GM_rječnik[ID]

        ax_total = ax_total + GM * dx / R_j**3
        ay_total = ay_total + GM * dy / R_j**3
        az_total = az_total + GM * dz / R_j**3
    
    a_komet = np.array([ax_total, ay_total, az_total])

    return a_komet