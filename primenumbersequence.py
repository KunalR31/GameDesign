first=25
last=50
for number in range(first,last + 1):
    if number > 1:
        for a in range(2,number):
            if number%a == 0:
                break
        else:
            print(number)
