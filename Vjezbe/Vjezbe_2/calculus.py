import math

def deriviranje_u_tocki(f, x, ε, method="three-step"):
    
    if method == "two-step":
        
        f_der_x = (f(x + ε) - f(x)) / ε
        
        return f_der_x
    
    else:
        
        f_der_x = ((f(x + ε) - f(x - ε)) / (2 * ε))

    return f_der_x

def deriviranje_na_intervalu(f, a, b, ε, method="three-step"):

    x_list = []
    f_der_x_list = []
    
    x = a
    korak = 0.1

    while x <= b:

        x_list.append(x)

        if method == "two-step":
            
            f_der_x = (f(x + ε) - f(x)) / ε
        
        else:
                        
            f_der_x = ((f(x + ε) - f(x - ε)) / (2 * ε))

        f_der_x_list.append(f_der_x)

        x = x + korak

    return x_list, f_der_x_list

def pravokutna_apox(f, a, b, n):
    
    h = (b - a) / n
    L_n = 0
    U_n = 0

    for i in range(n):

        x_i = a + i * h
        x_ip1 = x_i + h

        m_i = min(f(x_i), f(x_ip1))
        M_i = max(f(x_i), f(x_ip1))

        L_n = L_n + m_i * h
        U_n = U_n + M_i * h

    return L_n, U_n


def trapezna_apox(f, a, b, n):

    h = (b - a) / n
    suma = 0

    for i in range(1, n):

        x_i = a + i * h
        suma = suma + f(x_i)

    integral = h * ((f(a) + f(b)) / 2 + suma)

    return integral