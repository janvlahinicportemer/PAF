import numpy as np

V1_2R = np.array([19.98, 20.18, 20.10, 20.08, 19.74])
V2_2R = np.array([19.92, 19.82, 19.96, 19.98, 19.88])
V3_2R = np.array([24.96, 24.98, 24.98, 24.92, 24.94])

V1_L = np.array([49.80, 49.00, 50.48, 49.80, 49.96])
V2_L = np.array([52.56, 52.50, 52.62, 52.58, 52.54])
V3_L = np.array([55.34, 55.40, 55.30, 55.44, 55.48])

V1_m = np.array([138.92, 138.98, 139.20, 138.90, 138.92])
V2_m = np.array([128.65, 128.60, 128.65, 128.35, 128.50])
V3_m = np.array([71.89, 71.90, 71.79, 71.85, 71.70])

def aritmeticka_sredina(x_list):

    x = 0
    for i in range(len(x_list)):
        x = x + x_list[i]
    x = x / len(x_list)

    return x

def standardna_devijacija(x_list):

    x = 0
    x_s = aritmeticka_sredina(x_list)

    for i in range(len(x_list)):
        x = x + (x_list[i]-x_s)**2
    x = x / (len(x_list)*(len(x_list)-1))
    x = np.sqrt(x)

    return x

def volumen_valjka(R, L):

    R_mean = np.mean(R)

    L_mean = np.mean(L)

    V_mean = np.pi * R_mean**2 * L_mean

    return V_mean

def sigma_volumen(R, sigma_R, L, sigma_L):

    R_mean = np.mean(R)

    L_mean = np.mean(L)

    sigma_V = np.sqrt((2 * np.pi * R_mean * L_mean * sigma_R)**2 + (np.pi * R_mean**2 * sigma_L)**2)

    return sigma_V

print("Valjak broj 1:")
print(f"V = ({volumen_valjka(V1_2R/2/10, V1_L/10):e} ± {sigma_volumen(V1_2R/2/10, standardna_devijacija(V1_2R/2)/10, V1_L/10, standardna_devijacija(V1_L)/10):e}) cm^3")

print("\nValjak broj 2:")
print(f"V = ({volumen_valjka(V2_2R/2/10, V2_L/10):e} ± {sigma_volumen(V2_2R/2/10, standardna_devijacija(V2_2R/2)/10, V2_L/10, standardna_devijacija(V2_L)/10):e}) cm^3")

print("\nValjak broj 3:")
print(f"V = ({volumen_valjka(V3_2R/2/10, V3_L/10):e} ± {sigma_volumen(V3_2R/2/10, standardna_devijacija(V3_2R/2)/10, V3_L/10, standardna_devijacija(V3_L)/10):e}) cm^3")