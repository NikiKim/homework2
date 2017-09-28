def binary_search(num, arr):
    size = len(arr)
    low = 0
    hight = size - 1
    while (low <= hight):
        mid = int((low + hight) / 2)
        if num == arr[mid]:
            return mid
        elif num > arr[mid]:
            low = mid + 1
        else:
            hight = mid - 1
    return 'Такого числа не существует в массиве!'
print('Индекс требуемого элемента равен: ',
      binary_search(int(input('Введите число, которое необходимо найти: ')),[10,3,2,6,8,4,1,5,7,9]))
