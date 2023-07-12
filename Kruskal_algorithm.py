# Importing the required libraries
import networkx as nx
import matplotlib.pyplot as plt
from unionfind import unionfind

# Define a function to create the graph as a dictionary


def make_graph():
    return {
        'A': [(3, 'D', 'A'), (3, 'C', 'A'), (2, 'B', 'A')],
        'B': [(2, 'A', 'B'), (4, 'C', 'B'), (3, 'E', 'B')],
        'C': [(3, 'A', 'C'), (5, 'D', 'C'), (1, 'E', 'C'), (4, 'B', 'C')],
        'D': [(3, 'A', 'D'), (5, 'C', 'D'), (7, 'F', 'D')],
        'E': [(8, 'F', 'E'), (1, 'C', 'E'), (3, 'B', 'E')],
        'F': [(9, 'G', 'F'), (8, 'E', 'F'), (7, 'D', 'F')],
        'G': [(9, 'F', 'G')],
    }

# Define a function to load the edges from the graph dictionary


def load_edges(G):
    num_nodes = 0
    edges = []

    for _, value in G.items():
        num_nodes += 1
        edges.extend(value)

    return num_nodes, sorted(edges)

# Define a function to convert character to integer


def conv_char(c):
    return ord(c) - 65

# Define the Kruskal's algorithm


def kruskals(G):
    total_cost = 0
    MST = []
    # Load the edges and initialize union-find

    num_nodes, edges = load_edges(G)
    uf = unionfind(num_nodes)
    # Iterate over the sorted edges and add them to the MST
    for edge in edges:
        cost, n1, n2 = edge[0], edge[1], edge[2]
        # Check if adding the edge creates a cycle

        if not uf.issame(conv_char(n1), conv_char(n2)):
            total_cost += cost
            uf.unite(conv_char(n1), conv_char(n2))
            MST.append((n1, n2, cost))

# Return the MST and the total cost

    return MST, total_cost

# Define the main function


def main():
    G = make_graph()
    MST, total_cost = kruskals(G)

    # Create a NetworkX graph
    G_nx = nx.Graph()
    for node, edges in G.items():
        for edge in edges:
            cost, neighbor = edge[0], edge[1]
            G_nx.add_edge(node, neighbor, weight=cost)

    # Create a NetworkX graph of the Minimum Spanning Tree
    MST_nx = nx.Graph()
    for edge in MST:
        n1, n2, cost = edge
        MST_nx.add_edge(n1, n2, weight=cost)

    # Draw both graphs using Matplotlib
    pos = nx.spring_layout(G_nx, seed=42)
    labels = nx.get_edge_attributes(G_nx, 'weight')
    nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=labels)
    nx.draw_networkx_nodes(G_nx, pos, node_size=1000, node_color='w')
    nx.draw_networkx_labels(G_nx, pos)
    nx.draw_networkx_edges(G_nx, pos)
    nx.draw_networkx_edges(MST_nx, pos, edge_color='r', width=2)

    plt.axis('off')
    plt.show()

    print(f'Minimum spanning tree: {MST}')


main()
