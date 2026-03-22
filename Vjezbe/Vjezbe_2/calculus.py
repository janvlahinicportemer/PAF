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