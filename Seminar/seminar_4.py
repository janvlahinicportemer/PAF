from RK4 import *
from seminar_1 import *
from seminar_2 import *
from seminar_3 import *
from provjera_sudara import *
import matplotlib.pyplot as plt

plt.figure()

plt.plot(M_mnp[0:i_kraj+1, 0, 1], M_mnp[0:i_kraj+1, 0, 2])
plt.scatter(M_mnp[i_kraj, 0, 1], M_mnp[i_kraj, 0, 2], s=25, label="KOMET")

for i, ID in enumerate(ID_valid_list):

    if ID == 10:
        color = "yellow"
        size = 100
    else:
        color = None
        size = 50

    plt.plot(M_mnp[0:i_kraj+1, i+1, 1], M_mnp[0:i_kraj+1, i+1, 2], color=color)
    plt.scatter(
        M_mnp[i_kraj, i+1, 1],
        M_mnp[i_kraj, i+1, 2],
        s=size,
        label=f"{IME_rječnik[ID]}",
        color=color
    )

x_min = np.min(M_mnp[0:i_kraj+1, :, 1]) - 1*AU
x_max = np.max(M_mnp[0:i_kraj+1, :, 1]) + 1*AU

y_min = np.min(M_mnp[0:i_kraj+1, :, 2]) - 1*AU
y_max = np.max(M_mnp[0:i_kraj+1, :, 2]) + 1*AU

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.xlabel("x [km]")
plt.ylabel("y [km]")
plt.title("Putanje kometa i planeta u heliocentričnom sustavu")
plt.grid(False)
plt.legend()

plt.savefig("IMG_putanje.jpg", dpi=300, bbox_inches="tight")

plt.show()