# using Counter: O(n) solution
# space in exchange of time
# from collections import Counter

# 空间换时间，形成字典，比对字典中key对应的value是否相等
# 时间复杂度为O(n)
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
