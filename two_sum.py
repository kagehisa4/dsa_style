import random
arr = []
sum = 100

for i in range(100):
    arr.append(random.randint(1,100))

print(arr)

hm = {}
'''for i in range(len(arr)):
    if  arr[i] not in hm:
        value = i
        key = sum - arr[i]
        hm[key] = value
    else:
        print(sum-arr[i], arr[i])'''

for i in range(len(arr)):
    need = sum - arr[i]

    if need in hm:
        print(arr[i], need)
        print('indices: ', hm[need], i)
    else:
        key = arr[i]
        value = i
        hm[key] = value
