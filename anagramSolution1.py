# solution1: O(n^2)
# 对s1中的元素挨个在s2中搜索，搜索到的记为None
def anagramSolution1(s1, s2):
    if len(s1) != len(s2):
        return False
    alist = list(s2)
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 += 1
    return stillOK


print(anagramSolution1('abcd', 'dcba'))