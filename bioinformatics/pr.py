# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    # insert your code here
    d = {
        'A':0,
        'C':1,
        'G':2,
        'T':3
    }
    ans = 1
    for i in range(len(Text)):
        ans *= Profile[Text[i]][i]
    return ans





