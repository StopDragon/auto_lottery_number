import requests
import random

def get_lotto_numbers(episode):
    params = {
        'method': 'getLottoNumber',
        'drwNo': episode
    }

    request = requests.get('https://dhlottery.co.kr', params=params)
    response = request.json()
    return response

    num_arr = []
    for i in range(1,7):
        num_arr.append(response["drwtNo" + str(i)])
    return num_arr

old_lotto_numbers = []
new_lotto_numbers = []

for i in range(1, 883):
    old_lotto_numbers.append(get_lotto_numbers(i))

while len(new_lotto_numbers) < 5:
    list_of_numbers = list(range(1,46))
    random.shuffle(list_of_numbers)
    numbers = list_of_numbers[:6]

    if numbers not in old_lotto_numbers or numbers not in new_lotto_numbers:
        new_lotto_numbers.append(numbers)

f = open("new_numbers.txt", 'w')
for nums in new_lotto_numbers:
    f.write(str(sorted(nums)) + "\n")
f.close()