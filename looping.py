# #Kunal Rai
for a in range(10):
     print(a)
for b in range(1,10):
    print(b, end = '')
    print(" ", end = '')
print("\nI Am Done")
for line in range(1,10):
    for number in range(line):
        print(line, end = '')
    print()



for line in range (1,10):
    for space in range(9-line):
        print(" ", end = '')
    for number in range(line):
        print(line, end = '')
        print()
    # for space in range()
    for space in range(line):
        print(" ", end = '')
