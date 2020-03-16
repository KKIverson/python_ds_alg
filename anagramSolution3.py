# using Counter: O(n) solution
# space in exchange of time
# from collections import Counter


def anagramSolution3(s1, s2):
    if len(s1) != len(s2):
        return False
    # c1 = Counter(s1)
    # c2 = Counter(s2)
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        c1[ord(s1[i]) - ord('a')] += 1
        c2[ord(s2[i]) - ord('a')] += 1
    stillOK = True
    j = 0
    while j < 26 and stillOK:
        if c1[j] != c2[j]:
            stillOK = False
            break
        j += 1
    # return c1 == c2
    return stillOK


print(anagramSolution3('apple', 'plfap'))
