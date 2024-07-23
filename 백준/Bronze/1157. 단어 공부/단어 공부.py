word=input().upper()
word_list=list(set(word)) #중복값 제거

max_letter = 0
num_letter_list = []
for l in word_list:
    count = word.count(l)
    if max_letter <= count:
        max_letter = count
        letter = l

    num_letter_list.append(count)

if num_letter_list.count(max(num_letter_list))>=2:
     print('?')
else:
     print(letter)