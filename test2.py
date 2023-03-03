import networkx as nx
import matplotlib.pyplot as plt
import random

def inputlivingthings(num):return [input('Name of living things: ').lower() for _ in range(num)]

colist = ["gold","red","violet","pink","green","violet","orange","grey","blue","yellow","cyan"]

network = nx.DiGraph()
network.add_nodes_from(['1','2','3'],weight=10)
print(f"This area has {network.number_of_nodes()} living things.")

def inputnetwork():
    lis = []
    ans = ''
    while ans != 'q':
        ans = input("----- Who Eat Who, Ex. --> Tiger Deer\nInput(q to quit): ").lower()
        if ans != 'q':
            lis.append(tuple(ans.split()))
    return lis

network.add_edges_from(inputnetwork())
color_list = [random.choice(colist) for _ in range(network.number_of_nodes())]

plt.figure(figsize=(8, 6))
plt.title('Huang So R Han', size=10)
nx.draw_networkx(network,node_color=color_list,with_labels=True,arrows=True,arrowstyle='->',arrowsize=20)
plt.show()