"""
7. Write a Program to check if a given graph is a complete graph. Represent the graph using
the Adjacency List representation.
"""

def is_complete_graph_list(adj_list):
    num_vertices = len(adj_list)
    is_complete = True
    for i in range(num_vertices):
        if len(adj_list[i]) != num_vertices - 1:
            is_complete = False
            break
    return is_complete

size_list = int(input("Enter number of vertices: "))
adj_list = []
for i in range(size_list):
    print(f"Enter adjacent vertices of vertex {i}: ", end="")
    adj_elements = input().split()
    adj_list.append([int(x) for x in adj_elements])

if is_complete_graph_list(adj_list):
    print("Complete Graph:")
else:
    print("Not Complete")