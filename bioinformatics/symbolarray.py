# Input:  Strings Genome and symbol
# Output: SymbolArray(Genome, symbol)
#!Looking for the forward strand. 
def PatternCount(Pattern, Text):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    '''
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    '''
    #array = [0]*n
    for i in range(n):
        if (i==0):
            array[0]=PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
        else:
            #!Ohh, it isn't just one letter!
            array[i] = array[i-1]
            array[i]+=(ExtendedGenome[i+(n//2)-len(symbol):i+(n//2)]==symbol)
            array[i]-=(ExtendedGenome[i-1:i-1+len(symbol)]==symbol)
    return array
'''
file = open("ecoli.txt")
inp = file.read()
print(SymbolArray(inp, 'C'))
'''
'''
inp1 = input()
inp2 = input()
print(SymbolArray(inp1, inp2))
'''