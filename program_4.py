# 4. Python program to create a list of tuples from given list having number and its 
# cube in each tuple.
# I/P-[1,2,5,6]  Output-[(1, 1), (2, 8), (5, 125), (6, 216)]

num = [1,2,5,6]

list_t = [(x, x**3) for x in num ]

print(f"{list_t}")