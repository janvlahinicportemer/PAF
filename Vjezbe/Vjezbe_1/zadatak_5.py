import matplotlib.pyplot as plt

k1 = ["X", "Y", "X", "Y"]
k2 = ["prve", "prve", "druge", "druge"]
k3 = ["X1", "Y1", "X2", "Y2"]
v = []

for i in range (4):
  while True:
    try:
      v.append(float(input(f"Unesi {k1[i]} koordinatu {k2[i]} točke ({k3[i]}): ")))
      break
    except:
      print ("Pogrešan unos!")

def f(x1, y1, x2, y2):
    if x1==x2:
        W = f"x = {x1}"
    elif y1==y2:
        W = f"y = {y1}"
    else:
        K = round((y2-y1)/(x2-x1), 2)
        N = round(y2 - K*x2, 2)
        if N < 0:
            W = f"y = {K}x - {abs(N)}"
        elif N > 0:
            W = f"y = {K}x + {abs(N)}"
        else:
            W = f"y = {K}x"
    return print (f"Jednadžba pravca u eksplicitnom obliku: {W}")

f(v[0], v[1], v[2], v[3])

plt.scatter((v[0], v[2]), (v[1], v[3]))
plt.axline((v[0], v[1]), (v[2], v[3]))
plt.show()