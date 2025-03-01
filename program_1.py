# 1.Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:

list_1 = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_list = sorted(list_1, key=lambda x: x[1])

print(f"{sorted_list}")