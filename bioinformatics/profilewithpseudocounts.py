# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def Count(Motifs):
    d = {}
    chars = ['A', 'C', 'G', 'T']
    for i in chars:
        d[i] = [1] * len(Motifs[0])
    for col in range(len(Motifs[0])):
        for row in range(len(Motifs)):
            d[Motifs[row][col]][col] += 1
    return d

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    return Count(Motifs)


def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)
    profile = count
    for i in range(k):
        total = 0
        for key in count:
            total += count[key][i]
        for key in count:
            profile[key][i] = count[key][i] / total
    '''
    for key in count:
        total = 0
        for i in count[key]:
            sum+=i
        for i in range(len(count[key])):
            profile[key][i] = count[key][i] / total
    '''
    # your code here
    return profile

