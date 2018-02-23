def min (arr):
    my_min = float('Inf')
    for el in arr:
        if el < my_min:
            my_min = el
    return my_min

def average (arr):
    avrg = 0
    for el in arr:
        avrg += el
    avrg /= len(arr)
    return avrg

arr1 = [4, 8, 15, 16, 23, 42]
arr2 = range (10)
print ("Элементы массива: ", list(arr1))
print ("Наименьший элемент: ", min(arr1))
print ("Среднее значение: ", average(arr1))
print ("Элементы массива: ", list(arr2))
print ("Наименьший элемент: ", min(arr2))
print ("Среднее значение: ", average(arr2))
