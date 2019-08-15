def smallest(s):
    l = len(s)
    ans = ''
    for i in range (l):
        if (s[i] < s[i + 1]):
            for j in range (l):
                if (i != j):
                    ans += s[j]
            return ans
            ans = s[0: l]
    return ans
if __name__ == "__main__":
    s = input()
    print (smallest(s))
