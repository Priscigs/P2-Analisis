def lcs_dynamic(string1, string2):
    string1 = string1.upper()
    string2 = string2.upper()
    lx, ly = len(string1), len(string2)

    M = [[0 for x in range(ly + 1)] for y in range(lx + 1)]

    for i in range(lx + 1):
        for j in range(ly + 1):
            if not i or not j:
                M[i][j] = 0
            elif string1[i - 1] == string2[j - 1]:
                M[i][j] = M[i - 1][j - 1] + 1
            else:
                M[i][j] = max(M[i - 1][j], M[i][j - 1])

    index = M[lx][ly]
    lsc = [""] * (index + 1)
    lsc[index] = ""

    while lx > 0 and ly > 0:
        if string1[lx - 1] == string2[ly - 1]:
            lsc[index - 1] = string1[lx - 1]
            lx -= 1
            ly -= 1
            index -= 1
        elif M[lx - 1][ly] > M[lx][ly - 1]:
            lx -= 1
        else:
            ly -= 1

    print(string1, "<>", string2)
    print("LCS:", "".join(lsc), "\n")
    return "".join(lsc)


def lcs_divide_conquer(s1, s2, memo=None):
    s1 = s1.upper()
    s2 = s2.upper()

    if not s1 or not s2:
        return ""

    if memo is None:
        memo = {}

    if (len(s1), len(s2)) in memo:
        return memo[(len(s1), len(s2))]

    if s1[-1] == s2[-1]:
        lcs = lcs_divide_conquer(s1[:-1], s2[:-1], memo) + s1[-1]
    else:
        lcs1 = lcs_divide_conquer(s1[:-1], s2, memo)
        lcs2 = lcs_divide_conquer(s1, s2[:-1], memo)
        lcs = max(lcs1, lcs2, key=len)

    memo[(len(s1), len(s2))] = lcs
    print(s1, "<>", s2)
    print("LCS:", lcs, "\n")
    return lcs