class RELATION:
    def __init__(self, matrix):
        self.my_matrix = matrix
        self.my_size = len(matrix)

    def is_reflexive(self):
        reflexive = True
        for i in range(self.my_size):
            if self.my_matrix[i][i] != 1:
                reflexive = False
                break
        return reflexive

    def is_symmetric(self):
        symmetric = True
        for i in range(self.my_size):
            for j in range(self.my_size):
                if self.my_matrix[i][j] != self.my_matrix[j][i]:
                    symmetric = False
                    break
            if not symmetric:
                break
        return symmetric

    def is_antisymmetric(self):
        antisymmetric = True
        for i in range(self.my_size):
            for j in range(self.my_size):
                if i != j and self.my_matrix[i][j] == 1 and self.my_matrix[j][i] == 1:
                    antisymmetric = False
                    break
            if not antisymmetric:
                break
        return antisymmetric

    def is_transitive(self):
        transitive = True
        for i in range(self.my_size):
            for j in range(self.my_size):
                if self.my_matrix[i][j] == 1:
                    for k in range(self.my_size):
                        if self.my_matrix[j][k] == 1 and self.my_matrix[i][k] == 0:
                            transitive = False
                            break
                if not transitive:
                    break
            if not transitive:
                break
        return transitive

    def relation_type(self):
        if self.is_reflexive() and self.is_symmetric() and self.is_transitive():
            return "Equivalence Relation"
        elif self.is_reflexive() and self.is_antisymmetric() and self.is_transitive():
            return "Partial Order Relation"
        else:
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