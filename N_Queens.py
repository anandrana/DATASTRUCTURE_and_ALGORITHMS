class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        result=[]
        list3=[]
        board=[[0 for i in range(A)] for j in range(A)]
        
        def issafe(board,i,j,n):
            #check for elements of column
            for row in range(i):
                if(board[row][j]==1):
                    return False 
            #check for elements of left diagonal 
            x=i
            y=j
            while(x>=0 and y>=0):
                if(board[x][y]==1):
                    return False 
                x-=1 
                y-=1 
                
            #check for elements of right diagonal 
            x=i
            y=j
            while(x>=0 and y<n):
                if(board[x][y]==1):
                    return False 
                x-=1 
                y+=1 
            return True 
            
        def solve(board,i,j,n):
            if(i==n):
                result=[]
                for i in range(0,n):
                    list1=[]
                    for j in range(0,n):
                        if(board[i][j]==1):
                            list1.append('Q')
                        else:
                            list1.append('.')
                    list1=''.join(list1)
                    result.append(list1)
                list3.append(result)
                return False 
            for j in range(n):
                if(issafe(board,i,j,n)):
                    board[i][j]=1 
                    t=solve(board,i+1,j,n)
                    if(t):
                        return True 
                    board[i][j]=0 
            
                
        solve(board,0,0,A)
        return list3

obj=Solution()
n=int(input())
print(obj.solveNQueens(n))


