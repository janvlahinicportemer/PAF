from seminar_1 import *
from seminar_2 import *
from scipy.optimize import minimize_scalar, brentq

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

    X_λ = D_planet_λ[0]
    Y_λ = D_planet_λ[1]

    S_λ = X_λ**2 / A**2 + Y_λ**2 / B**2

    return S_λ

#############################################################################################################################

#############################################################################################################################

def provjera_sudara(Ta, Tb, ID,
                    Xka, Yka,
                    Xkb, Ykb,
                    V_Xka, V_Yka,
                    V_Xkb, V_Ykb,
                    Xpa, Ypa,
                    Xpb, Ypb,
                    V_Xpa, V_Ypa,
                    V_Xpb, V_Ypb,):
    
    Rka = np.array([Xka, Yka])
    Rkb = np.array([Xkb, Ykb])

    Vka = np.array([V_Xka, V_Yka,])
    Vkb = np.array([V_Xkb, V_Ykb])

    Rpa = np.array([Xpa, Ypa])
    Rpb = np.array([Xpb, Ypb])

    Vpa = np.array([V_Xpa, V_Ypa])
    Vpb = np.array([V_Xpb, V_Ypb])

    Δt = Tb - Ta

    R_planet = R_rječnik[ID]

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

        X_λ = D_planet_λ[0]
        Y_λ = D_planet_λ[1]

        S_λ = X_λ**2 / A**2 + Y_λ**2 / B**2

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