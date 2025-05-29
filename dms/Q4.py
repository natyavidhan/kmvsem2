"""
4. For any number n, write a program to list all the solutions of the equation x, + x; + x, +
ot x, =C, where C is a constant (C<=10) and x,, x2.x3,....X, are nonnegalive integers,
using brute force strategy.
"""

n = int(input("Enter number of variables (n): "))
C = int(input("Enter constant (C <= 10): "))
if C > 10 or n <= 0:
    print("Invalid input! Ensure C <= 10 and n > 0.")
else:
    print(f"\nAll solutions of x1 + x2 + ... + x{n} = {C}:")

def solve(temp, index):
    if index == n - 1:
        last = C - sum(temp)
        if last >= 0:
            temp.append(last)
            print(temp)
            temp.pop()
        return
    for i in range(C - sum(temp) + 1):
        temp.append(i)
        solve(temp, index + 1)
        temp.pop()
solve([], 0)