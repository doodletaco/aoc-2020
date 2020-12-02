input = open('input.txt').read().splitlines()
goodpasswords = 0

for line in input:
    words = line.split()

    minmax = words[0].split('-')
    min = int(minmax[0])
    max = int(minmax[1])
    char = words[1][0]

    count = words[2].count(char)
    if count >= min and count <= max:
        goodpasswords += 1

print(goodpasswords)
