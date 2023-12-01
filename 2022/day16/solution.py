import networkx as nx
import matplotlib.pyplot as plt

def drawgraph(G):
    pos = nx.spring_layout(G, seed=1)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=4)
    nx.draw_networkx_labels(G, pos, font_size=14, font_family="sans-serif")
    # edge_labels = nx.get_edge_attributes(G, "weight")
    # nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def part1():
    G = nx.Graph()
    with open(filename) as f:
        for i,line in enumerate(f):
            name = line.split(' ')[1]
            rate = int(line.split('=')[1].split(';')[0])
            if 'valves' in line:
                paths = line.strip().split('valves ')[1].split(', ')
            else:
                paths = [line.strip()[-2:]]
            G.add_node(name, rate=rate)
            for path in paths:
                G.add_edge(name,path,weight=2)
            


    for node in G.nodes(data=True):
        print(node)
    drawgraph(G)


def part2():
    with open(filename) as f:
        pass











import sys,time,string
try:
    if sys.argv[1] not in ['T','F']:
        raise
    filename = 'sampleinput.txt' if sys.argv[1] == 'T' else 'input.txt'
    part = int(sys.argv[2])
except:
    print('Usage: solution.py [T|F] [1|2] (Testing & Part)')
    exit()


start = time.perf_counter()
if part == 1:
    part1()
else:
    part2()
end = time.perf_counter()
ms = (end-start)# * 10**6
print(f"Elapsed {ms:.03f} seconds.")
print(f"Elapsed {ms*10**3:.03f} milliseconds.")
print(f"Elapsed {ms*10**6:.03f} microsecondss.")