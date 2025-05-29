"""
3. Write a Program that generates all the permutations of a given set of digits, with or
without repetition.
"""


# Function to generate permutations
# digits: The list of digits to permute
# allow_repetition: Boolean flag; True if repetitions are allowed, False otherwise
# current_permutation: The permutation being built in the current recursive call
def generate_permutations(digits, allow_repetition, current_permutation=[]):
    # Base case: a complete permutation has been formed
    if len(current_permutation) == len(digits):
        print(current_permutation)
        return

    for digit in digits:
        if allow_repetition or digit not in current_permutation:
            # Recursively call with the chosen digit added.
            # Creating a new list (current_permutation + [digit]) is important for backtracking.
            generate_permutations(digits, allow_repetition, current_permutation + [digit])

# Main function to drive the program
def main():
    try:
        n = int(input("Enter number of digits: "))
        if n <= 0:
            print("Number of digits must be positive.")
            return
        
        digits = []
        print(f"Enter {n} digits one by one:")
        for i in range(n):
            digits.append(int(input(f"Enter digit {i+1}: ")))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return

    # Main menu loop
    while True:
        print("\nMenu:")
        print("1. Permutations Without Repetition")
        print("2. Permutations With Repetition")
        print("3. Exit")
        
        choice = input("Enter choice: ") 
        
        if choice == '1':
            print("\nPermutations without repetition:")
            generate_permutations(digits, False)
        elif choice == '2':
            print("\nPermutations with repetition:")
            generate_permutations(digits, True)
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Ensures main() is called only when the script is executed directly
if __name__ == "__main__":
    main()