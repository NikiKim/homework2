array=[10,3,2,6,8,4,1,5,7,9]
for i in range(len(array)-1):
    for j in range(len(array)-i-1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)