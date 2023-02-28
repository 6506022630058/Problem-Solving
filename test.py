import networkx as nx
import matplotlib.pyplot as plt
import random

def inputlivingthings(num):return [input('Name of living things: ') for _ in range(num)]

colist = ["gold","red","violet","pink","green","violet","orange","grey","blue","yellow","cyan"]

network = nx.Graph()
network.add_nodes_from(inputlivingthings(int(input('Number of living things in this area: '))))
print(f"This area has {network.number_of_nodes()} living things.")

def inputnetwork():
    lis = []
    ans = ''
    while ans.lower() != 'q':
        print("Input Who Eat Who, --> Tiger Deer")
        ans = input(':')
        if ans.lower() != 'q':
            lis.append(tuple(ans.split()))
    print(lis)
    return lis

network.add_edges_from([('a','b'),('c','b'),('d','b')])

color_list = [random.choice(colist) for _ in range(network.number_of_nodes())]
plt.figure(figsize=(8, 6))
plt.title('Huang So R Han', size=10)
nx.draw_networkx(network,node_color=color_list,with_labels=True,arrows=True,arrowstyle='->',arrowsize=20)
plt.show()