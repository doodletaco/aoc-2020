input = open('input.txt').read().splitlines()

def countTrees(r, d):
    xpos = 0
    trees = 0

    for i in range(0, len(input), d):
        line = input[i]

        if line[xpos] == '#':
            trees += 1

        if xpos + r >= len(line):
            xpos = (xpos + r) % len(line)
        else:
            xpos += r

    return trees

print(countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))
