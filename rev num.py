a = (input())
reverse = 0
try:
    val = int(a)
    while val > 0:
        reminder = val % 10
        reverse = (reverse * 10) + reminder
        val //= 10
    print(reverse)
except ValueError:
    print("not valid")
