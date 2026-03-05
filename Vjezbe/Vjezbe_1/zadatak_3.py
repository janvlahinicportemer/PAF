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

if v[0]==v[2]:
  print (f"x={v[0]}")
elif v[1]==v[3]:
  print (f"y={v[1]}")
else:
  K = round((v[3]-v[1])/(v[2]-v[0]), 2)
  N = round(v[3] - K*v[2], 2)
  if N < 0:
    print (f"Jednadžba pravca u eksplicitnom obliku: y={K}x - {abs(N)}")
  elif N > 0:
    print (f"Jednadžba pravca u eksplicitnom obliku: y={K}x + {abs(N)}")
  else:
    print (f"Jednadžba pravca u eksplicitnom obliku: y={K}x")