def without_rep(digits, temp=[]):
    if len(temp) == len(digits):
        print(temp)
        return
    for num in digits:
        if num not in temp:
            without_rep(digits, temp + [num])

def with_rep(digits, temp=[]):
    if len(temp) == len(digits):
        print(temp)
        return
    for num in digits:
        with_rep(digits, temp + [num])

n = int(input("Enter number of digits: "))
digits = []
print(f"Enter {n} digits one by one:")
for _ in range(n):
    num = int(input("Enter numbers: "))
    digits.append(num)

while True:
    print("\nMenu:")
    print("1. Permutations Without Repetition")
    print("2. Permutations With Repetition")
    print("3. Exit..")
 
    choice = int(input("Enter choice: "))
 
    if choice == 1:
        print("Permutations without repetition:")
        without_rep(digits)
    elif choice == 2:
        print("Permutations with repetition:")
        with_rep(digits)
    elif choice == 3:
        print("Exit!!")
        break
    else:
        print("Invalid choice.")