from seminar_1 import *
from seminar_2 import *
from seminar_3 import *
from RK4 import *
import matplotlib.pyplot as plt




### ODREĐIVANJE ZADNJEG POPUNJENOG INDEKSA ###
if sudar:
    zadnji_i = i
else:
    zadnji_i = len(t_list) - 1

### CRTANJE PUTANJA U x-y RAVNINI ###
plt.figure(figsize=(10, 10), facecolor="black")
ax = plt.gca()
ax.set_facecolor("black")

### PUTANJA KOMETA ###
plt.plot(
    M_mnp[:zadnji_i+1, 0, 1],
    M_mnp[:zadnji_i+1, 0, 2],
    color="white",
    linewidth=1.5,
    label="Komet"
)

plt.scatter(
    M_mnp[zadnji_i, 0, 1],
    M_mnp[zadnji_i, 0, 2],
    color="white",
    s=35
)

### PUTANJE PLANETA I SUNCA ###
for j, ID in enumerate(ID_valid_list):

    if ID == 10:
        boja = "yellow"
    else:
        boja = None

    plt.plot(
        M_mnp[:zadnji_i+1, j+1, 1],
        M_mnp[:zadnji_i+1, j+1, 2],
        linewidth=1.0,
        label=IME_rječnik[ID],
        color=boja
    )

    plt.scatter(
        M_mnp[zadnji_i, j+1, 1],
        M_mnp[zadnji_i, j+1, 2],
        s=35,
        color=boja
    )

### UREĐIVANJE GRAFA ###
plt.xlabel("x [km]", color="white")
plt.ylabel("y [km]", color="white")
plt.title("Putanje kometa, planeta i Sunca u x-y ravnini", color="white")

plt.xticks(color="white")
plt.yticks(color="white")

for spine in ax.spines.values():
    spine.set_color("white")

plt.grid(False)
plt.axis("equal")
plt.legend(facecolor="black", edgecolor="white", labelcolor="white")

plt.show()