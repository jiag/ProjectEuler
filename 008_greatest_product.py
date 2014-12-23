import timing

f = open('008_greatest_product.txt','r')
number_list = f.read().replace('\n','')
f.close()

i = 0
max_prod = 1
while i < len(number_list):
	prod = 1
	j = 0
	while j <= 4:
		num = int(number_list[i+j])
		if num == 0:
			i += j
			break
		else:
			prod *= num
			j += 1
	i += 1
	if prod > max_prod:
		max_prod = prod

print max_prod