import json
import networkx as nx
import matplotlib.pyplot as plt

# Load data from JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Create a directed graph (or use nx.Graph() for undirected)
G = nx.DiGraph()

# Add nodes
for node in data['nodes']:
    G.add_node(node['id'], label=node['label'])

# Add edges
for edge in data['edges']:
    G.add_edge(edge['source'], edge['target'])

# Optionally print out the graph nodes and edges
print("Nodes:", G.nodes(data=True))
print("Edges:", G.edges())
# Draw the graph
pos = nx.spring_layout(G)  # Positioning layout for better visualization
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_color='black', font_weight='bold', edge_color='gray')

# Optionally, add labels to nodes
labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels, font_size=12)

# Show the plot
plt.title("Graph from JSON Data")
plt.show()
