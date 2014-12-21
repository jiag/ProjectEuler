def ispal(n): 
    return str(n)==str(n)[::-1]

maxn = 0
for i in range(999,99,-1):
    for j in range(i, 99, -1):
        temp = i*j
        if ispal(temp):
            if temp>maxn:
                maxn = temp

print maxn