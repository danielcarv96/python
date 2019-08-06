def pageCount(n, p):
    #
    # Write your code here.
    #
    val1=0
    val2=0
    lista=[]
    i=1
    ip = False
    
    if n%2 != 0:
        ip=True
    if ip==True:
        while i!=n-1/2+1:
            if i==1 :
                lista.append(i)
                i=i+1
            else:
                lista.append([i,i+1])
                i=i+2
            
        return lista
n = 5
p = 3
result = pageCount(n, p)
print (result)