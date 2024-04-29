#PANGANIBAN, JOHN PAOLO D. 
#GROUP 3

import array as arr


my_array = arr.array('i', [1, 3, 5])


print(my_array[0])  
print(my_array[1])  
print(my_array[2])  


my_array = arr.array('i', [1, 3, 5, 7, 9])

print("\nOriginal array:", my_array, "\nAppend 11 at the end of the array:")


my_array.append(11)

print("New array:", my_array)


my_array = arr.array('i', [1, 3, 5, 3, 7, 1, 9, 3])

print("\nOriginal array:", my_array)


my_array.reverse()

print("Reverse the order of the items:", my_array)



def has_duplicates(my_array):
    return len(set(my_array)) != len(my_array)


array1 = arr.array('i', [1, 2, 3, 4])
array2 = arr.array('i', [1, 2, 3, 2])
array3 = arr.array('i', [1, 1, 2, 3])

print("\n")
print(has_duplicates(array1))  
print(has_duplicates(array2))  
print(has_duplicates(array3))  


def find_first_duplicate(my_array):
    seen = set()
    for num in my_array:
        if num in seen:
            return num
        seen.add(num)
    return -1


array1 = arr.array('i', [2, 1, 4, 4, 5])
array2 = arr.array('i', [1, 2, 3, 4])
array3 = arr.array('i', [1, 1])

print("\n")
print(find_first_duplicate(array1))  
print(find_first_duplicate(array2))  
print(find_first_duplicate(array3))  