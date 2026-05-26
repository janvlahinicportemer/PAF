from seminar_1 import *
from seminar_2 import *
from scipy.optimize import minimize_scalar, brentq

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

    Rp_x = R_planet[0]
    Rp_y = R_planet[1]
    Rp_z = R_planet[2]

    body_frame = FRAME_rječnik[ID]

    #############################################################################################################################

    def udaljenost_tocka_elipsoid(P, Rp_x, Rp_y, Rp_z):

        X = P[0]
        Y = P[1]
        Z = P[2]

        provjera_unutra = X**2/Rp_x**2 + Y**2/Rp_y**2 + Z**2/Rp_z**2

        if provjera_unutra <= 1:
            return 0

        def F(t):
            return (
                (Rp_x**2 * X**2) / (t + Rp_x**2)**2 +
                (Rp_y**2 * Y**2) / (t + Rp_y**2)**2 +
                (Rp_z**2 * Z**2) / (t + Rp_z**2)**2
                - 1
            )

        t_min = 0
        t_max = max(Rp_x**2, Rp_y**2, Rp_z**2)

        while F(t_max) > 0:
            t_max = 2*t_max

        t = brentq(F, t_min, t_max)

        Qx = Rp_x**2 * X / (t + Rp_x**2)
        Qy = Rp_y**2 * Y / (t + Rp_y**2)
        Qz = Rp_z**2 * Z / (t + Rp_z**2)

        d = np.sqrt((X - Qx)**2 + (Y - Qy)**2 + (Z - Qz)**2)

        return d

    #############################################################################################################################

    def D(λ):

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

        udaljenost = udaljenost_tocka_elipsoid(D_planet_λ, Rp_x, Rp_y, Rp_z)

        return udaljenost

    #############################################################################################################################

    rezultat = minimize_scalar(D, bounds=(0, 1), method="bounded")

    λ_min = rezultat.x
    d_min = rezultat.fun

    t_sudar = Ta + λ_min * (Tb - Ta)

    if d_min <= R_komet:
        return True, t_sudar

    else:
        return False, None