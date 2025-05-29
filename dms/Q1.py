"""
1. Create a class SET. Create member functions to perform the following SET operations:
    1) ismember: check whether an element belongs to the set or not and return value as true/false.
    2) powerset: list all the clements of the power set of a set .
    3) subset: Check whether one set is a subset of the other or not.
    4) union and Intersection of two Sets.
    5) complement: Assume Universal Set as per the input elements from the user.
    6) set Difference and Symmetric Difference between two sets.
    7) cartesian Product of Sets. 
    
    Write a menu driven program to perform the above functions on an instance of the SET class.
"""

def remove_duplicates(seq):
    unique = []
    for item in seq:
        if item not in unique:
            unique.append(item)
    return unique

class SET:
    def __init__(self, elements):
        self.elements = remove_duplicates(elements)

    def is_member(self, elem):
        return elem in self.elements

    def power_set(self):
        if not self.elements:
            return [[]]
        first = self.elements[0]
        # Recursively find power set of the rest of the elements
        rest_powerset = SET(self.elements[1:]).power_set()
        # Combine subsets: those without 'first' and those with 'first' using a list comprehension
        return rest_powerset + [[first] + subset for subset in rest_powerset]

    def is_subset(self, other): # Checks if 'other' (Set) is a subset of 'self' (Set)
        for elem in other.elements:
            if elem not in self.elements:
                return False
        return True

    def union(self, other): # 'other' is a SET object
        # Combines elements from both sets and removes duplicates, returns a list
        return remove_duplicates(self.elements + other.elements)

    def intersection(self, other): # 'other' is a SET object
        # Returns a list of elements present in both sets using a list comprehension
        return [elem for elem in self.elements if elem in other.elements]

    def complement(self, universal_elements): # 'universal_elements' is a list of elements
        # Returns elements from universal_elements (list) not in self.elements using a list comprehension
        return [elem for elem in universal_elements if elem not in self.elements]

    def difference(self, other): # 'other' is a SET object
        # Returns elements in self but not in other using a list comprehension
        return [elem for elem in self.elements if elem not in other.elements]

    def symmetric_difference(self, other): # 'other' is a SET object
        # Original logic is concise and correct
        symmetric_diff_set = []
        combined = self.elements + other.elements
        for elem in combined: # Iterate over all elements, including potential duplicates in 'combined'
            # XOR condition correctly identifies elements unique to one set or the other
            if (elem in self.elements) ^ (elem in other.elements):
                symmetric_diff_set.append(elem)
        # The logic ensures elements in symmetric_diff_set are unique without an explicit remove_duplicates here
        return symmetric_diff_set

    def cartesian_product(self, other): # 'other' is a SET object
        # Returns a list of tuples (a, b) using a list comprehension
        return [(a, b) for a in self.elements for b in other.elements]

def set_menu():
    print("\n--- SET Operations Menu ---")
    set1_elements = input("Enter elements of Set 1 (space-separated): ").split()
    s1 = SET([int(x) for x in set1_elements])
    set2_elements = input("Enter elements of Set 2 (space-separated): ").split()
    s2 = SET([int(x) for x in set2_elements])
    universal_input_elements = input("Enter elements of Universal Set (space-separated): ").split()
    universal = [int(x) for x in universal_input_elements]

    while True:
        print("\n1. isMember\n2. PowerSet\n3. Subset\n4. Union\n5. Intersection\n6. Complement\n7. Difference\n8. Symmetric Difference\n9. Cartesian Product\n0. Exit")
        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            x = int(input("Enter element to check in Set 1: "))
            print("Present" if s1.is_member(x) else "Not Present")
        elif choice == '2':
            print("Power Set of Set 1:", s1.power_set())
        elif choice == '3':
            # s1.is_subset(s2) checks if s2 is a subset of s1
            print("Set 2 is subset of Set 1" if s1.is_subset(s2) else "Set 2 is not a subset of Set 1")
        elif choice == '4':
            print("Union (s1 U s2):", s1.union(s2))
        elif choice == '5':
            print("Intersection (s1 intersect s2):", s1.intersection(s2))
        elif choice == '6':
            print("Complement of Set 1 w.r.t Universal Set:", s1.complement(universal))
            print("Complement of Set 2 w.r.t Universal Set:", s2.complement(universal))
        elif choice == '7':
            print("Set1 - Set2:", s1.difference(s2))
            print("Set2 - Set1:", s2.difference(s1))
        elif choice == '8':
            print("Symmetric Difference (s1 delta s2):", s1.symmetric_difference(s2))
        elif choice == '9':
            print("Cartesian Product (s1 x s2):", s1.cartesian_product(s2))
        elif choice == '0':
            break
        else:
            print("Invalid choice")

set_menu()