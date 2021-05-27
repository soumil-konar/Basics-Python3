def selectionsort(l):
    for start in range(len(l)):
        minpos=start
        for i in range(start,len(l)):
            if(l[i]<l[minpos]):
                minpos=i
        (l[start],l[minpos])=(l[minpos],l[start])
        

        
def insertionsort(l):
    for sliceEnd in range (len(l)):
        pos=sliceEnd
        while pos>0 and l[pos]<l[pos-1]:
            (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos])
        pos=pos-1
        
        
        
def insertionsort2(l):
    isort(l,len(l))
    
def isort(l,k):
    if k>1:
        isort(l,k-1)
        insert(l,k-1)

def insert(l,k):
    pos=k
    while pos>0 and l[pos]<l[pos-1]:
        (l[pos],l[pos-1])=(l[pos-1],l[pos])
    pos=pos-1
    
    
def mergesort(a,b):
    (c,m,n)=([],len(a),len(b))
    (i,j)=(0,0)
    while (i+j<m+n):
        if i==m:
            c.append(b[j])
            j=j+1
        if j==n:
            c.append(a[i])
            i=i+1
        elif a[i]<=b[j]:
            c.append(a[i])
            i=i+1
        elif a[i]>b[j]:
            c.append(b[j])
            j=j+1
    return(c)


def mergesort(l,right,left):
    if right-left<=1:
        return(a[left:right])
    if right-left>1:
        mid=(right+left)//2
        L=mergesort(a,left,mid)
        R=mergesort(a,mid,right)
        
        return(merge(L,R))


    
    
