from seminar_1 import *
from seminar_2 import *
from scipy.optimize import minimize_scalar

#############################################################################################################################

def provjera_sudara(Ta, Tb, ID, 
                    Xka, Yka, Zka,
                    Xkb, Ykb, Zkb,
                    Xpa, Ypa, Zpa,
                    Xpb, Ypb, Zpb):
    
    Rka = np.array([Xka, Yka, Zka])
    Rkb = np.array([Xkb, Ykb, Zkb])

    Rpa = np.array([Xpa, Ypa, Zpa])
    Rpb = np.array([Xpb, Ypb, Zpb])

    R_planet = R_rječnik[ID]

    A = R_planet[0] + R_komet
    B = R_planet[1] + R_komet
    C = R_planet[2] + R_komet

    body_frame = FRAME_rječnik[ID]

    #############################################################################################################################

    def S(λ):

        T_λ = Ta + λ * (Tb - Ta)

        Rk_λ = Rka + λ * (Rkb - Rka)
        Rp_λ = Rpa + λ * (Rpb - Rpa)

        D_J2000_λ = Rk_λ - Rp_λ

        rotacija = sp.pxform("J2000", body_frame, T_λ)
        D_planet_λ = rotacija @ D_J2000_λ

        X_λ = D_planet_λ[0]
        Y_λ = D_planet_λ[1]
        Z_λ = D_planet_λ[2]

        S_λ = X_λ**2 / A**2 + Y_λ**2 / B**2 + Z_λ**2 / C**2

        return S_λ

    #############################################################################################################################

    rezultat = minimize_scalar(S, bounds=(0, 1), method="bounded")

    λ_min = rezultat.x
    S_min = rezultat.fun

    t_sudar = Ta + λ_min * (Tb - Ta)

    if S_min <= 1:
        return True, t_sudar, λ_min, S_min
        
    else:
        return False, None, λ_min, S_min