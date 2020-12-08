import  random

words = ['python', 'java', 'kotlin', 'javascript']
count = 0
random_word = list(random.choice(words))
progress = list('-' * len(random_word))
print('H A N G M A N')

while count < 8:
    print(f'\n{"".join(progress)}')
    attempt = input('Input a letter: ')
    if attempt in set(random_word):
        for i in range(0, len(random_word) - 1):
            if attempt == random_word[i]:
                progress[i] = attempt
    count += 1

print("""\nThanks for playing!
We'll see how well you did in the next stage""")
