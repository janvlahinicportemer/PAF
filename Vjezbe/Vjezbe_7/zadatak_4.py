import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] #pogreske pri redukciji podataka

def medijan(podaci):

    podaci_sortirani = sorted(podaci)

    n = len(podaci_sortirani)

    if n % 2 != 0:
        medijan = podaci_sortirani[n // 2]

    else:
        medijan = (podaci_sortirani[n // 2 - 1] + podaci_sortirani[n // 2]) / 2

    return medijan

aritmeticka_sredina_m = np.mean(mase)
medijan_m = medijan(mase)

relativna_pogreska = abs((aritmeticka_sredina_m - medijan_m) / medijan_m) * 100

print(f"Aritmetička sredina: {np.round(aritmeticka_sredina_m, 2)}")
print(f"Medijan: {np.round(medijan_m, 2)}")
print(f"Relativna pogreška: {np.round(relativna_pogreska, 2)} %")

aritmeticka_sredina_mase_ciste= np.mean(mase_ciste)
medijan_mase_ciste = medijan(mase_ciste)

relativna_pogreska_mase_ciste = abs((aritmeticka_sredina_mase_ciste - medijan_mase_ciste) / medijan_mase_ciste) * 100

print("\nBez pogrešnih mjerenja:")
print(f"Aritmetička sredina: {np.round(aritmeticka_sredina_mase_ciste, 2)}")
print(f"Medijan: {np.round(medijan_mase_ciste, 3)}")
print(f"Relativna pogreška: {np.round(relativna_pogreska_mase_ciste, 3)} %")

plt.figure()
plt.hist(mase, bins=10, edgecolor="black")
plt.axvline(aritmeticka_sredina_m, color="blue", linestyle="--", linewidth=3, alpha=0.8, label="Aritmetička sredina mase")
plt.axvline(medijan_m, color="red", linestyle="-.", linewidth=3, alpha=0.8, label="Medijan mase")
plt.axvline(aritmeticka_sredina_mase_ciste, color="green", linestyle=":", linewidth=5, alpha=0.9, label="Aritmetička sredina mase_ciste")
plt.axvline(medijan_mase_ciste, color="orange", linestyle="-", linewidth=2, alpha=0.8, label="Medijan mase_ciste")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Histogram masa Sirius A")
plt.grid(False)
plt.legend()
plt.show()

plt.figure()
plt.hist(mase_ciste, bins=10, edgecolor="black")
plt.axvline(aritmeticka_sredina_m, color="blue", linestyle="--", label="Aritmetička sredina mase")
plt.axvline(medijan_m, color="red", linestyle="-.", label="Medijan mase")
plt.axvline(aritmeticka_sredina_mase_ciste, color="green", linestyle=":", label="Aritmetička sredina mase_ciste")
plt.axvline(medijan_mase_ciste, color="orange", linestyle="-", label="Medijan mase_ciste")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Histogram masa Sirius A")
plt.grid(False)
plt.legend()
plt.show()