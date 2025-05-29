"""
6. Write a Program to check if'a given graph is a complete graph. Represent the graph using
the Adjacency Matrix representation.
"""

def is_complete_graph_matrix(adj_matrix):
    num_vertices = len(adj_matrix)
    is_complete = True
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and adj_matrix[i][j] == 0:
                is_complete = False
                break
        if not is_complete:
            break
    return is_complete

size_matrix = int(input("Enter number of vertices: "))
matrix = []
print("Enter adjacency matrix row by row:")
for _ in range(size_matrix):
    row_elements = input().split()
    row = [int(x) for x in row_elements]
    matrix.append(row)

if is_complete_graph_matrix(matrix):
    print("Complete Graph:")
else:
    print("Not Complete")