from seminar_1 import *
from seminar_2 import *
from seminar_3 import *
from RK4 import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x_min = np.min(M_mnp[:, :, 1]) - 1*AU
x_max = np.max(M_mnp[:, :, 1]) + 1*AU

y_min = np.min(M_mnp[:, :, 2]) - 1*AU
y_max = np.max(M_mnp[:, :, 2]) + 1*AU

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

ax.set_xlabel("x [km]")
ax.set_ylabel("y [km]")
ax.set_title("Animacija gibanja kometa u heliocentričnom sustavu")
ax.grid(False)

ax.plot(M_mnp[:, 0, 1], M_mnp[:, 0, 2], linewidth=1)

tocka_komet, = ax.plot([], [], "o", markersize=6, label="KOMET")

def update(frame):
    tocka_komet.set_data([M_mnp[frame, 0, 1]], [M_mnp[frame, 0, 2]])
    return tocka_komet,

animacija = FuncAnimation(
    fig,
    update,
    frames=range(0, len(t_list), 1),
    interval=1,
    blit=True
)

ax.legend()
plt.show()