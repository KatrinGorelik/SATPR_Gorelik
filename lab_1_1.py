#лаб 1, завдання 1
#оцінки альтернатив(адвокатів) за критеріями
arr_candidates = [[3, 7, 2, 9], 
                  [8, 3, 6, 7], 
                  [4, 8, 3, 5], 
                  [9, 6, 5, 4]]
#ваги критеріїв
weight = [8, 9, 6, 7]

#обчислення оцінки корисності кожної альтернативи
result = [] 
for i in range(len(arr_candidates)):
    for j in range(len(arr_candidates[i])):
        arr_candidates[i][j] *= weight[j]
    # вивід поточного кандидата після множення на ваги
    print(f"Оцінки кандидата {i+1}:", arr_candidates[i])
    result.append(sum(arr_candidates[i]))

#визначення найкращої альтернативи
print("\nФункції корисності:", result)
print("Найкраща альтернатива:", result.index(max(result))+1, 
      "\nМаксимальна функція корисності:", max(result))