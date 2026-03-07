import kinematika

while True:
    try:
        F = float(input("Unesi silu u N: "))
        m = float(input("Unesi masu u kg: "))

        if m <= 0:
            print("Masa ne smije biti manja ili jednaka 0!")
            continue

        break
    except:
        print("Pogrešan unos!")

kinematika.jednoliko_gibanje(F,m)