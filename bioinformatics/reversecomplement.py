# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern

# Copy your Reverse() function here.
def Reverse(Pattern):
    # your code here
    return Pattern[::-1]
def Complement(Pattern):
    # your code here
    d = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    s = ""
    for i in Pattern:
        s+=d[i]
    return s
def ReverseComplement(Pattern):   
    # your code here
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern

print(ReverseComplement("CCAGATC"))