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