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

### DEFINIRANJE POČETNOG TRENUTKA ###
t0 = sp.str2et("2025 APR 24 07:58:51 TDB")

### DEFINIRANJE VREMENSKOG INTERVALA ###
dt = 60*60*2
N = 7500
t_list = np.arange(t0, t0+N*dt, dt)

### DEFINIRANJE ASTRONOMSKE JEDINICE ###
AU = 149597870.7   #(u km)

### DEFINIRANJE KOMETA ###
x0_komet = -958284977.8292934      #(u km)
y0_komet = +525432299.72381735     #(u km)

vx0_komet = +19.781650541790206    #(u km/s)
vy0_komet = -17.92779218156617     #(u km/s)

m_komet = 1.0e14     #(u kg)
R_komet = 11.0       #(u km)