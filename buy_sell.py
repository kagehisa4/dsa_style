# given stock prices on days
# maximmize profit = sell-buy
# sell happens after buy happens

import random

[68, 62, 53, 62, 59, 70, -1]

arr = [68, 62, 53, 62, 59, 70, -1]
'''for i in range (7):
    arr.append(random.randint(50,80))

arr.append(-1)'''
print(arr)
min = arr[0]
max = arr[0]
profit = 0
hm = {}

for i in range(len(arr)):

    if max - min > profit:
        profit = max - min
        hm[profit] = [max, min]
    if arr[i] < min:
        min = arr[i]
    max = arr[i]

if profit != 0:
    print('profit: ', profit, hm[profit])
else:
    print('dont buy or sell')
