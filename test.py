import networkx as nx
import matplotlib.pyplot as plt
import random

def swap(l):return[l[1],l[0]]
def findpath(src,des):return [path for path in nx.all_simple_paths(network, source=src, target=des)]
def inputlivingthings(num):return [input(f'Name of living things {i+1}: ').lower() for i in range(num)]

def readfile(filename):
    global lisedg
    if filename.endswith('.txt') == False:filename += '.txt'
    lisedg,lisnod = [],[]
    filer = open(filename,'r')
    line = filer.readline().rstrip('\n').lower()
    while line != '':
        if len(line.split()) == 2:
            lisedg.append(tuple(swap(line.split())))
        elif len(line.split()) == 1:
            lisnod.append(line)
        else:
            pass
        line = filer.readline().rstrip('\n').lower()
    filer.close()
    network.add_nodes_from(lisnod)
    network.add_edges_from(lisedg)

def inputnetwork():
    print("\nWho Eat Who, Ex. -->Input: tiger deer\nTo quit --> Input: q\n")
    lis,ans = [],''
    while ans != 'q':
        ans = input("Input: ").lower()
        if ans != 'q':
            if len(ans.split()) == 2:
                if ans.split()[0] in network.nodes() and ans.split()[1] in network.nodes():
                    lis.append(tuple(swap(ans.split())))
    return lis

def minmaxpath():
    print('\n--Find min-max path--')
    lc,fc,res1,resmin,resmax = '','',[],[],[]
    while lc.lower() not in network.nodes() or fc.lower() not in network.nodes():
        lc,fc = input('From: ').lower(),input('To: ').lower()
    allpath = findpath(lc,fc)
    for i in allpath:
        res1.append(len(i))
    if res1 != []:
        print('\n-All path')
        for i in allpath:
            print(i,'\t')
            if len(i) == min(res1):resmin.append(i)
            if len(i) == max(res1):resmax.append(i)
        print('\n-Min path')
        for i in resmin:print(i)
        print('\n-Max path')
        for i in resmax:print(i)
    if res1 == []:
        print('There is no path\n')

def makechoice(num):
    if num == 1:
        readfile(input('File name: '))
    elif num == 2:
        userinput()
    else:
        makechoice(int(input(f'Error:Invalid number\n1) Read File\n2) User Input\nChoice: ')))
        
def userinput():
    network.add_nodes_from(inputlivingthings(int(input('\nHow many living things in this area: '))))
    network.add_edges_from(inputnetwork())

def displaygraph():
    colist = ["gold","violet","pink","violet","orange","yellow","cyan"]
    color_list = [random.choice(colist) for _ in range(network.number_of_nodes())]
    plt.figure(figsize=(8, 6))
    plt.title('Food Web', size=10)
    nx.draw_networkx(network,node_color=color_list,with_labels=True,arrows=True,arrowstyle='->',arrowsize=15,node_size=1000,font_size=9,pos=nx.circular_layout(network))
    plt.show()

def menu():
    ans = ''
    while ans != 5:
        ans = int(input('\n---Food Chains Program---\n1) Show All Living Things\n'
                        '2) Display Graph\n3) Find Min-Max Path\n4) Find Relation\n'
                        '5) Exit Program\nChoice: '))
        if ans == 1:print('\n--All living things in this area--\n',network.nodes(),'\n')
        elif ans == 2:displaygraph()
        elif ans == 3:minmaxpath()
        elif ans == 4:relation()
        elif ans == 5:print('Exiting Program...')
        else:print('Error:Invalid number')

def relation():
    print('\n--Relation--')
    lt,liseat,liseaten = '',[],[]
    while lt.lower() not in network.nodes():
        lt = input('Living thing: ').lower()
    for i in lisedg:
        if i[0] == lt:liseaten.append(i[1])
        elif i[1] == lt:liseat.append(i[0])
    if liseat == []:print(lt,'not eat any livingthing')
    elif liseat != []:print(lt,'eat',liseat)
    if liseaten == []:print(lt,'is not eaten by any livingthing')
    elif liseaten != []:print(lt,'is eaten by',liseaten)

if __name__ == '__main__':
    network = nx.DiGraph()
    makechoice(int(input('---Food Chains Program---\n1) Read File\n2) User Input\nChoice: ')))
    menu()