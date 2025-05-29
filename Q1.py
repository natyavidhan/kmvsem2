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
        else:
            first = self.elements[0]
            rest_set = SET(self.elements[1:])
            subsets_of_rest = rest_set.power_set()
            new_subsets = []
            for subset in subsets_of_rest:
                new_subsets.append([first] + subset)
            return subsets_of_rest + new_subsets

    def is_subset(self, other):
        for elem in other.elements:
            if elem not in self.elements:
                return False
        return True

    def union(self, other):
        combined = self.elements + other.elements
        return remove_duplicates(combined)

    def intersection(self, other):
        intersection_set = []
        for elem in self.elements:
            if elem in other.elements:
                intersection_set.append(elem)
        return intersection_set

    def complement(self, universal_set):
        complement_set = []
        for elem in universal_set:
            if elem not in self.elements:
                complement_set.append(elem)
        return complement_set

    def difference(self, other):
        difference_set = []
        for elem in self.elements:
            if elem not in other.elements:
                difference_set.append(elem)
        return difference_set

    def symmetric_difference(self, other):
        symmetric_diff_set = []
        combined = self.elements + other.elements
        for elem in combined:
            if (elem in self.elements) ^ (elem in other.elements):
                symmetric_diff_set.append(elem)
        return symmetric_diff_set

    def cartesian_product(self, other):
        product_set = []
        for a in self.elements:
            for b in other.elements:
                product_set.append((a, b))
        return product_set

def set_menu():
    print("\n--- SET Operations Menu ---")
    set1_elements = input("Enter elements of Set 1 (space-separated): ").split()
    s1 = SET([int(x) for x in set1_elements])
    set2_elements = input("Enter elements of Set 2 (space-separated): ").split()
    s2 = SET([int(x) for x in set2_elements])
    universal_elements = input("Enter elements of Universal Set (space-separated): ").split()
    universal = [int(x) for x in universal_elements]

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
            print("Set 2 is subset of Set 1" if s1.is_subset(s2) else "Not a subset")
        elif choice == '4':
            print("Union:", s1.union(s2))
        elif choice == '5':
            print("Intersection:", s1.intersection(s2))
        elif choice == '6':
            print("Complement of Set 1 w.r.t Universal Set:", s1.complement(universal))
            print()
            print("Complement of Set 2 w.r.t Universal Set:", s2.complement(universal))
        elif choice == '7':
            print("Set1 - Set2:", s1.difference(s2))
            print()
            print("Set2 - Set1:", s2.difference(s1))
        elif choice == '8':
            print("Symmetric Difference:", s1.symmetric_difference(s2))
        elif choice == '9':
            print("Cartesian Product:", s1.cartesian_product(s2))
        elif choice == '0':
            break
        else:
            print("Invalid choice")

set_menu()