import numpy as np
import matplotlib.pyplot as plt

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336]) #(u Nm)
φ = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]) #(u rad)

# M = Dt * φ, y = a*x

def a(M, φ):

    a = np.mean(M*φ)/np.mean(φ**2) 

    return a

def sigma_a(M, φ):

    sigma_a = np.sqrt((1/len(M))*((np.mean(M**2)/np.mean(φ**2) - a(M, φ)**2)))

    return sigma_a

Dt_mean = a(M, φ)
σ_a = sigma_a(M, φ)

print (f"a = ({Dt_mean} ± {σ_a})Nm/rad")

plt.figure()
plt.scatter(φ, M, label="Mjerenja", color="red")
plt.plot(φ, Dt_mean * φ, label="Regresija", color="green")
plt.xlabel("φ (rad)")
plt.ylabel("M (Nm)")
plt.title("Linearna regresija")
plt.grid(True)
plt.legend()
plt.show()