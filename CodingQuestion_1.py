"""
CODING QUESTIONS: 1
Read two integers from STDIN and print three lines where:
● The first line contains the sum of the two numbers.
● The second line contains the difference between the two numbers (first -
second).
● The third line contains the product of the two numbers.
Input Format
The first line contains the first integer, a. The second line contains the second integer, b.
Constraints
1<_a<_10 10
1<_b<_10 10
Output Format
Print the three lines as explained above.
Sample Input
3 2
Sample Output
5 1 6
"""

a = int(input())
b = int(input())

print(a+b, a-b, a*b)
