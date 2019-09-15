
import java.util.*;
import java.io.*;

class Graph
{
	int V;
	LinkedList<Integer> list[];

	Graph(int v)
	{
		this.V=v;
		list=new LinkedList[v];

		for(int i=0;i<V;i++)
		{
			list[i]=new LinkedList<Integer>();
		}
	}

	void addList(int u,int v)
	{
		list[u].add(v);
		list[v].add(u);
	}

	void PrintList()
	{
		for(int i=0;i<V;i++)
		{
			System.out.print(i);
			for(int node:list[i])
			{
				System.out.print("->"+node);
			}
			System.out.println();
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
		g.PrintList();
	}
}


		





