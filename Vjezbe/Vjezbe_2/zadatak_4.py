import calculus
import math
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
from sympy import (symbols, integrate, lambdify, sin, cos, tan, cot, sinh, cosh, tanh, coth, asin, acos, atan, acot, asinh, acosh, atanh, acoth, log, exp, sqrt, Abs, pi, E)

#################################################################################################################################################################################################################################################

a = float(input("Unesi a: "))
b = float(input("Unesi b: "))
n = int(input("Unesi n: "))

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

def f_i_intf(izraz):
    
    rjecnik = {
        "x": x_sym,
        "sin": sin, "cos": cos, "tg": tan, "tan": tan, "ctg": cot,
        "sh": sinh, "ch": cosh, "th": tanh, "ctgh": coth,
        "arcsin": asin, "arccos": acos, "arctg": atan, "arcctg": acot,
        "arsh": asinh, "arch": acosh, "arth": atanh, "arcctgh": acoth,
        "log": log, "ln": log, "exp": exp, "sqrt": sqrt, "abs": Abs,
        "pi": pi, "e": E
    }

    expr = parse_expr(izraz, local_dict=rjecnik)
    expr_int = integrate(expr, x_sym)

    f = lambdify(x_sym, expr, "math")
    int_f = lambdify(x_sym, expr_int, "math")

    return f, int_f

#################################################################################################################################################################################################################################################

f, int_f = f_i_intf(izraz)

print("\ntest 1 (pravokutna aproksimacija)\n")
L_n, U_n = calculus.pravokutna_aprox(f, a, b, n)

print(f"Donja međa = {round(L_n, 2)}")
print(f"Gornja međa = {round(U_n, 2)}")

#################################################################################################################################################################################################################################################

print("\ntest 2 (trapezna aproksimacija)\n")
integral = calculus.trapezna_aprox(f, a, b, n)

print(f"Vrijednost integrala = {round(integral, 2)}")

#################################################################################################################################################################################################################################################

print(f"Analitička vrijednost integrala = {round(int_f(b) - int_f(a), 2)}")

#################################################################################################################################################################################################################################################

n_vrijednosti = [1, 2, 5, 10, 25, 50]
pravokutna_aprox_lista_Ln = []
pravokutna_aprox_lista_Un = []
trapezna_aprox_lista = []
analiticka_lista = []

I_a = int_f(b) - int_f(a)

for n in n_vrijednosti:

    L_n, U_n = calculus.pravokutna_aprox(f, a, b, n)
    pravokutna_aprox_lista_Ln.append(L_n)
    pravokutna_aprox_lista_Un.append(U_n)

    I_t_aprox = calculus.trapezna_aprox(f, a, b, n)
    trapezna_aprox_lista.append(I_t_aprox)
    
    analiticka_lista.append(I_a)
    
plt.plot(n_vrijednosti, trapezna_aprox_lista, marker="o", label="Trapezna aproksimacija")
plt.plot(n_vrijednosti, pravokutna_aprox_lista_Ln, marker="s", label="Pravokutna aproksimacija - donja međa")
plt.plot(n_vrijednosti, pravokutna_aprox_lista_Un, marker="d", label="Pravokutna aproksimacija - gornja međa")
plt.plot(n_vrijednosti, analiticka_lista, marker="^", label="Analitičko rješenje")

plt.xlabel("Broj podjela n")
plt.ylabel("Vrijednost integrala")
plt.title("Usporedba analitičkog i numeričkih rješenja integrala")
plt.legend()
plt.grid(True)
plt.show()

#################################################################################################################################################################################################################################################