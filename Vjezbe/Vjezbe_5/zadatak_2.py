N_list = [200, 2000, 20000]

def f(N_list):
    for i in range(len(N_list)):
        sum = 5
        for j in range(N_list[i]):
            sum = sum + 1/3
        for j in range(N_list[i]):
            sum = sum - 1/3
        
        print(f"Za N = {N_list[i]}, konačni rezultat je {sum}")
    return

f(N_list)