scores = [10, 59, 68, 45, 89, 78, 120, 80, 30, 60, 45]
#Duplicating the max function in Python
max = scores[0]
for a in scores:
    if (a > max):
        max = a

print(max)

'''
Assume the first index value is largest,
'a' will check with every value in the list after each iteration and if it finds a value greater than itself,
it will update in max.
'''