""" https://sociopatterns.org/datasets/high-school-contact-and-friendship-networks/
"""
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Load dataset
df = pd.read_csv(r"C:\Users\Samiksha Bokade\Downloads\your_file.csv", header=None)

# Create graph
G = nx.from_pandas_edgelist(df, 0, 1)

print("Total nodes:", G.number_of_nodes())

# Get top 50 nodes by degree
top_nodes = [n for n, _ in sorted(G.degree, key=lambda x: x[1], reverse=True)[:50]]

# Create subgraph
G = G.subgraph(top_nodes)

print("Nodes in graph:", G.number_of_nodes())

# Closeness centrality
print("Top 5 Closeness:")
print(sorted(nx.closeness_centrality(G).items(), key=lambda x: x[1], reverse=True)[:5])

# Betweenness centrality
print("\nTop 5 Betweenness:")
print(sorted(nx.betweenness_centrality(G).items(), key=lambda x: x[1], reverse=True)[:5])

# Draw graph
nx.draw(G, nx.spring_layout(G, seed=42), with_labels=True, node_size=400, font_size=8)
plt.title("Top 50 Nodes Network")
plt.show()

"""pip install pandas
pip install matplotlib
pip install networkx """
