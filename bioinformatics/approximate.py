# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def HammingDistance(p, q):
    # your code here
    ans = 0
    for i in range(len(p)):
        if (p[i]!=q[i]):
            ans+=1
    return ans

def ApproximatePatternMatching(Text, Pattern, d):
    positions = [] # initializing list of positions
    # your code here
    for i in range(len(Text)-len(Pattern)+1):
        if (HammingDistance(Pattern, Text[i:i+len(Pattern)])<=d):
            positions.append(i)
    return positions


# Insert your Hamming distance function on the following line.