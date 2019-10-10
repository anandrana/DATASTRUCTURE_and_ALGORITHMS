import java.lang.*;
import java.io.*;
import java.util.*;
class Node {
    char c;
    int data;
    Node left;
    Node right;
    
    Node(char c, int data) {
        this.c = c;
        this.data = data;
        left = null;
        right = null;
    }
}

class NodeComparator implements Comparator<Node> {
    public int compare(Node n1, Node n2) {
        if (n1.data < n2.data) {
            return -1;
        } else {
            return 1;
        }
    }
}
    
class GFG {
    
	public static void main (String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt();
		while(t > 0) {
		    String s = sc.next();
		    int d[] = new int[s.length()];
		    
		    for(int i=0;i<s.length();i++) {
		        d[i] = sc.nextInt();
		    }
		    
		    PriorityQueue<Node> q = new PriorityQueue<Node>(s.length(), new NodeComparator());
		    
		    for(int i=0;i<s.length();i++) {
		        Node n = new Node(s.charAt(i), d[i]);
		        q.add(n);
		        
		        //System.out.println(s.charAt(i) + ":" + d[i]);
		    }
		    
		    while(q.size() != 1) {
		        Node x = q.poll();
		        Node y = q.poll();
		        
		        Node n = new Node('-', x.data + y.data);
		        if(x.data <= y.data) {
		            n.left = x;
		            n.right = y;
		        } else {
		            n.left = y;
		            n.right = x;
		        }
		        
		        q.add(n);
		    }
		    
		    printHuffman(q.poll(), "");
		    System.out.println(); 
		    
		    t--;
		}
	}
	
	static void printHuffman(Node root, String s) {
	    if(root.left == null && root.right == null) {
	        System.out.print(s + " ");
	        return;
	    }
	    
	    if(root.left != null) {
	        printHuffman(root.left, s+"0");
	    }
	    
	    if(root.right != null) {
	        printHuffman(root.right, s+"1");
	    }
	}
}
