# Run the following program: 
# from math import sqrt
# from random import random

# count = 0 
# for i in range(1000000):
#     x = random()
#     y = random()
#     if sqrt(x*x+y*y)<1:
#         count+=1

# print(4*(count/1000000))

'''
2. What is it calculating?
    a) idk but it looks like the output is pi "3.14178"

3. How/why does it work? What is the theory behind this?

'''

# a  = [1, 2, 3, 4, 5, 6, 7]
# b = a[3:5]
# print (b)
# # prints [4, 5]

# c = a[:5]
# print (c)
# #prints [1,2, 3, 4, 5]

# d = a[1:]
# print (d)
# #prints every value except the first one

# y = a[::2]
# z = a[1::2]
# print(y)
# #prints [1, 3, 5, 7]

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = x[1:8:2]
# print(y)

# y[1:8:2]=['a', 'b', 'c', 'd']
# print (y)



# d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(d[1:len(d):2])

# def delete_at_even_positions(x):
#     del x[1:len(d):2]

# delete_at_even_positions(d)
# print(d)
# #remove the 1 so it actually deletes at even positions.

def insertion_sort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        key = arr[i] 
        # Move elements of arr[0..i-1], that are greater than key, 
        # to one position ahead of their current position 
        j = i - 1 
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j] 
            j -= 1 
        arr[j + 1] = key 
    return arr 
 
arr = [12, 11, 13, 5, 6] 
insertion_sort(arr) 
print("Sorted array is:", arr) 