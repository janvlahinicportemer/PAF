from RK4 import *
from seminar_1 import *
from seminar_2 import *
from provjera_sudara import *

### DEFINIRANJE MATRICE DIMENZIJE MxNxP ###
m = N
n = len(ID_valid_list) + 1
p = 7 # ID, x, y, z, vx, vy, vz
M_mnp = np.zeros((m, n, p))
a_all = np.zeros((m, 3))

for i, t in enumerate(t_list):

    ax_total = 0
    ay_total = 0
    az_total = 0

    if i==0:
        
        x_komet = x0_komet
        y_komet = y0_komet
        z_komet = z0_komet

        vx_komet = vx0_komet
        vy_komet = vy0_komet
        vz_komet = vz0_komet

        M_mnp[0, 0, :] = [-1, x_komet, y_komet, z_komet, vx_komet, vy_komet, vz_komet]
            
        for j, ID in enumerate(ID_valid_list):
            
            state_vector, _ = sp.spkezr(str(ID), t, referentni_sustav, abcorr, ishodište)
            x, y, z, vx, vy, vz = state_vector
            M_mnp[0, j+1, :] = [ID, x, y, z, vx, vy, vz]

            dx = x - x_komet
            dy = y - y_komet
            dz = z - z_komet

            R_j = np.sqrt(dx**2 + dy**2 + dz**2)

            GM = GM_rječnik[ID]

            ax = GM * dx / R_j**3
            ay = GM * dy / R_j**3
            az = GM * dz / R_j**3

            ax_total = ax_total + ax
            ay_total = ay_total + ay
            az_total = az_total + az
        
        a_all[0, :] = [ax_total, ay_total, az_total]

    else:
        
        x_komet, y_komet, z_komet, vx_komet, vy_komet, vz_komet = RK4(t_list[i-1], dt, M_mnp[i-1, 0, 1:4], M_mnp[i-1, 0, 4:7])
        
        M_mnp[i, 0, :] = [-1, x_komet, y_komet, z_komet, vx_komet, vy_komet, vz_komet]

        for j, ID in enumerate(ID_valid_list):
            
            state_vector, _ = sp.spkezr(str(ID), t, referentni_sustav, abcorr, ishodište)
            x, y, z, vx, vy, vz = state_vector
            M_mnp[i, j+1, :] = [ID, x, y, z, vx, vy, vz]

            dx = x - x_komet
            dy = y - y_komet
            dz = z - z_komet

            R_j = np.sqrt(dx**2 + dy**2 + dz**2)

            sudar, t_sudar = provjera_sudara(t_list[i-1], t_list[i], ID,
                                                      M_mnp[i-1, 0, 1], M_mnp[i-1, 0, 2], M_mnp[i-1, 0, 3],
                                                      M_mnp[i,   0, 1], M_mnp[i,   0, 2], M_mnp[i,   0, 3],
                                                      M_mnp[i-1,j+1,1], M_mnp[i-1,j+1,2], M_mnp[i-1,j+1,3],
                                                      M_mnp[i,  j+1,1], M_mnp[i,  j+1,2], M_mnp[i, j+1, 3])

            if sudar:
                
                vrijeme_sudara_utc = sp.et2utc(t_sudar, "C", 3)

                print("Sudar s tijelom:", IME_rječnik[ID])
                print("Vrijeme sudara UTC:", vrijeme_sudara_utc)

                break

            GM = GM_rječnik[ID]

            ax = GM * dx / R_j**3
            ay = GM * dy / R_j**3
            az = GM * dz / R_j**3

            ax_total = ax_total + ax
            ay_total = ay_total + ay
            az_total = az_total + az

        if sudar:
            break

        a_all[i, :] = [ax_total, ay_total, az_total]