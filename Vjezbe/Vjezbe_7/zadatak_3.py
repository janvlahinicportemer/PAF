import numpy as np

np.random.seed(42)
mase_ciste = np.random.normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] #pogreske pri redukciji podataka

a = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6] # paran n
b = [3 , 1 , 4 , 1 , 5 , 9 , 2 , 6 , 5] # neparan n

def medijan(podaci):

    podaci_sortirani = sorted(podaci)

    n = len(podaci_sortirani)

    if n % 2 != 0:
        medijan = podaci_sortirani[n // 2]

    else:
        medijan = (podaci_sortirani[n // 2 - 1] + podaci_sortirani[n // 2]) / 2

    return medijan

medijan_a = medijan(a)
medijan_b = medijan(b)
medijan_m = medijan(mase)

print(f"Medijan za a (ručno): {np.round(medijan_a, 2)}")
print(f"Medijan za a (numpy): {np.round(np.median(a), 2)}\n")

print(f"Medijan za b (ručno): {np.round(medijan_b, 2)}")
print(f"Medijan za b (numpy): {np.round(np.median(b), 2)}\n")

print(f"Medijan za mase (ručno): {np.round(medijan_m, 2)}")
print(f"Medijan za mase (numpy): {np.round(np.median(mase), 2)}")