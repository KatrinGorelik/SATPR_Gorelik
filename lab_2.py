import numpy as np

def read_file(name_file):
    try:
        with open(name_file, 'r') as file:
            expert = [list(map(float, line.strip().split())) for line in file]
        return expert
    
    except FileNotFoundError:
        print(f"Файл '{name_file}' не знайдено.")
        return None
    
    except ValueError:
        print("Помилка: Файл містить недопустимі дані.")
        return None

def check_non_zero(val):
    if val == 0:
        raise ValueError("Значення не можуть бути рівними нулю через ділення на нуль")
    return val

def create_matrix(date):
    if len(date) != 3:
        raise ValueError("Масив повинен містити рівно 3 значення.")
    
    date = [check_non_zero(x) for x in date]

    matrix = np.array([
        [1,         date[0],   date[1]],       
        [1/date[0], 1,         date[2]],   
        [1/date[1], 1/date[2], 1]  
    ])
    return matrix

def geo_mean(matrix):
    return [np.prod(row)**(1/len(row)) for row in matrix]

def W_norm(matrix, Wi):
    # column_sums = np.sum(matrix, axis=0)
    #Wi = [geo_mean(row) for row in matrix]
    #Wi_sum = np.sum(Wi)
    return [a/np.sum(Wi) for a in Wi]

def matrix_pair_compair(matrix):
    Wi = geo_mean(matrix)
    Wnorm = W_norm(matrix, Wi)
    matrix_pair_compair = np.column_stack((matrix, Wi, Wnorm))
    return matrix_pair_compair, Wnorm

def get_MO(Wnorm_arr):
    return geo_mean(np.array(Wnorm_arr).T)

def max_priority_altern_K(Wnorm_arr):
    return np.max(Wnorm_arr, axis=0)

def global_priority(priority_alters, MO):
    global_priority_arr = np.sum(np.array(priority_alters).T * MO, axis=1)
    global_priority = np.max(global_priority_arr)
    return global_priority



# формат виводу
np.set_printoptions(precision=3, suppress=True)


# Розрахунок пріоритетністі критеріїв привиборі альтернативи
Wnorm_arr = [] # Значення оцінок за трьома експертами
print("\n----- Розрахунок пріоритетності критеріїв при виборі альтернативи -----")
for arr, i in zip(read_file('priority_criteria'), range(1, 4)):
    matrix_criteria, Wnorm = matrix_pair_compair(create_matrix(arr))
    Wnorm_arr.append(Wnorm)

    print(f"\nЕксперт {i}")
    print(np.matrix(matrix_criteria))

print("\n----- Розрахунок середнього значення оцінок за трьома експертами -----\n")
print("Вектор пріорітетів для кожного критерію:\n", np.matrix(Wnorm_arr).T)
MO = get_MO(Wnorm_arr)
print("\nMO(середнє значення оцінок за трьома експертами ):", np.matrix(MO))


#визначення пріоритетів альтернатив за кожним з критерії
priority_alter =[]
for i in range(1, 4):
    f_name = f'priority_alternatives_K{i}'
    print(f"\n----- Розрахунок пріоритетів альтернатив за критерієм К{i} -----")
    Wnorm_arr=[]
    for arr, j in zip(read_file(f_name), range(1, 4)):
        matrix_alternative, Wnorm = matrix_pair_compair(create_matrix(arr))
        Wnorm_arr.append(Wnorm)

        print(f"\nЕксперт {j}")
        print(np.matrix(matrix_alternative))

    priority_alter.append(max_priority_altern_K(Wnorm_arr))

print("\n----- Розрахунок глобального пріорітету -----\n")
print("Пріорітети альтернатив:\n", np.matrix(priority_alter).T)
print("MO(середнє значення оцінок за трьома експертами):", np.matrix(MO))

global_priority = global_priority(priority_alter, MO)
print("\nНайвищій пріорітет", np.round(global_priority, 3), "\n")

