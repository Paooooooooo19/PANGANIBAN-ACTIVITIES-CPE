# 1.

for num in range(-10, 0):
    print(num)


# 2.
for num in range(-10, 0):
    print(num)
else:
    print("Done")
    print("\n")

# 3.
start = 2
end = 9
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            print("\n")


# 4.
my_list = [1, 2, 3, 4, 5, 6]
for index in range(1, len(my_list), 2):
    print(my_list[index])


# 5.
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    elif num % 5 == 0:
        print(num)



