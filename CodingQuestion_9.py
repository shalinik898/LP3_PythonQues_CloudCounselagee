"""
CODING QUESTIONS:8
Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)...
(until n-x =< 0).
Test Data:
sum_series(6) -> 12
sum_series(10) -> 30
"""

def sum_series(n):
    if n<1:
        return 0
    else:
        return n+sum_series(n-2)

num=int(input())
print(sum_series(num))

"""(OR)

n=int(input())
total=0

for i in range(n-2):
    total+=i

print(total)"""