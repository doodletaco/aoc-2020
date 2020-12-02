number = 0
a = 0

input = open('input.txt').read().splitlines()

while a < len(input):
    b = a
    while b < len(input):
        c = b
        while c < len(input):
            if int(input[a]) + int(input[b]) + int(input[c]) == 2020:
                number = int(input[a]) * int(input[b]) * int(input[c])
            c += 1
        b += 1
    a += 1

print(number)
