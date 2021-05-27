def binarysearch(seq,v,l,r):
    if (r-l==0):
        return(False)
    mid=(l+r)//2
    if (v==seq[mid]):
        return(True)
    if(v<seq[mid]):
        return(binarysearch(seq,v,l,mid))
    else:
        return(binarysearch(seq,v,mid+1,r))
    