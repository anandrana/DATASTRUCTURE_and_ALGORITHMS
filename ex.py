class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        stack=[]
        postfix=[]
        
        n=len(A)
        list1=list(A)
        for i in range(n):
            print(stack)
            print(postfix)
            
            if list1[i]>='a' and list1[i]<='z':
                postfix.append(list1[i])
            else:
                if list1[i]=='^':
                    
                    stack.append(list1[i])
                    
                elif list1[i]=='*':
                    if(len(stack)!=0):
                        while((len(stack)!=0) and (stack[-1]=='^' or stack[-1]=='/')):
                        
                            top=stack[-1]
                            postfix.append(top)
                            stack.pop()
                        
                    stack.append(list1[i])
                    
                elif list1[i]=='/':
                    print(len(stack),stack[-1])
                    if(len(stack)!=0):
                        while((len(stack)!=0) and (stack[-1]=='^' or stack[-1]=='*') ):
                            top=stack[-1]
                            postfix.append(top)
                            stack.pop()
                        
                    stack.append(list1[i])
                    
                elif list1[i]=='+':
                    if(len(stack)!=0):
                        while((len(stack)!=0) and (stack[-1]=='^' or stack[-1]=='*' or stack[-1]=='/' or stack[-1]=='-')):
                            top=stack[-1]
                            postfix.append(top)
                            stack.pop()
                    
                    stack.append(list1[i])
                
                elif list1[i]=='-':
                    if(len(stack)!=0):
                        while((len(stack)!=0) and (stack[-1]=='^' or stack[-1]=='*' or stack[-1]=='/' or stack[-1]=='+')):
                            top=stack[-1]
                            postfix.append(top)
                            stack.pop()
                        
                    stack.append(list1[i])
                    
                else:
                    if list1[i]==')':
                        if(list1[i]==')'):
                            while(stack[-1]!='('):
                                top=stack[-1]
                                postfix.append(top)
                                stack.pop()
                        
                            stack.pop()
                        
                    else:            
                        stack.append(list1[i])
                
        print(stack)
        postfix.extend(stack)
        print(postfix)
        
        
A="a+b*(c^d-e)^(f+g*h)-i"         
obj=Solution()
print(obj.solve(A))


