def convert(seconds): 
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return "%d %02d" % (hour, sec)  
n =int(input())
print(convert(n))
convert(seconds)
