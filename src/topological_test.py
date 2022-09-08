import networkx as nx
import matplotlib.pyplot as plt

G3 = nx.Graph()

G3.add_nodes_from([1, 2, 3, 4, 5, 6])
G3.add_edges_from([(1, 2), (1, 4), (2, 1), (2, 3), (2, 5), (3, 2),
                  (3, 6), (4, 5), (5, 4), (5, 6), (6, 5)])

pos = {1: (0.0, 0.5), 2: (1.0, 0.5), 3: (3.0, 0.5),
       4: (0.0, 0.0), 5: (1.0, 0.0), 6: (3.0, 0.0)}
# print(pos)

fig = plt.figure(figsize=(5, 3))
# ax = fig.add_subplot()
nx.draw(G3, pos, with_labels=True)

plt.show(block=False)

print("Input goal node:1 or node:3")
node_no = input()
# print(node_no)
