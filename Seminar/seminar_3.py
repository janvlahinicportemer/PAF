from RK4 import *
from seminar_1 import *
from seminar_2 import *
from provjera_sudara import *

m = N
n = len(ID_valid_list) + 1
p = 5 # ID, x, y, vx, vy
M_mnp = np.zeros((m, n, p))
a_all = np.zeros((m, 2))

i_kraj = 0

for i, t in enumerate(t_list):

    ax_total = 0
    ay_total = 0

    if i==0:
        
        x_komet = x0_komet
        y_komet = y0_komet

        vx_komet = vx0_komet
        vy_komet = vy0_komet

        M_mnp[0, 0, :] = [-1, x_komet, y_komet, vx_komet, vy_komet]
            
        for j, ID in enumerate(ID_valid_list):
            
            state_vector, _ = sp.spkezr(str(ID), t, referentni_sustav, abcorr, ishodište)
            x, y, z, vx, vy, vz = state_vector
            M_mnp[0, j+1, :] = [ID, x, y, vx, vy]

            dx = x - x_komet
            dy = y - y_komet

            R_j = np.sqrt(dx**2 + dy**2)

            GM = GM_rječnik[ID]

            ax = GM * dx / R_j**3
            ay = GM * dy / R_j**3

            ax_total = ax_total + ax
            ay_total = ay_total + ay
        
        a_all[0, :] = [ax_total, ay_total]

    else:
        
        x_komet, y_komet, vx_komet, vy_komet = RK4(t_list[i-1], dt, M_mnp[i-1, 0, 1:3], M_mnp[i-1, 0, 3:5])

        M_mnp[i, 0, :] = [-1, x_komet, y_komet, vx_komet, vy_komet]

        for j, ID in enumerate(ID_valid_list):
            
            state_vector, _ = sp.spkezr(str(ID), t, referentni_sustav, abcorr, ishodište)
            x, y, z, vx, vy, vz = state_vector
            M_mnp[i, j+1, :] = [ID, x, y, vx, vy]

            dx = x - x_komet
            dy = y - y_komet

            R_j = np.sqrt(dx**2 + dy**2)

            sudar, t_sudar = provjera_sudara(t_list[i-1], t_list[i], ID,
                                             M_mnp[i-1, 0, 1], M_mnp[i-1, 0, 2],
                                             M_mnp[i,   0, 1], M_mnp[i,   0, 2],
                                             M_mnp[i-1, 0, 3], M_mnp[i-1, 0, 4],
                                             M_mnp[i,   0, 3], M_mnp[i,   0, 4],
                                             M_mnp[i-1, j+1, 1], M_mnp[i-1, j+1, 2],
                                             M_mnp[i,   j+1, 1], M_mnp[i,   j+1, 2],
                                             M_mnp[i-1, j+1, 3], M_mnp[i-1, j+1, 4],
                                             M_mnp[i,   j+1, 3], M_mnp[i,   j+1, 4])
                                                    
            if sudar:
                
                vrijeme_sudara_utc = sp.et2utc(t_sudar, "C", 0)

                print("Sudar s tijelom:", IME_rječnik[ID])
                print("Vrijeme sudara UTC:", vrijeme_sudara_utc)
                i_kraj = i -1

                break

            GM = GM_rječnik[ID]

            ax = GM * dx / R_j**3
            ay = GM * dy / R_j**3

            ax_total = ax_total + ax
            ay_total = ay_total + ay

        if sudar:
            break

        a_all[i, :] = [ax_total, ay_total]
        i_kraj = i