def Pr(Text, Profile):
    # insert your code here
    prob = 1
    for j in range(len(Text)):
        base = Text[j]
        prob *=Profile[base][j]
    return prob

def ProfileMostProbableKmer(text, k, profile):
    d = {}
    for i in range(len(text)-k+1):
        if (text[i:i+k] not in d):
            d[text[i:i+k]]=0
        d[text[i:i+k]]+=1
    maxi = 0
    for key in d:
        if (d[key]>maxi):
            maxi = d[key]
    arr = []
    for key in d:
        if (d[key]==maxi):
            arr.append(key)
    
    maxi =0
    for i in arr:
        if (Pr(i, profile)>maxi):
            maxi = Pr(i, profile)
    for i in arr:
        if (Pr(i, profile)==maxi):
            return i
    