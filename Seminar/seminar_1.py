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
t0 = sp.str2et("6 MAY 1950 11:11:11 TDB")

### DEFINIRANJE VREMENSKOG INTERVALA ###
dt = 60*60*2 
N = 7000
t_list = np.arange(t0, t0+N*dt, dt)

### DEFINIRANJE ASTRONOMSKE JEDINICE ###
AU = 149597870.7   #(u km)

### DEFINIRANJE KOMETA ###
x0_komet = -5.0*AU   #(u km)
y0_komet =  0        #(u km)
z0_komet =  0        #(u km)

vx0_komet =  395.6781  #(u km/s)
vy0_komet = -73.2829   #(u km/s)
vz0_komet = -31.7823  #(u km/s)

m_komet = 1.0e14     #(u kg)
R_komet = 11.0       #(u km)