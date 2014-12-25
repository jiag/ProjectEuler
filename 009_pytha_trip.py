##### NOTE: Be aware of indent!!!!!!! Spend almost one hour to figure out a stupid mistake

import timing

def pytha(a,b):
    return a*a + b*b == (1000-a-b)*(1000-a-b)

def prod():
    a = 1
    while a < 1000/2:
        for b in range(max(a+1,500-a), 1000/2):
            if pytha(a,b):
                return a*b*(1000-a-b)
        a += 1

print prod()