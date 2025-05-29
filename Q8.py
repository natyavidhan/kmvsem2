def compute_degrees(adj_matrix):
    size = len(adj_matrix)
    in_degrees = [0] * size
    out_degrees = [0] * size
    for i in range(size):
        for j in range(size):
            if adj_matrix[i][j]:
                out_degrees[i] += 1
                in_degrees[j] += 1
    return in_degrees, out_degrees

size = int(input("Enter number of vertices: "))
matrix = []
print("Enter adjacency matrix row by row:")
for _ in range(size):
    row_elements = input().split()
    row = [int(x) for x in row_elements]
    matrix.append(row)
in_deg, out_deg = compute_degrees(matrix)
for i in range(size):
    print(f"Vertex {i}: In-degree = {in_deg[i]}, Out-degree = {out_deg[i]}")