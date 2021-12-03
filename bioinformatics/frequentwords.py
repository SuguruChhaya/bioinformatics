# Copy your updated FrequentWords function (along with all required subroutines) below this line
def FrequencyMap(sequence, k):
    freq = {}
    for i in range(len(sequence) - k + 1):
        pattern = sequence[i:i+k]
        freq[pattern] = freq.get(pattern, 0) + 1
    return freq

def FrequentWords(sequence, k):
    words = []
    freq = FrequencyMap(sequence, k)
    m = max(freq.values())
    words = [pattern for pattern in freq if freq[pattern] == m]
    return words

# Now set Text equal to the Vibrio cholerae oriC and k equal to 10
Text = "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"

k = 3

# Finally, print the result of calling FrequentWords on Text and k.
print(FrequentWords(Text, k))