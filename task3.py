array=[10,3,2,6,8,4,1,5,7,9]
for i in range(1, len(array)):
        j = i - 1
        while j >= 0 and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
print(array)