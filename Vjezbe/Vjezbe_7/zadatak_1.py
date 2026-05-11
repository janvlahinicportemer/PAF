import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal ( loc =2.06 , scale =0.05 , size =57) . tolist ()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] #pogreske pri redukciji podataka

k = 10

def histogram(podaci, k):
    
    xmin = min(podaci)
    xmax = max(podaci)

    h = (xmax - xmin) / k

    rubovi = []

    for i in range(k):
        rub = xmin + i*h
        rubovi.append(rub)
    rubovi.append(xmax)

    brojač = [0] * k

    for m in podaci:
        for i in range(k):
            
            if i < k - 1:
                if rubovi[i] <= m < rubovi[i + 1]:
                    brojač[i] = brojač[i] + 1
            else:
                if rubovi[i] <= m <= rubovi[i + 1]:
                    brojač[i] = brojač[i] + 1

    return h, rubovi, brojač

h, rubovi, brojač = histogram(mase_ciste, k)

for i in range(k):
    print(f"[{rubovi[i]}, {rubovi[i+1]}): {brojač[i]}")

plt.figure()
plt.bar(rubovi[:-1], brojač, width=h, align="edge", edgecolor="black")
plt.xlabel("Masa")
plt.ylabel("Frekvencija")
plt.title("Histogram masa Sirius A")
plt.grid(False)
plt.show()