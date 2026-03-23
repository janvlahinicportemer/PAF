import calculus
import math
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr #pretvaranje teksta u simbolički matematički izraz koji SymPy razumije
from sympy import (symbols, diff, lambdify, sin, cos, tan, cot, sinh, cosh, tanh, coth, asin, acos, atan, acot, asinh, acosh, atanh, acoth, log, exp, sqrt, Abs, pi, E)

#################################################################################################################################################################################################################################################

x = float(input("Unesi x: "))
a = float(input("Unesi a: "))
b = float(input("Unesi b: "))
ε = float(input("Unesi ε: "))
method = input("Želiš li koristiti two-step metodu (DA/NE):").strip().upper()

izraz = input(
    "Unesi funkciju f(x)\n "
    "Npr. x**(n), x**(1/n), sqrt(x), "
    "sin(x), cos(x), tg(x), ctg(x), "
    "sh(x), ch(x), th(x), ctgh(x), "
    "arcsin(x), arccos(x), arctg(x), arcctg(x), "
    "arsh(x), arch(x), arth(x), arcctgh(x), "
    "log(x, b), ln(x), exp(x), a**(x), "
    "abs(x), (konst.; pi, e)\n "
    "\n\nf(x) = ")

#################################################################################################################################################################################################################################################

x_sym = symbols('x')

def f_i_derf(izraz):
    
    rjecnik = {
        "x": x_sym,
        "sin": sin, "cos": cos, "tg": tan, "tan": tan, "ctg": cot,
        "sh": sinh, "ch": cosh, "th": tanh, "ctgh": coth,
        "arcsin": asin, "arccos": acos, "arctg": atan, "arcctg": acot,
        "arsh": asinh, "arch": acosh, "arth": atanh, "arcctgh": acoth,
        "log": log, "ln": log, "exp": exp, "sqrt": sqrt, "abs": Abs,
        "pi": pi, "e": E}

    expr = parse_expr(izraz, local_dict = rjecnik)
    expr_der = diff(expr, x_sym)

    f = lambdify(x_sym, expr, "math") #pretvara simbolički izraz u Python funkciju
    der_f = lambdify(x_sym, expr_der, "math")

    return f, der_f

#################################################################################################################################################################################################################################################

f, der_f = f_i_derf(izraz)

if method == "DA":

    print("\n test 1 \n")
    print(f"f'({x}) = {calculus.deriviranje_u_tocki(f, x, ε, 'two-step')}")

else:

    print("\n test 1 \n")
    print(f"f'({x}) = {calculus.deriviranje_u_tocki(f, x, ε)}")

#################################################################################################################################################################################################################################################

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

#################################################################################################################################################################################################################################################

ε_list = [0.5, 0.25, 0.1, 0.01, 0.001]
rezultati = []

if method == "DA":

    for ε in ε_list:

        x_num, y_num = calculus.deriviranje_na_intervalu(f, a, b, ε, "two-step")
        
        rezultati.append((ε, x_num, y_num))
else:
    
    for ε in ε_list:
        
        x_num, y_num = calculus.deriviranje_na_intervalu(f, a, b, ε)
        
        rezultati.append((ε, x_num, y_num))

x_analiticki = rezultati[0][1]
y_analiticki = []

for t in x_analiticki:

    y_analiticki.append(der_f(t))

plt.plot(x_analiticki, y_analiticki, label="Analitička derivacija")

for ε, x_num, y_num in rezultati:

    plt.plot(x_num, y_num, label=f"Numerička, ε={ε}")

plt.xlabel("x")
plt.ylabel("f'(x)")
plt.title("Usporedba analitičke i numeričke derivacije")
plt.legend()
plt.grid()
plt.show()

#################################################################################################################################################################################################################################################