lst = list(input())
alphabet = {}
for l in lst:
    alphabet[l] = 0

for l in lst:
    alphabet[l] += 1

odd = 0
odd_alp = ''
for key, value in alphabet.items():
    if value%2 == 1:
        odd += 1
        odd_alp = key
        alphabet[odd_alp] -= 1

keys = list(alphabet.keys())
keys.sort()
result = ''
if  odd > 1:
    result = "I'm Sorry Hansoo"
else:
    for key in keys:
        for _ in range(alphabet[key]//2):
            result = result + key

    temp = result[::-1]
    result = result + odd_alp + temp

print(result)