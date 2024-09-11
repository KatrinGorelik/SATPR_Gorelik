#лаб 1, завдання 2
#оцінки альтернатив(юристів) за критеріями
arr_candidates = [
    [85, 30, 22, 0.65, 6],
    [60, 20, 10, 0.6, 7],
    [30, 12, 5, 0.45, 5],
    [75, 24, 13, 0.7, 8],
    [40, 15, 7, 0.55, 7]]
#ваги
weights = [7, 5, 6, 8, 6]

#об'єднує елементи з однаковими індексами з кожного вкладеного списка в кортеж
#для кожного стовпця(кортежа), знаходимо max та min 
#та генерує список який має max та min для кожного стовпця
minc = [min(col) for col in zip(*arr_candidates)]
maxc = [max(col) for col in zip(*arr_candidates)]

#нормалізація
for j in range(len(arr_candidates)):
    for i in range(len(arr_candidates[j])):
        if j == 1: arr_candidates[i][j] = (maxc[j]-arr_candidates[i][j])/(maxc[j]-minc[j])*weights[j]
        else: arr_candidates[i][j] = (arr_candidates[i][j] - minc[j])/(maxc[j]-minc[j])*weights[j]

#визначення функцій корисності та найкращої альтернативи
result = [round(sum(cand), 4) for cand in arr_candidates]
print("\nФункції корисності:", result)
print("Найкраща альтернатива:", result.index(max(result))+1, 
      "\nМаксимальна функція корисності:", max(result))
