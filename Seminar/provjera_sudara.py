from seminar_1 import *
from seminar_2 import *
from scipy.optimize import minimize_scalar

def provjera_sudara(Ta, Tb, ID,
                    Xka, Yka,
                    Xkb, Ykb,
                    V_Xka, V_Yka,
                    V_Xkb, V_Ykb,
                    Xpa, Ypa,
                    Xpb, Ypb,
                    V_Xpa, V_Ypa,
                    V_Xpb, V_Ypb):
    
    Rka = np.array([Xka, Yka])
    Rkb = np.array([Xkb, Ykb])

    Vka = np.array([V_Xka, V_Yka])
    Vkb = np.array([V_Xkb, V_Ykb])

    Rpa = np.array([Xpa, Ypa])
    Rpb = np.array([Xpb, Ypb])

    Vpa = np.array([V_Xpa, V_Ypa])
    Vpb = np.array([V_Xpb, V_Ypb])

    Δt = Tb - Ta

    R_planet = R_rječnik[ID]
    
    #############################################################################################################################

    def D(λ):

        h00 = 2*λ**3 - 3*λ**2 + 1
        h10 = λ**3 - 2*λ**2 + λ
        h01 = -2*λ**3 + 3*λ**2
        h11 = λ**3 - λ**2

        Rk_λ = h00*Rka + h10*Δt*Vka + h01*Rkb + h11*Δt*Vkb
        Rp_λ = h00*Rpa + h10*Δt*Vpa + h01*Rpb + h11*Δt*Vpb

        D_λ = Rk_λ - Rp_λ
        
        X_λ = D_λ[0]
        Y_λ = D_λ[1]

        D_λ = np.sqrt(X_λ**2 + Y_λ**2)

        return D_λ

    #############################################################################################################################

    rezultat = minimize_scalar(D, bounds=(0, 1), method="bounded")

    λ_min = rezultat.x
    D_min = rezultat.fun

    t_sudar = Ta + λ_min * (Tb - Ta)

    if D_min <= (R_planet + R_komet):
        return True, t_sudar

    else:
        return False, None