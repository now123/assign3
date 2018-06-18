# Ques 1-

list = []
name1 = input("enter the input for the list")
list.append(name1)
name2 = input("enter the input for the list")
list.append(name2)
print("the list is", list)

# Ques 2-

a = []
b = ("yahoo", "mango", "whatsapp", "tesla")
a.append(b)
print(a)

# Ques 3-

a = "python", "java", "python", "c", "python"
print(a.count("python"))

# Ques 4-

a = [1, 6, 5, 8, 9]
a.sort()
print(a)

# Ques 5-

a = [1, 2, 3, 4, 5]
b = [5, 6, 7]
c = a + b
print(c)

# Ques 6-

a = [1, 2, 3, 4, 5]
a.pop()
print(a)

# Ques 7-

number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even += 1
    else:
        count_odd += 1
        print("number of even numbers:", count_even)
        print("nember of odd numbers:", count_odd)

