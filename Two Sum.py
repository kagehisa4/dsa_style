# this is two_sum
# generate number using random.randint()

arr = []
target = 100
hm = {}
for number in arr:
    compliment = target - number
    if compliment not in hm:
        hm[number] = ''
    else:
        print(number, compliment)
