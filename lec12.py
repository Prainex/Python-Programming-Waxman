'''
s = []
for i in range (1, 11):
    s.append(i)

sum = 0
for elements in s:
    sum = sum + elements
print(s)
print(sum)
'''

''' #even numbers
s = []
for i in range (1, 11):
    s.append(i)

sum = 0
for elements in s:
    if (elements % 2 == 0):
        sum += elements
print(s)
print(sum)
'''
''' #even positions
list = [x for x in range(1, 11)]
y = 0
for i, x in enumerate(list):
    if i % 2 == 0:
        y += x

print(list)
print (y)
'''

# from random import random as r, randint as ri
# # s = [ri(1, 10) for x in range(10)]
# # print(s)

# s = [ri(1, 25) for x in range(10)]
# maxint = 0
# for num in s: 
#     if num > maxint:
#         maxint = num

# print(s)
# print(maxint)

# from random import randint 
# s = []
# i = 0
# while i < 10:
#     x = randint(1, 10)
#     if x not in s: 
#         s.append(x)
#         i += 1
    
# print(s)


from random import randint
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 101) if is_prime(x)]
print(primes)