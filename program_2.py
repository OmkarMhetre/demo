# 2.Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]

list_l =[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

div = list( filter(lambda x: x % 19==0 & x % 13 == 0, list_l))
print(f"{div}")