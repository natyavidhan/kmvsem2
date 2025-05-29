"""
5. Write a Program to evaluate a polynomial function. (For example store f(x) = 4n? + 2n + 9 
in an array and for a given value of n, say n = 5, compute the value of f{n)).
"""

def evaluate_polynomial(coeffs, n):
    result = 0
    power = 0
    for coefficient in coeffs:
        term_value = coefficient * (n ** power)
        result += term_value
        power += 1
    return result

coeffs_input = input("Enter coefficients (from x^0 to x^n): ").split()
coeffs = [int(x) for x in coeffs_input]
n_value = int(input("Enter value of n: "))
print("f(n) =", evaluate_polynomial(coeffs, n_value))