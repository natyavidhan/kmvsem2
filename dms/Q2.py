"""
2. Create a class RELATION, use Matrix notation to represent a relation. Include member
functions to check if the relation is Reflexive. Symmetric, Anti-symmetric, Transitive.
Using these functions check whether the given relation is: Equivalence or Partial Order
relation or None
"""

class RELATION:
    def __init__(self, matrix):
        self.my_matrix = matrix
        self.my_size = len(matrix)

    def is_reflexive(self):
        # Checks if all diagonal elements are 1.
        return all(self.my_matrix[i][i] == 1 for i in range(self.my_size))

    def is_symmetric(self):
        # Checks if matrix[i][j] == matrix[j][i] for all i < j.
        # Iterating j from i + 1 covers each pair once.
        return all(self.my_matrix[i][j] == self.my_matrix[j][i]
                   for i in range(self.my_size)
                   for j in range(i + 1, self.my_size))

    def is_antisymmetric(self):
        # Checks if for i != j, it's not possible for both (i,j) and (j,i) to be in the relation.
        # So, if i != j, at least one of matrix[i][j] or matrix[j][i] must be 0.
        # Iterating j from i + 1 covers each pair (where i != j) once.
        return all(self.my_matrix[i][j] == 0 or self.my_matrix[j][i] == 0
                   for i in range(self.my_size)
                   for j in range(i + 1, self.my_size))

    def is_transitive(self):
        # Checks if for every (i,j) and (j,k) in relation, (i,k) is also in relation.
        # Returns False as soon as a counterexample (i,j) & (j,k) but not (i,k) is found.
        for i in range(self.my_size):
            for j in range(self.my_size):
                if self.my_matrix[i][j] == 1:  # If (i,j) is in R
                    for k in range(self.my_size):
                        # If (j,k) is in R but (i,k) is not
                        if self.my_matrix[j][k] == 1 and self.my_matrix[i][k] == 0:
                            return False  # Not transitive
        return True # No counterexample found

    def relation_type(self):
        # Determine relation type based on its properties.
        # Caching property results can be an optimization if called multiple times
        # or if computations are very expensive, but direct calls are fine here.
        reflexive = self.is_reflexive()
        symmetric = self.is_symmetric()
        transitive = self.is_transitive()

        if reflexive and symmetric and transitive:
            return "Equivalence Relation"
        
        # Antisymmetric property is checked only if not an Equivalence Relation,
        # or if specifically needed for Partial Order.
        antisymmetric = self.is_antisymmetric()
        if reflexive and antisymmetric and transitive:
            return "Partial Order Relation"
        
        return "None"

def relation_menu():
    print("\n--- RELATION Properties Menu (Revised) ---")
    n = int(input("Enter number of elements: "))
    matrix = []
    print("Enter adjacency matrix row by row:")
    for _ in range(n):
        row_elements = input().split()
        row = [int(x) for x in row_elements]
        matrix.append(row)

    rel = RELATION(matrix)
    print()
    print("Reflexive:", rel.is_reflexive())
    print("Symmetric:", rel.is_symmetric())
    print("Antisymmetric:", rel.is_antisymmetric())
    print("Transitive:", rel.is_transitive())
    print("Relation Type:", rel.relation_type())

relation_menu()