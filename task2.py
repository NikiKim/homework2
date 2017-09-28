array=[10,3,2,6,8,4,1,5,7,9]
for i in range(len(array) - 1):
        min_element = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_element]:
                min_element = j
        array[min_element], array[i] = array[i], array[min_element]
        print(array[i])
        
# Сложность n*n, т.е. O(n^2)
# Идет поиск наименьшего элемента и меняется с первым
# затем ищется следующий наименьший и меняем со вторым 
