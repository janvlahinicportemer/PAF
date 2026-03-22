import math
import numpy as np
from particle import Particle

V0 = 10
θ = 45
X0 = 0
Y0 = 0

g = 9.81

p = Particle(V0, θ, X0, Y0)

domet_numerički = p.range()

θ_radian = math.radians(θ)
domet_analitički = (V0**2 * math.sin(2 * θ_radian)) / g

abs_err  = abs(domet_numerički - domet_analitički)
rel_err = (abs_err / domet_analitički) * 100

print("Numerički domet:", np.round(domet_numerički, 4), "m")
print("Analitički domet:", np.round(domet_analitički, 4), "m")
print("Apsolutna pogreška:", np.round(abs_err, 4), "m")
print("Relativna pogreška:", np.round(rel_err, 4), "%")

p.plot_trajectory()
p.reset()