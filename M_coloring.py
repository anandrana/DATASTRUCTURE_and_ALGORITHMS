def issafe(graph,color,u,c):
    for i in range(len(graph[0])):
            if(graph[u][i] and c==color[i]):
                return False
    return True

def graph_coloring_util(graph,m,color,u):
    v=len(graph[0])
    if(u==v):
        print("solution exits are:")
        for i in range(v):
            print(color[i],end=" ")
        
        print()
        return False

    for c in range(1,m+1):
        if(issafe(graph,color,u,c)):
                color[u]=c
                if(graph_coloring_util(graph,m,color,u+1)):
                    return True 
                color[u]=0 
     


graph=[[0,1,1,1,],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
m=3
v=len(graph[0])
color=[]
p=0
for i in range(v):
    color.append(p)

graph_coloring_util(graph,m,color,0)


