from collections import Counter

c = Counter('abdaab')

for letter in 'abcde':
    print(f'{letter} {c[letter]}')
