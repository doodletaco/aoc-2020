input = open('input.txt').read().splitlines()
goodpasswords = 0

for line in input:
    words = line.split()

    characters = words[0].split('-')
    posA = int(characters[0]) - 1
    posB = int(characters[1]) - 1
    char = words[1][0]

    if len(words[2]) > posB:
        if char in words[2][posA] and char in words[2][posB]:
            pass
        elif char in words[2][posA] or char in words[2][posB]:
            goodpasswords += 1

print(goodpasswords)
