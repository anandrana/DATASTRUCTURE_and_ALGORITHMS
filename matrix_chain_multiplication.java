/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;


class GFG {
    public static int matrix_chain_multiplication(int[] array,int n)
    {
        int[][] multiply=new int[n+1][n+1];
        
        int i,l,j,k,q;
        for(i=1;i<n;i++)
            multiply[i][i]=0;
            
        
        // chain length
        
        for(l=2;l<n;l++)
        {
            for(i=1;i<n-l+1;i++)
            {
                j=i+l-1;
                if(j==n)
                    continue;
                    
                multiply[i][j]=Integer.MAX_VALUE;
                
                for(k=i;k<=j;k++)
                {
                    q=multiply[i][k]+multiply[k+1][j]+(array[i-1]*array[k]*array[j]);
                    
                    if(q<multiply[i][j])
                        multiply[i][j]=q;
                }
            }
        }
        return multiply[1][n-1];
        
    }
	public static void main (String[] args) {
		//code
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-- > 0)
		{
		    int n=sc.nextInt();
		    
		    int[] array=new int[n+1];
		    for(int i=0;i<n;i++)
		    {
		        array[i]=sc.nextInt();
		        
		    }
		    System.out.println(matrix_chain_multiplication(array,n));
		}
	}
}
