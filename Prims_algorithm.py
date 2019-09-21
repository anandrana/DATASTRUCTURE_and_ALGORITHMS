"""
this is also used for finding the Mst(minimum spanning tree).
"""

import sys

class Graph:
    def __init__(self,vertex):
        self.V=vertex
        self.graph=[[0 for i in range(self.V)]for j  in range(self.V)]
    
    def printMst(self,parent):
        for i in range(1,self.V):
            print(parent[i],"----",i,self.graph[i][parent[i]])


    def minkey(self,key,mstSet):
        Min=sys.maxsize

        for i in range(self.V):
            if(key[i]<Min and mstSet[i]==False):
                Min=key[i]
                min_index=i
        return min_index


    def Prims(self):
        parent=[None]*(self.V)

        key=[sys.maxsize]*(self.V)
        key[0]=0
        parent[0]=-1

        mstSet=[False]*(self.V)
        for cout in range(self.V):
            u=self.minkey(key,mstSet)
            
            mstSet[u]=True

            for v in range(self.V):
                if self.graph[u][v]>0 and mstSet[v]==False and key[v]>self.graph[u][v]:
                    key[v]=self.graph[u][v]
                    parent[v]=u
        
        
        self.printMst(parent)




g=Graph(5)
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]]
g.Prims()

