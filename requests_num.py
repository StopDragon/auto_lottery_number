import requests, random, sys, time

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    if iteration == total: 
        print("\nAnalysis Complete")

def get_lotto_numbers(episode):
    params = {
        'method': 'getLottoNumber',
        'drwNo': episode
    }

    lottoAPI = requests.get('https://nlotto.co.kr/common.do', params=params)
    response = lottoAPI.json()

    old_temp = []
    for i in range(1,7):
        old_temp.append(response["drwtNo" + str(i)])
    return old_temp

old_lotto_numbers = []
new_lotto_numbers = []

for i in range(1, 891):
    old_lotto_numbers.append(get_lotto_numbers(i))
    printProgressBar(i, 890, 'Analyzing:', 'Complete', 1, 50, '█')

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
