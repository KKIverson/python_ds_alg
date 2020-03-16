# solution2: O(nlogn)
def anagramSolution2(s1, s2):
    if len(s1) != len(s2):
        return False
    alist1 = sorted(s1)
    alist2 = sorted(s2)

    pos = 0
    stillOK = True
    while pos < len(alist1) and stillOK:
        if alist1[pos] != alist2[pos]:
            stillOK = False
            break
        pos += 1
    return stillOK


print(anagramSolution2('abcd', 'dcbe'))
