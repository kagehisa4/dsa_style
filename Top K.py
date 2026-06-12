# Prints Top K numbers
import random
k = 2
arr = [random.randint(1,3) for _ in range(10)]
print(arr)
hm = {}

for num in arr:
    hm[num] = hm.get(num, 0) + 1 # obrains existing frequency adds with 1

# create buckets as lists stored inside lists - two numbers may have same frequency - so use lists.
bucket = [[] for _ in range(len(arr) + 1)]

for num, fre in hm.items():
    bucket[fre].append(num)

count = 0
for bucket_list in reversed(bucket):
    if bucket_list == []: continue
    print(bucket_list)
    if count == k:
        break
