import calculus
import math
from sympy import symbols, sympify, diff, lambdify
import matplotlib.pyplot as plt

x = float(input("Unesi x: "))
a = float(input("Unesi a: "))
b = float(input("Unesi b: "))
ε = float(input("Unesi ε: "))
ε1 = float(input("Unesi ε1: "))
ε2 = float(input("Unesi ε2: "))
ε3 = float(input("Unesi ε3: "))
method = input("Želiš li koristiti two-step metodu (DA/NE):")

izraz = input(
    "Unesi funkciju f(x)\n "
    "Npr. x**(n), x**(1/n), sqrt(x), "
    "sin(x), cos(x), tg(x), ctg(x), "
    "sh(x), ch(x), th(x), ctgh(x), "
    "arcsin(x), arccos(x), arctg(x), arcctg(x), "
    "arsh(x), arch(x), arth(x), arcctgh(x), "
    "log(x, b), ln(x), exp(x), a**(x), "
    "abs(x), (konst.; pi, e)\n "
    "f(x) = ")

def f(x):

    f = eval(izraz, {
        "x": x,
        "abs": abs, 
        "sin": math.sin,
        "cos": math.cos,
        "tg": math.tan,
        "tan": math.tan,
        "ctg": ctg,
        "sh": math.sinh,
        "ch": math.cosh,
        "th": math.tanh,
        "ctgh": ctgh,
        "arcsin": math.asin,
        "arccos": math.acos,
        "arctg": math.atan,
        "arcctg": arcctg,
        "arsh": math.asinh,
        "arch": math.acosh,
        "arth": math.atanh,
        "arcctgh": arcctgh,
        "log": math.log,
        "ln": math.log,
        "exp": math.exp,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e})

    return f

def ctg(x):

    f = 1 / math.tan(x)

    return f

def ctgh(x):

    f = 1 / math.tanh(x)

    return f

def arcctg(x):

    f = math.atan(1 / x)

    return f

def arcctgh(x):

    f = 0.5 * math.log((x + 1) / (x - 1)) 

    return f

##################################################################################################################################################################

def der_analiticki(x):

    x_sym = symbols('x')
    expr = sympify(izraz)
    expr_der = diff(expr, x_sym)
    der_f_a = lambdify(x_sym, expr_der, "math")

    return der_f_a(x)

##################################################################################################################################################################

if method == "DA":

    print("\n test 1 \n")
    print(f"f'({x}) = {calculus.deriviranje_u_tocki(f, x, ε, 'two-step')}")

else:

    print("\n test 1 \n")
    print(f"f'({x}) = {calculus.deriviranje_u_tocki(f, x, ε)}")

##################################################################################################################################################################

if method == "DA":

    print("\n test 2 \n")
    x1, y1 = calculus.deriviranje_na_intervalu(f, a, b, ε, 'two-step')
    
    print(f"Točke: {[round(x, 2) for x in x1]}")
    print(f"Derivacije: {[round(y, 2) for y in y1]}")

else:

    print("\n test 2 \n")
    x1, y1 = calculus.deriviranje_na_intervalu(f, a, b, ε)
    
    print(f"Točke: {[round(x, 2) for x in x1]}")
    print(f"Derivacije: {[round(y, 2) for y in y1]}")

##################################################################################################################################################################

if method == "DA":

    x1, y1 = calculus.deriviranje_na_intervalu(f, a, b, ε1, 'two-step')
    x2, y2 = calculus.deriviranje_na_intervalu(f, a, b, ε2, 'two-step')
    x3, y3 = calculus.deriviranje_na_intervalu(f, a, b, ε3, 'two-step')

    y_analiticki = []

    for x in (x1):

        der = der_analiticki(x)
        y_analiticki.append(der)

else:

    x1, y1 = calculus.deriviranje_na_intervalu(f, a, b, ε1)
    x2, y2 = calculus.deriviranje_na_intervalu(f, a, b, ε2)
    x3, y3 = calculus.deriviranje_na_intervalu(f, a, b, ε3)

    y_analiticki = []

    for x in (x1):

        der = der_analiticki(x)
        y_analiticki.append(der)

plt.plot(x1, y_analiticki, label="Analiticka derivacija")
plt.plot(x1, y1, label=f"Numericka, eps={ε1}")
plt.plot(x2, y2, label=f"Numericka, eps={ε2}")
plt.plot(x3, y3, label=f"Numericka, eps={ε3}")

plt.xlabel("x")
plt.ylabel("f'(x)")
plt.title("Usporedba analiticke i numericke derivacije")
plt.legend()
plt.grid()
plt.show()

##################################################################################################################################################################