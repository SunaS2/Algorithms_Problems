word = list(input())

reverse_word=word.copy()
reverse_word.reverse()

if word == reverse_word:
        print(1)
else:
        print(0)