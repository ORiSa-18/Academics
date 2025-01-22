#Q1. WRITE A PROGRAM TO SPLIT A WORD INTO PAIR’S AT ALL POSSIBLE POSITIONS. FOR EXAMPLE, CARRIED WILL BE SPLIT INTO {C, ARRIED, CA ,RRIED, CAR, RIED, CARR, IED, CARRI, ED, CARRI, D}.

word = "CARRIED"
result = []
for i in range(1, len(word)):
    part1 = word[:i]
    part2 = word[i:]
    result.append((part1, part2))

for split in result:
    print(split)

# Additional Exercise: Q1.Write a program to generate all possible prefixes and suffixes of a given word.

word = "CARRIED"
prefixes = []
suffixes = []
for i in range(1, len(word) + 1):
    prefixes.append(word[:i])
    suffixes.append(word[-i:])

for prefix in prefixes:
    print(prefix)

for suffix in suffixes:
    print(suffix)

  
# Additional Exercise: Q1.Write a program to generate all possible prefixes and suffixes of a given word.

import random

word = "CARRIED"
positions = list(range(1, len(word)))
random.shuffle(positions)

result = []
for i in positions:
    part1 = word[:i]
    part2 = word[i:]
    result.append((part1, part2))

for split in result:
    print(split)
