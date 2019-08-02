def des():
    count=5
    print("Input six integers:")
    nums = list(map(int, input().split()))
    nums.sort()
    nums.reverse()
    print("After sorting the said integers:")
    print(*nums)
des()
