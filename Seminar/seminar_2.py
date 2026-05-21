from seminar_1 import *

### UČITAVANJE KONSTANTNIH PODATAKA ###
ID_list = [
    1,    # MERKUR
    2,    # VENERA
    3,    # ZEMLJA
    10]   # SUNCE

ID_list_2 = [199, 299, 399, 10]

IME_rječnik = {}
GM_rječnik = {} #(u km^3/s^2)
R_rječnik = {} #(u km)
ID_valid_list = []

######################################################################################

for i, ID in enumerate(ID_list_2):
    
    try:
        ime = sp.bodc2n(ID)
        IME_rječnik[ID_list[i]] = ime
    
    except:
        IME_rječnik[ID_list[i]] = "UNKNOWN"

######################################################################################

for ID in ID_list:
    
    try:
        GM = sp.bodvrd(str(ID), "GM", 1)[1][0]
        GM_rječnik[ID] = GM
    
    except:
        GM_rječnik[ID] = "UNKNOWN"

######################################################################################

for i, ID in enumerate(ID_list_2):
    
    try:
        R = sp.bodvrd(str(ID), "RADII", 3)[1]
        R_rječnik[ID_list[i]] = np.max(R[:2])
    
    except:
        R_rječnik[ID_list[i]] = "UNKNOWN"

######################################################################################

for ID in ID_list:

    if not isinstance(GM_rječnik[ID], str) and not isinstance(R_rječnik[ID], str):
        ID_valid_list.append(ID)

######################################################################################