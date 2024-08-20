# four major datatypes in python
# name = "shete" #string
# age = 21  #integer
# height = 5.8 #float
# is_employee = True #boolean
# print(name, age, height, is_employee)


# Concatenation
# input("What's your name ? ")
# print("Hello " + name)


# Type conversion
# old_age = input("What's your age ? ")
# new_age = int(old_age) + 5 #converting string into integer
# print(new_age)
# print("New age is : " + str(new_age))   #convert int back into string


# Strings
# name = "Shreyash Shete"
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.find('H'))
# print(name.replace('Shreyash', 'Shrey'))
# print('m' in name)


# Operator precedence
# i = 10 + 3 * 2
# i = (10 + 3) * 2
# print(i)


#if else statements
# age = 90
# if(age >= 20) :
#     print("You are an adult")
#     print("you can drive")
# elif(age < 18 and age > 3) :
#     print("You are in school")
# else :
#     print("You are younger than skibidi toilet")
# print("Thank you")


# Mini calculator
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# op = input("Enter operator : ")
# if(op == "+") :
#     print(a+b)
# elif(op == "-") :
#     print(a-b)
# elif(op == "*") :
#     print(a*b)
# elif(op == "/") :
#     print(a/b)
# elif(op == "%") :
#     print(a%b)
# elif(op == "//") :
#     print(a//b)
# elif(op == "**") :
#     print(a**b)
# else :
#     print("Invalid operator")


# Range is function in python
# num = range(5) #0,1,2,3,4
# print(num)
# print(list(num))
# print(list(range(6)))

# While loop
# i=0
# while(i<5) :
#     print(i)
#     i+=1

# i=0
# while(i<5) :
#     print(i * "*")
#     i+=1

# i=5
# while(i>=0) :
#     print(i * "*")
#     i-=1


# for loop
# for i in range(5) :
#     print(i + 1)


# List is collection of items, it can be combination of one or more datatypes
# list1 = [1, 2, 3, 4]
# print(list1)
# print(list1[1])
# list1.append(6)
# print(list1[-1])
# print(list1[0:2])  #ending index is exclusive

# for list in list1 :
#     print(list)

# list1.append(6)  #adds a value to the last index
# print(list1)

# list1.insert(0, 88)  #insert a value at any given index
# print(list1)

# print(99 in list1)  #boolean operator which checks whether a given value is present in the list or not

# print(len(list1))  #shows the total no of elements present in the list

# i=0
# while i< len(list1) :
#     print(list1[i])
#     i+=1


# list1.clear()  #clears all the elements in the list
# print(list1)
# print(list)


# Break and continue
# students = ["abc", "123", "shrey", "shete", "immobile"]
# for stud in students :
#     if stud == "shete" :
#         break
#     print(stud)

# for stud in students :
#     if stud == "shete" :
#         continue
#     print(stud)


#Tuples are immutable datatypes in python, the operations in tuples are faster than lists
# marks = (45, 38, 65, 65, 78, 65)
# print(marks.count(65))
# print(marks.index(65))
# print(type(marks))


#Sets stores unique values, index doesn't exist in sets, sets uses hash concepts to store values
# marks = {45, 38, 65, 78, 65}
# print(marks)


#Dictionary stores key value pairs
# marks = {"English" : 67,
#         "Chemistry" : 95,
#         "Physics" : 88}
# print(marks)
# print(marks["Chemistry"])

# marks["maths"] = 77
# print(marks)


