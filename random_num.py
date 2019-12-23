import random

try_nums = 0
while try_nums < 5:
    lotto_nums = random.sample(range(1,46),6)
    lotto_nums.sort()
    print(lotto_nums)
    try_nums += 1
