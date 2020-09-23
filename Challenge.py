for line in range(1,9):
    for space in range (8-line):
        print(" ", end = '')
    for number in range (line,0,-1):
        print (number, end = '')
    for number in range(2,line+1):
        print(number,end = '')
    print()
