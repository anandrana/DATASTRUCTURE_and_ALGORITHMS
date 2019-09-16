import java.util.*;
import java.io.*;

class Graph
{
	int V;
	LinkedList<Integer> stack[];

	Graph(int v)
	{
		V=v;
		stack=new LinkedList[v];
		for(int i=0;i<v;i++)
		{
			stack[i]=new LinkedList<Integer>();
		}
	}
	void addList(int u,int v)
	{
		stack[u].add(v);
	}

	void UtilDfs(int s,boolean vis[])
	{
		vis[s]=true;
		System.out.print(s+" ");

		Iterator<Integer> it=stack[s].iterator();
		while(it.hasNext())
		{
			int n=it.next();
			if(!vis[n])
			{
				vis[n]=true;
				UtilDfs(n,vis);
			}
		}

	}
	
	void Dfs(int s)
	{
		boolean[] vis=new boolean[V];
		UtilDfs(s,vis);
	}

	public static void main(String[] args)
	{
		Scanner sc=new  Scanner(System.in);
		int e,v;
		
		e=sc.nextInt();
		v=sc.nextInt();

		//boolean[] vis=new boolean[v];
		Graph g=new Graph(v);
		for(int i=0;i<e;i++)
		{
			int v1,v2;
			v1=sc.nextInt();
			v2=sc.nextInt();

			g.addList(v1,v2);
		}
		g.Dfs(0);

	}
}





