import numpy as np
import spiceypy as sp

### UČITAVANJE DATOTEKA ###
sp.furnsh("de442.bsp")
sp.furnsh("mar097.bsp")
sp.furnsh("gm_de440.tpc")
sp.furnsh("pck00011.tpc")
sp.furnsh("naif0012.tls")

### DEFINIRANJE REFERENTNOG SUSTAVA ###
referentni_sustav = "J2000"
ishodište = "SUN"
abcorr = "NONE"

### DEFINIRANJE PROMATRAČA ###
promatrač = "EARTH"

### DEFINIRANJE TRENUTKA SUDARA ZEMLJE I KOMETA###
t_sudar = sp.str2et("15 JUNE 2026 00:00:00 TDB")

### DEFINIRANJE VREMENSKOG INTERVALA ###
dt = 60*60*2
N = 5000
dt_unazad = -dt

### DEFINIRANJE ASTRONOMSKE JEDINICE ###
AU = 149597870.7   #(u km)

### DEFINIRANJE KOMETA ###
state_vector_earth, _ = sp.spkezr("399", t_sudar, referentni_sustav, abcorr, ishodište)
xE, yE, _, vxE, vyE, _ = state_vector_earth

r_komet = np.array([xE, yE]) #(u km); x0_komet=xE; y0_komet=yE

v_komet = np.array([vxE + 20, vyE + 0]) #(u km/s); vx0_komet=vxE+vx_rel;  vy0_komet=vyE+vy_rel

m_komet = 1.0e14     #(u kg)
R_komet = 11.0       #(u km)

####################################################################################################################################################################################

ID_list = [
    199,  # MERKUR
    299,  # VENERA
    399,  # ZEMLJA
    499,  # MARS
    10]   # SUNCE

IME_rječnik = {}
GM_rječnik = {} #(u km^3/s^2)
R_rječnik = {} #(u km)
ID_valid_list = []

for i, ID in enumerate(ID_list):
    
    try:
        ime = sp.bodc2n(ID)
        IME_rječnik[ID_list[i]] = ime
    
    except:
        IME_rječnik[ID_list[i]] = "UNKNOWN"

######################################################################################

for ID in ID_list:
    
    try:
        GM = sp.bodvrd(str(ID), "GM", 1)[1][0]
        GM_rječnik[ID] = GM
    
    except:
        GM_rječnik[ID] = "UNKNOWN"

######################################################################################

for i, ID in enumerate(ID_list):
    
    try:
        R = sp.bodvrd(str(ID), "RADII", 3)[1]
        R_rječnik[ID_list[i]] = np.mean([R[0], R[1]])
    
    except:
        R_rječnik[ID_list[i]] = "UNKNOWN"

######################################################################################

for i, ID in enumerate(ID_list):

    if not isinstance(GM_rječnik[ID], str) and not isinstance(R_rječnik[ID], str):
        ID_valid_list.append(ID)

####################################################################################################################################################################################

def akceleracija(t, r_komet):

    ax_total = 0.0
    ay_total = 0.0

    x_komet = r_komet[0]
    y_komet = r_komet[1]

    for ID in ID_valid_list:

        state_vector, _ = sp.spkezr(str(ID), t, referentni_sustav, abcorr, ishodište)

        x = state_vector[0]
        y = state_vector[1]

        dx = x - x_komet
        dy = y - y_komet

        R = np.sqrt(dx**2 + dy**2)

        GM = GM_rječnik[ID]

        ax_total += GM * dx / R**3
        ay_total += GM * dy / R**3

    return np.array([ax_total, ay_total])

def F(t, Y):

    r = Y[0:2]
    v = Y[2:4]

    a = akceleracija(t, r)

    return np.array([v[0], v[1], a[0], a[1]])

def RK4(t_old, dt, r_old, v_old):

    Y_old = np.array([r_old[0], r_old[1], v_old[0], v_old[1]])

    k1 = F(t_old, Y_old)
    k2 = F(t_old + dt/2, Y_old + dt*k1/2)
    k3 = F(t_old + dt/2, Y_old + dt*k2/2)
    k4 = F(t_old + dt, Y_old + dt*k3)

    Y_new = Y_old + dt/6 * (k1 + 2*k2 + 2*k3 + k4)

    return Y_new

t = t_sudar

for i in range(N):

    Y_new = RK4(t, dt_unazad, r_komet, v_komet)

    r_komet = Y_new[0:2]
    v_komet = Y_new[2:4]

    t = t + dt_unazad

x0_komet = r_komet[0]
y0_komet = r_komet[1]

vx0_komet = v_komet[0]
vy0_komet = v_komet[1]

v0_komet = np.sqrt(vx0_komet**2 + vy0_komet**2)

r0_km = np.sqrt(x0_komet**2 + y0_komet**2)
r0_AU = r0_km / AU

vrijeme_pocetka = sp.et2utc(t, "C", 0)

print("PODACI ZA ORIGINALNI KOD")
print("t0 =", vrijeme_pocetka)
print("x0_komet =", x0_komet)
print("y0_komet =", y0_komet)
print("vx0_komet =", vx0_komet)
print("vy0_komet =", vy0_komet)

if v0_komet > 15:
    print("BRZINA OK: v0 > 15 km/s")
else:
    print("BRZINA NIJE OK: v0 <= 15 km/s")

if r0_AU > 4:
    print("UDALJENOST OK: r0 > 4 AU")
else:
    print("UDALJENOST NIJE OK: r0 <= 4 AU")