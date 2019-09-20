"""
In this concept we detect the cycle present in the graph if present then print graph have cycle otherwise donot have any cycle
in the graph


"""
from collections import defaultdict
class Graph:
    def __init__(self,vertex):
        self.V=vertex
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def find_parent(self,parent,i):
        if(parent[i]==-1):
            return i 
        if(parent[i]!=-1):
            return self.find_parent(parent,parent[i])

    def Union(self,parent,x,y):
        x_set=self.find_parent(parent,x)
        y_set=self.find_parent(parent,y)
        parent[x_set]=y_set


    def Cyclic(self):
        parent=[-1]*(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                x=self.find_parent(parent,i)
                y=self.find_parent(parent,j)

                if(x==y):
                    return True 
                self.Union(parent,x,y)



v=int(input())
g=Graph(v+1)

for i in range(v):
    u,v=map(int,input().split())

    g.addEdge(u,v)

if g.Cyclic():
    print("Graph contains cycle ")
else:
    print("Graph does not contain cycle")


