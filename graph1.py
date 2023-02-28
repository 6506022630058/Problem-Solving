import networkx as nx
import matplotlib.pyplot as plt
import random

colist = ["gold","red","violet","pink","green","violet","orange","grey","blue","yellow","cyan"]
network = nx.Graph()
network.add_nodes_from([1,2,3,4,5,6,7])
print(f"This network has now {network.number_of_nodes()} nodes.")

network.add_edge(1,2)
network.add_edge(1,3)
network.add_edge(1,4)
network.add_edge(1,5)
network.add_edge(2,4)
network.add_edge(3,5)
network.add_edge(3,7)
network.add_edge(5,6)
network.add_edge(6,7)
color_list = [random.choice(colist) for _ in range(7)]
plt.figure(figsize=(8, 6))
plt.title('Huang So R Han', size=10)
nx.draw_networkx(network,node_color=color_list,with_labels=True,arrows=True,arrowstyle='->',arrowsize=20)
plt.show()