from seminar_1 import *
from seminar_2 import *
from seminar_3 import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(8, 8))

imena = ["KOMET"] + [IME_rječnik[ID] for ID in ID_valid_list]

linije = []
tocke = []

for k, ime in enumerate(imena):

    if k > 0 and ID_valid_list[k - 1] == 10:
        boja = "gold"
        velicina_tocke = 9
        debljina_linije = 1.2
    else:
        boja = None
        velicina_tocke = 5
        debljina_linije = 1.5

    linija, = ax.plot([], [], lw=debljina_linije, label=ime, color=boja)
    boja_linije = linija.get_color()

    tocka, = ax.plot([], [], "o", markersize=velicina_tocke, color=boja_linije)

    linije.append(linija)
    tocke.append(tocka)

M_anim = M_mnp[0:i_kraj + 1, :, :]

x_min = np.nanmin(M_anim[:, :, 1]) - AU
x_max = np.nanmax(M_anim[:, :, 1]) + AU
y_min = np.nanmin(M_anim[:, :, 2]) - AU
y_max = np.nanmax(M_anim[:, :, 2]) + AU

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel("x [km]")
ax.set_ylabel("y [km]")
ax.set_title("Animacija gibanja kometa i planeta u heliocentričnom sustavu")
ax.grid(False)
ax.legend(loc="upper right")

tekst_vrijeme = ax.text(0.02, 0.02, "", transform=ax.transAxes)

rep = 1000
preskok = 1

frames = list(range(0, i_kraj + 1, preskok))

if len(frames) == 0:
    frames = [0]


def init():
    for k in range(len(imena)):
        linije[k].set_data([], [])
        tocke[k].set_data([], [])

    tekst_vrijeme.set_text("")
    return linije + tocke + [tekst_vrijeme]


def update(frame):

    pocetak = max(0, frame - rep)

    for k in range(len(imena)):

        x = M_mnp[pocetak:frame + 1, k, 1]
        y = M_mnp[pocetak:frame + 1, k, 2]

        linije[k].set_data(x, y)
        tocke[k].set_data([M_mnp[frame, k, 1]], [M_mnp[frame, k, 2]])

    try:
        tekst_vrijeme.set_text("UTC: " + sp.et2utc(t_list[frame], "C", 0))
    except Exception:
        tekst_vrijeme.set_text(f"frame = {frame}")

    return linije + tocke + [tekst_vrijeme]


ani = FuncAnimation(fig,
                    update,
                    init_func=init,
                    frames=frames,
                    interval=20,
                    blit=True,
                    repeat=False)
                    
ani.save("animacija.mp4", writer="ffmpeg", fps=30)

plt.show()