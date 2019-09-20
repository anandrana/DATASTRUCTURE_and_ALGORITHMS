class Graph:
    def __init__(self,vertex):
        self.V=vertex
        self.graph=[]

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    
    def find_parent(self,parent,i):
        if(parent[i]==i):
            return i
        return self.find_parent(parent,parent[i])


    def Union(self,parent,rank,x,y):

        x_set=self.find_parent(parent,x)
        y_set=self.find_parent(parent,y)

        if(rank[x_set]<rank[y_set]):
            parent[x_set]=y_set
        elif(rank[x_set]>rank[y_set]):
            parent[y_set]=x_set
        else:
            parent[y_set]=x_set
            rank[x_set]+=1 


    def KruskalMST(self):
        parent=[]
        rank=[]
        for i in range(self.V):
            parent.append(i)
            rank.append(0)
        
        self.graph=sorted(self.graph,key=lambda x:x[2])
        print(self.graph)
        e=0 #this is index for the vertex i.e V-1
        i=0
        
        result=[]
        while(e<self.V-1):
            u,v,w=self.graph[i]
            i+=1
            x=self.find_parent(parent,u)
            y=self.find_parent(parent,v)

            if(x!=y):
                e=e+1
                result.append([u,v,w])

                self.Union(parent,rank,x,y)
            #else discard the edge
        for u,v,w in result:
            print("%d---%d =%d"%(u,v,w))



V,E=map(int,input().split())
g=Graph(V)
for i in range(E):
    u,v,w=map(int,input().split())
    g.addEdge(u,v,w)

g.KruskalMST()


