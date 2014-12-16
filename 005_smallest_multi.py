primen = [2,3,5,7,11,13,17,19] 
smallest_number = 1
for i in primen:
    powj = i
    while powj < 20:
        powj = powj*i
    smallest_number *= powj/i
print smallest_number

print 2**4*3**2*5*7*11*13*17*19