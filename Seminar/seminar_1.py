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
t0 = sp.str2et("1 JUNE 2026 00:00:00 TDB")

### DEFINIRANJE VREMENSKOG INTERVALA ###
dt = 60*60*2 
N = 7000
t_list = np.arange(t0, t0+N*dt, dt)

### DEFINIRANJE ASTRONOMSKE JEDINICE ###
AU = 149597870.7   #(u km)

### DEFINIRANJE KOMETA ###
x0_komet =  -6*AU    #(u km)
y0_komet =  -1*AU    #(u km)
z0_komet =  0        #(u km)

vx0_komet = 16     #(u km/s)
vy0_komet = 0      #(u km/s)
vz0_komet = 0      #(u km/s)

m_komet = 1.0e14     #(u kg)
R_komet = 11.0       #(u km)