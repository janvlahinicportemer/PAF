import math
import matplotlib.pyplot as plt
from particle import Particle

dt_values = [0.5, 0.1, 0.05, 0.01, 0.005, 0.001]
domet_numerički_list = []
abs_err_list = []
rel_err_list = []

V0 = 10
θ = 60
X0 = 0
Y0 = 0

g = 9.81
θ_radian = math.radians(θ)

p = Particle(V0, θ, X0, Y0)

domet_analitički = (V0**2 * math.sin(2 * θ_radian)) / g

for i in range(len(dt_values)):
    
    dt = dt_values[i]

    domet_numerički = p.range(dt)
    domet_numerički_list.append(domet_numerički)

    abs_err = abs(domet_numerički - domet_analitički)
    abs_err_list.append(abs_err)

    rel_err = (abs_err / domet_analitički) * 100
    rel_err_list.append(rel_err)

plt.figure()
plt.plot(dt_values, rel_err_list)
plt.xlabel("Δt (s)")
plt.ylabel("relativna pogreška (%)")
plt.title("Ovisnost relativne pogreške o vremenskom koraku Δt")
plt.grid(True)
plt.show()