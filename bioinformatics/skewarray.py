def SkewArray(g):
    arr = [0] * (len(g)+1)
    for i in range(1, len(g)+1):
        arr[i]=arr[i-1]
        if (g[i-1]=='G'):
            arr[i]+=1
        elif (g[i-1]=='C'):
            arr[i]-=1
    return arr