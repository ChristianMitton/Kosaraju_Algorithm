# finds strongly connected components in directed graph

# 2 pass algorithm

# do dfs on graph until all nodes are explored
# store finish times of each node in stack
# reverse the graph 
# pop off each node in stack and do dfs on these nodes using newly reversed graph
    # obtain strongly connected component after each dfs
# return list of strongly connected components

class GraphNode:
    def __init__(self, name):
        self.name = name
        self.children = []

#? graph is given as an array of nodes
def kosaraju(graph):
    visited = {}
    nodesSortedByFinishTime = []
    # first pass
    for node in graph:        
        if node not in visited:
            getFinishTimes(root, visited, nodesSortedByFinishTime)
    
    reverseGraph(graph)  

    # second pass
    # pop elements from end of stack, do a dfs from that element on reversed graph
    visited = {}
    stonglyConnectedComponents = []
    for i in range(len(nodesSortedByFinishTime)):
        node = nodesSortedByFinishTime.pop(-1)
        stronglyConnectedComponent = []
        getStronglyConnectedComponentsAtNode(node, visited, stronglyConnectedComponent)
        stronglyConnectedComponents.append(stronglyConnectedComponent)

    return stronglyConnectedComponents


def getStronglyConnectedComponentsAtNode(node, visited, stronglyConnectedComponent):
    if root not in visited:
        visited[root] = True
    else:
        return

    stronglyConnectedComponent.append(root)

    for child in visited:
        getStronglyConnectedComponents(child, visited)    

def getFinishTimes(root, visited, stack):
    if root not in visited:
        visited[root] = True
    else:
        return

    for child in visited:
        getFinishTimes(child, visited)

    stack.append(root)

def reverseGraph(graphNodes):       
        pass




b = GraphNode('b')
c = GraphNode('c')
d = GraphNode('d')
e = GraphNode('e')
f = GraphNode('f')
g = GraphNode('g')
h = GraphNode('h')
i = GraphNode('i')
j = GraphNode('j')
k = GraphNode('k')
a = GraphNode('a')
a.children.append(b)
c.children.append(a)
b.children.append(c)
b.children.append(d)
d.children.append(e)
e.children.append(f)
f.children.append(d)
g.children.append(f)
g.children.append(h)
h.children.append(i)
i.children.append(j)
j.children.append(k)

graph = [a,b,c,d,e,f,g,h,i,j,k]

# for i in graph:    
#     print(i.name, ' >> ', end='')    
#     for i in i.children:
#         print(i.name + ' -> ', end='')        
#     print()


# time: o(v + e)
# space: o(v), 
#   where v is total vertices, and e total edges
