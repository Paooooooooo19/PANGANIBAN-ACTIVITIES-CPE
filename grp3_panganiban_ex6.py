
def find_maximum(a, b, c):
   
    return max(a, b, c)


num1 = 10
num2 = 25
num3 = 15

maximum_value = find_maximum(num1, num2, num3)
print(f"The maximum of {num1}, {num2}, and {num3} is: {maximum_value}")

def sum_list(numbers):
   
    return sum(numbers)


my_numbers = [1, 2, 3, 4, 5]

total_sum = sum_list(my_numbers)
print(f"The sum of the numbers in the list {my_numbers} is: {total_sum}")

def reverse_string(input_string):
  
    return input_string[::-1]


original_string = "Hello, World!"

reversed_string = reverse_string(original_string)
print(f"The original string: {original_string}")
print(f"The reversed string: {reversed_string}")

def count_upper_lower(string):
   
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count


input_string = "Hello, World!"

upper, lower = count_upper_lower(input_string)
print(f"Original string: {input_string}")
print(f"Number of upper case letters: {upper}")
print(f"Number of lower case letters: {lower}")

def unique_elements(input_list):
   
    return list(set(input_list))


original_list = [1, 2, 2, 3, 4, 4, 5]

distinct_elements = unique_elements(original_list)
print(f"Original list: {original_list}")
print(f"List with distinct elements: {distinct_elements}")