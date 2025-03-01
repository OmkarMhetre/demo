# 3. Write a program in Python to remove repetitive items from a list.
# Hint Given num = [2,3,4,5,2,6,3,2]
# Expected output Result: [2, 3, 4, 5, 6] New list

num = [2,3,4,5,2,6,3,2]

uni_list = list(set(num))

print("Unique List : ", uni_list)


