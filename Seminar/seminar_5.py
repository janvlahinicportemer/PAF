from seminar_1 import *
from seminar_2 import *
from seminar_3 import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

linije = []
tocke = []

fig, ax = plt.subplots(figsize=(8, 8))

imena = ["KOMET"] + [IME_rječnik[ID] for ID in ID_valid_list]

for ime in imena:

    linija, = ax.plot([], [], lw=1.5, label=ime)
    boja = linija.get_color()

    tocka, = ax.plot([], [], "o", markersize=6, color=boja)

    linije.append(linija)
    tocke.append(tocka)

x_min = np.nanmin(M_mnp[0:i_kraj+1, :, 1]) - AU
x_max = np.nanmax(M_mnp[0:i_kraj+1, :, 1]) + AU
y_min = np.nanmin(M_mnp[0:i_kraj+1, :, 2]) - AU
y_max = np.nanmax(M_mnp[0:i_kraj+1, :, 2]) + AU

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect("equal")
ax.set_xlabel("x [km]")
ax.set_ylabel("y [km]")
ax.set_title("Animacija gibanja kometa i planeta u heliocentričnom sustavu")
ax.grid(False)
ax.legend(loc="upper right")

rep = 1000
preskok = 1

def update(frame):
    for k in range(len(imena)):
        pocetak = max(0, frame - rep)

        x = M_mnp[pocetak:frame+1, k, 1]
        y = M_mnp[pocetak:frame+1, k, 2]

        linije[k].set_data(x, y)
        tocke[k].set_data([M_mnp[frame, k, 1]], [M_mnp[frame, k, 2]])

    return linije + tocke

ani = FuncAnimation(
    fig,
    update,
    frames=range(1, i_kraj + 1, preskok),
    interval=1,
    blit=True,
    repeat=False
)

ani.save(
    "animacija_gibanja.mp4",
    writer="ffmpeg",
    fps=60,
    dpi=200
)

plt.show()