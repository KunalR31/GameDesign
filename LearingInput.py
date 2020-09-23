begin =int(input('Number of Lines\n'))
lines= begin
for line in range(lines):
    for number in range(begin-line,0,1):
        print(number, end='')
    print()
