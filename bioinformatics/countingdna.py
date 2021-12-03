inp = input()
d = {'A': 0, 'C':0, 'G':0, 'T':0}
for c in inp:
    d[c]+=1
print(f"{d['A']} {d['C']} {d['G']} {d['T']}")
