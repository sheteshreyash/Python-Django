#Functions : There are 3 types of functions in python 1. in-built, 2. Module, 3. User-defined
# print(bin(25)) #convert from decimal to binary
# print(oct(25)) #convert from decimal to octal
# print(hex(25)) #convert from decimal to hexadecimal


# print(~12) #prints 2s complement of 12, reverses all the bits of the binary form of given decimal number and adds 1 to it to get to store the negative values

# print(12 & 13) #bitwise AND operation, compares all the bits of the binary form of the given decimal numbers and gives the output in binary form of the common bits

# print(12 | 13) #bitwise OR operation, compares all the bits of the binary form of the given decimal numbers and gives the output in binary form of the common bits

# print(12 ^ 13) #bitwise XOR operation, compares all the bits of the binary form of the given decimal numbers and gives the output in binary form of the uncommon bits

# print(12 << 2) #left shift operation, shifts all the bits of the binary form of the given decimal number to the left by 2 bits
#                 #Left shift decreases the value of the given decimal number by 2 power n, where n is the number of the bits shifted
# print(12 >> 2) #right shift operation, shifts all the bits of the binary form of the given decimal number to the right by 2 bits
#                 #Right shift increases the value of the given decimal number by 2 power n, where n is the number of the bits shifted





# Python import math module
# import math
# print(math.sqrt(25))
# print(math.floor(2.9))  #rounds off the given decimal number to the lower integer
# print(math.ceil(2.9))   #rounds off the given decimal number to the higher integer
# print(math.pow(2, 3))   #2 power 3
# print(math.pi)
# print(math.e)
# print(math.inf) #infinity
# print(-math.inf) #-infinity


# Swapping
# a = 6
# b = 7
# temp = a   # uses temporary variable to swap the values
# a = b
# b = temp   #requires extra variable memory to store the temp values

# a = a +b #uses addition to swap the values
# b = a-b  #b = a+b-b = a
# a = a-b  #a = a+b-a = b     #requires an extra bit to create a new variable

#uses XOR operation to swap the values
# a = a^b
# b = a^b
# a = a^b  #it will not require any extra bit to create a new variable

# a, b = b, a #pythonic way to swap the values
#uses rot_two() function which swaps two topmost stack items
# print(a, b)


#input from user
# b = eval(input("Enter an expression :"))
# print(b)


import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
z = a+b
print(z)