def SkewArray(Genome):
    skew = {}
    for i in range(1, len(Genome)+1):
        if (i==1):
            skew[i]=0
        else:
            skew[i]=skew[i-1]
        if (Genome[i-1]=='G'):
            skew[i]+=1
        elif (Genome[i-1]=='C'):
            skew[i]-=1
    return skew

def MinimumSkew(Genome):
    positions = []
    temp = SkewArray(Genome)
    min_val = 9999999999999
    for key in temp:
        if (temp[key]<min_val):
            min_val=temp[key]
    for key in temp:
        if (temp[key]==min_val):
            positions.append(key)
    return positions