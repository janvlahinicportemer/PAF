import numpy as np
import matplotlib.pyplot as plt

h0 = 0.54 # m
m = 0.5257 # kg
r = 4.025e-3 # m
g = 9.81 #m/s^2

h_list = [0.14 , 0.17 , 0.19 , 0.22 , 0.25 , 0.28 , 0.31 , 0.34 , 0.37 , 0.40] # m
t_mean_list = [1.740 , 1.793 , 2.043 , 2.190 , 2.280 , 2.417 , 2.540 , 2.640 , 2.670 , 2.813] # s

n = len(h_list)

y_list = []
x_list = []

for i in range(n):
    y_list.append(np.log(h_list[i]))
    x_list.append(np.log(t_mean_list[i]))

x = np.array(x_list)
y = np.array(y_list)

a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
b = (np.sum(y) - a * np.sum(x)) / n

sigma_a = np.sqrt((1 / (n - 2)) * ((n * np.sum(y**2) - (np.sum(y))**2) / (n * np.sum(x**2) - (np.sum(x))**2) - a**2))
sigma_b = sigma_a * np.sqrt((1 / n) * np.sum(x**2))

print("\na)")
print(f"a = ({np.round(a, 1)} ± {np.round(sigma_a, 1)}) ")
print(f"b = ({np.round(b, 2)} ± {np.round(sigma_b, 2)})")

x_fit = np.linspace(min(x), max(x), 1000)
y_fit = a * x_fit + b

plt.figure()
plt.scatter(x, y, color="red", label="Eksperimentalni podaci")
plt.plot(x_fit, y_fit, color="green", label=f"Linearna regresija: y = {np.round(a, 1)}x + {np.round(b, 2)}")
plt.xlabel("log(t)")
plt.ylabel("log(s)")
plt.title("Linearna regresija: log(s) - log(t)")
plt.grid(True)
plt.legend()
plt.show()

##########################################################################################################################################################

y_list_2 = []
x_list_2 = []

for i in range(n):
    y_list_2.append(h_list[i])
    x_list_2.append(t_mean_list[i]**2)

x_2 = np.array(x_list_2)
y_2 = np.array(y_list_2)

a_2 = (n * np.sum(x_2 * y_2) - np.sum(x_2) * np.sum(y_2)) / (n * np.sum(x_2**2) - (np.sum(x_2))**2)
b_2 = (np.sum(y_2) - a_2 * np.sum(x_2)) / n

sigma_a_2 = np.sqrt((1 / (n - 2)) * ((n * np.sum(y_2**2) - (np.sum(y_2))**2) / (n * np.sum(x_2**2) - (np.sum(x_2))**2) - a_2**2))
sigma_b_2 = sigma_a_2 * np.sqrt((1 / n) * np.sum(x_2**2))

print("\nb)")
print(f"a = ({np.round(a_2, 3)} ± {np.round(sigma_a_2, 3)}) m/s²")
print(f"b = ({np.round(b_2, 2)} ± {np.round(sigma_b_2, 2)}) m")

x_fit_2 = np.linspace(min(x_2), max(x_2), 1000)
y_fit_2 = a_2 * x_fit_2 + b_2

plt.figure()
plt.scatter(x_2, y_2, color="red", label="Eksperimentalni podaci")
plt.plot(x_fit_2, y_fit_2, color="green", label=f"Linearna regresija: s = {np.round(a_2, 3)}t² + {np.round(b_2, 3)}")
plt.xlabel("t² [s²]")
plt.ylabel("s [m]")
plt.title("Linearna regresija: s - t²")
plt.grid(True)
plt.legend()
plt.show()

##########################################################################################################################################################

a_ef = 2 * a_2
sigma_a_ef = 2 * sigma_a_2

I_z = (m * g * r**2) / a_ef - m * r**2
sigma_I_z = (m * g * r**2 / a_ef**2) * sigma_a_ef

print("\nc)")
print(f"Iz = ({np.round(I_z*1e4, 1)} ± {np.round(sigma_I_z*1e4, 1)}) × 10⁻⁴ kgm²\n")

##########################################################################################################################################################