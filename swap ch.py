def swap():
    s = 'abcd'
    t = list(s)
    t[::2], t[1::2] = t[1::2], t[::2]
    x=''.join(t)
    print("badc")
swap()
