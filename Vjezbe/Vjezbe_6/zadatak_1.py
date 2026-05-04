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

print("Valjak broj 1:")
print(f"R = ({aritmeticka_sredina(V1_2R/2)} ± {standardna_devijacija(V1_2R/2)}) mm")
print(f"L = ({aritmeticka_sredina(V1_L)} ± {standardna_devijacija(V1_L)}) mm")
print(f"m = ({aritmeticka_sredina(V1_m)} ± {standardna_devijacija(V1_m)}) g")

print("\nValjak broj 2:")
print(f"R = ({aritmeticka_sredina(V2_2R/2)} ± {standardna_devijacija(V2_2R/2)}) mm")
print(f"L = ({aritmeticka_sredina(V2_L)} ± {standardna_devijacija(V2_L)}) mm")
print(f"m = ({aritmeticka_sredina(V2_m)} ± {standardna_devijacija(V2_m)}) g")

print("\nValjak broj 3:")
print(f"R = ({aritmeticka_sredina(V3_2R/2)} ± {standardna_devijacija(V3_2R/2)}) mm")
print(f"L = ({aritmeticka_sredina(V3_L)} ± {standardna_devijacija(V3_L)}) mm")
print(f"m = ({aritmeticka_sredina(V3_m)} ± {standardna_devijacija(V3_m)}) g")