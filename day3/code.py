input = open('input.txt').read().splitlines()

xpos = 0
trees = 0

for line in input:
    if line[xpos] == '#':
        trees += 1

    if xpos + 3 >= len(line):
        xpos = (xpos + 3) % len(line)
    else:
        xpos += 3

print(trees)
