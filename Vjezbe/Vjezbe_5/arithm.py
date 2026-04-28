import numpy as np

x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def aritmeticka_sredina(x_list):

    x = 0
    for i in range(len(x_list)):
        x = x + x_list[i]
    x = x / len(x_list)

    return x

def standardna_devijacija(x_list):

    x = 0
    x_s = aritmeticka_sredina (x_list)

    for i in range(len(x_list)):
        x = x + (x_list[i]-x_s)**2
    x = x / (len(x_list)*(len(x_list)-1))
    x = np.sqrt(x)

    return x

print(aritmeticka_sredina(x_list))
print(standardna_devijacija(x_list))

print(np.mean(x_list))
print(np.std(x_list) / np.sqrt(len(x_list)-1))