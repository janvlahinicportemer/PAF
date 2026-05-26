from seminar_1 import *
from seminar_2 import *
from scipy.optimize import minimize_scalar

#############################################################################################################################

def provjera_sudara(Ta, Tb, ID,
                    Xka, Yka, Zka,
                    Xkb, Ykb, Zkb,
                    V_Xka, V_Yka, V_Zka,
                    V_Xkb, V_Ykb, V_Zkb,
                    Xpa, Ypa, Zpa,
                    Xpb, Ypb, Zpb,
                    V_Xpa, V_Ypa, V_Zpa,
                    V_Xpb, V_Ypb, V_Zpb):
    
    Rka = np.array([Xka, Yka, Zka])
    Rkb = np.array([Xkb, Ykb, Zkb])

    Vka = np.array([V_Xka, V_Yka, V_Zka])
    Vkb = np.array([V_Xkb, V_Ykb, V_Zkb])

    Rpa = np.array([Xpa, Ypa, Zpa])
    Rpb = np.array([Xpb, Ypb, Zpb])

    Vpa = np.array([V_Xpa, V_Ypa, V_Zpa])
    Vpb = np.array([V_Xpb, V_Ypb, V_Zpb])

    Δt = Tb - Ta

    R_planet = R_rječnik[ID]

    A = R_planet[0] + R_komet
    B = R_planet[1] + R_komet
    C = R_planet[2] + R_komet

    body_frame = FRAME_rječnik[ID]

    #############################################################################################################################

    def S(λ):

        T_λ = Ta + λ * (Tb - Ta)

        h00 = 2*λ**3 - 3*λ**2 + 1
        h10 = λ**3 - 2*λ**2 + λ
        h01 = -2*λ**3 + 3*λ**2
        h11 = λ**3 - λ**2

        Rk_λ = h00*Rka + h10*Δt*Vka + h01*Rkb + h11*Δt*Vkb
        Rp_λ = h00*Rpa + h10*Δt*Vpa + h01*Rpb + h11*Δt*Vpb

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
        return True, t_sudar

    else:
        return False, None