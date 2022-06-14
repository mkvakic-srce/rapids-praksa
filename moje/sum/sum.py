import numpy as np
np_numbers = np.arange(10**8)

# sum = np_numbers.sum()
# print (np_numbers)

sum = 0
for value in np_numbers:
	sum = sum + value
print(sum)

