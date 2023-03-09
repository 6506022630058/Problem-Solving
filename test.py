import networkx as nx
import matplotlib.pyplot as plt
import random

def readfile(filename):
    if filename.endswith('.txt') == False:
        filename += '.txt'
    lis1 = []
    lis2 = []
    filer = open(filename,'r')
    line = filer.readline().rstrip('\n').lower()
    while line != '':
        if len(line.split()) == 2:
            lis1.append(tuple(line.split()))
        elif len(line.split()) == 1:
            lis2.append(line)
        else:
            pass
        line = filer.readline().rstrip('\n')
    filer.close()
    network.add_nodes_from(lis2)
    network.add_edges_from(lis1)

def findpath(src,des):return [path for path in nx.all_simple_paths(network, source=src, target=des)]

def inputlivingthings(num):return [input(f'Name of living things {i+1}: ').lower() for i in range(num)]

def inputnetwork():
    print("\nWho Eat Who, Ex. -->Input: tiger deer\nTo quit --> Input: q\n")
    lis = []
    ans = ''
    while ans != 'q':
        ans = input("Input: ").lower()
        if ans != 'q':
            if len(ans.split()) == 2:
                if ans.split()[0] in network.nodes() and ans.split()[1] in network.nodes():
                    lis.append(tuple(ans.split()))
                else:
                    pass
            else:
                pass
    return lis

def minmaxpath():
    lc,fc = '',''
    while lc not in network.nodes() and fc not in network.nodes():
        lc = input('Last consumer: ').lower()
        fc = input('First consumer: ').lower()
    allpath = findpath(lc,fc)
    res = []
    for i in allpath:
        res.append(len(i))
    if res != []:
        for i in allpath:
            if len(i) == min(res):
                print('Min path')
                print(i)
            if len(i) == max(res):
                print('Max path')
                print(i)
    if res == []:
        print('There is no path')

def makechoice(num):
    if num == 1:
        readfile(input('File name: '))
    elif num == 2:
        userinput()
    else:
        print('Invalid number')
        makechoice(int(input('1) Read File\n2) User Input\nChoice: ')))
        
def userinput():
    network.add_nodes_from(inputlivingthings(int(input('\nHow many living things in this area: '))))
    print(f"This area has {network.number_of_nodes()} living things.")
    network.add_edges_from(inputnetwork())

network = nx.DiGraph()

print('---Food Chains Program---')

makechoice(int(input('1) Read File\n2) User Input\nChoice: ')))

print('\n--All living things in this area--\n',network.nodes(),'\n')
print('--Find min-max path--')
minmaxpath()

colist = ["gold","red","violet","pink","green","violet","orange","grey","blue","yellow","cyan"]
color_list = [random.choice(colist) for _ in range(network.number_of_nodes())]
plt.figure(figsize=(8, 6))
plt.title('Food Web', size=10)
nx.draw_networkx(network,node_color=color_list,with_labels=True,arrows=True,arrowstyle='->',arrowsize=20)
plt.show()