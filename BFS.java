
import java.util.*;
import java.io.*;

class Graph
{
	int V;

	LinkedList<Integer> list[];

	Graph(int v)
	{
		this.V=v;
		list=new LinkedList[this.V];

		for(int i=0;i<V;i++)
		{
			list[i]=new LinkedList<Integer>();
		}
	}

	void addList(int u,int v)
	{
		list[u].add(v);
	}

	void BFS(int s)
	{
		boolean[] visited=new boolean[V];

		LinkedList<Integer> queue=new LinkedList<Integer>();
		queue.add(s);
		visited[s]=true;

		while(queue.size()!=0)
		{
			int n=queue.poll();

			System.out.print(n+" ");

			Iterator<Integer> it=list[n].iterator();

			while(it.hasNext())
			{
				int t=it.next();

				if(!visited[t])
				{
					visited[t]=true;
					queue.add(t);
				}
			}
		}
	}

	public static void main(String[] args)
	{
		Scanner sc=new Scanner(System.in);
		
		int e,v;
		e=sc.nextInt();
		v=sc.nextInt();
		Graph g=new Graph(v);

		for(int i=0;i<v;i++)
		{
			int v1,v2;
			v1=sc.nextInt();
			v2=sc.nextInt();

			g.addList(v1,v2);
		}
		g.BFS(0);
	}
}


