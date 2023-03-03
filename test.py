import networkx as nx
import matplotlib.pyplot as plt
import random

def findpath(src,des):return [path for path in nx.all_simple_paths(network, source=src, target=des)]

def inputlivingthings(num):return [input(f'Name of living things {i+1}: ').lower() for i in range(num)]

def inputnetwork():
    print("\n----- Who Eat Who, Ex. --> Tiger Deer\nTo quit --> (Input: q)")
    lis = []
    ans = ''
    while ans != 'q':
        ans = input("Input: ").lower()
        if ans != 'q':
            lis.append(tuple(ans.split()))
    return lis

network = nx.DiGraph()

network.add_nodes_from(inputlivingthings(int(input('Number of living things in this area: '))))
print(f"This area has {network.number_of_nodes()} living things.")

network.add_edges_from(inputnetwork())
colist = ["gold","red","violet","pink","green","violet","orange","grey","blue","yellow","cyan"]
color_list = [random.choice(colist) for _ in range(network.number_of_nodes())]

print(findpath(input('Source: ').lower(),input('Destination: ').lower()))

plt.figure(figsize=(8, 6))
plt.title('Food Web', size=10)
nx.draw_networkx(network,node_color=color_list,with_labels=True,arrows=True,arrowstyle='->',arrowsize=20)
plt.show()