def HammingDistance(p, q):
    # your code here
    ans = 0
    for i in range(len(p)):
        if (p[i]!=q[i]):
            ans+=1
    return ans