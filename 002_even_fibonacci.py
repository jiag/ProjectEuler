before_even = 1;
sum = 0;
even_old = 2;
while even_old<4000000:
    sum += even_old;
    even_number = 3*even_old+before_even*2;
    before_even = 2*even_old+before_even;
    even_old = even_number;
print sum