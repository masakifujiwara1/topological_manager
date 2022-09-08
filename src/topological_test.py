import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G2 = nx.Graph([(0, 1), (1, 2), (2, 0)])
G3 = nx.Graph()

G3.add_nodes_from([1, 2, 3, 4, 5, 6])
G3.add_edges_from([(1, 2), (1, 4), (2, 1), (2, 3), (2, 5), (3, 2),
                  (3, 6), (4, 5), (5, 4), (5, 6), (6, 5)])
# G3.add_edges_from([(1, 2, {'weight': 0.6}), (1, 4, {'weight': 0.3}), (2, 1, {'weight': 0.6}), (2, 3, {'weight': 1}), (2, 5, {'weight': 0.3}), (3, 2, {'weight': 1}),
#                   (3, 6, {'weight': 0.3}), (4, 5, {'weight': 0.6}), (5, 4, {'weight': 0.6}), (5, 6, {'weight': 1}), (6, 5, {'weight': 1})])
pos = {1: (0.0, 0.5), 2: (1.0, 0.5), 3: (3.0, 0.5),
       4: (0.0, 0.0), 5: (1.0, 0.0), 6: (3.0, 0.0)}
# print(pos)


G.add_node(1)       # 一つのノードを追加
G.add_node('one')
G.add_nodes_from([2, 3])  # 複数ノードを追加
G.add_nodes_from(['two', 'three'])

G.add_edge(1, 2)  # エッジの追加
G.add_edges_from([('one', 1), (2, 3), (2, 4), (2, 'two'),
                 (2, 'three'), ('two', 'three')])

fig = plt.figure(figsize=(5, 3))
# ax = fig.add_subplot()
nx.draw(G3, pos, with_labels=True)

plt.show(block=False)

print("Input goal node:1 or node:3")
node_no = input()
# print(node_no)
