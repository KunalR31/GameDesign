#Kunal Rai
Dict1 = {3:4, 6:7, 4:5, 0:3}
print("Original ", Dict1)
#Sorted ascending
sorted_Dict1 =sorted(Dict1.items())
print("Sorted Ascending ", sorted_Dict1)
#Sorted Descending
sorted_Dict1 =sorted(Dict1.items(), reverse=True)
print("Sorted Descending ", sorted_Dict1)
Dict1.update({5:6})
print(Dict1)
#Make a new dictionary with other ones
Dict2={'e':4, 'b':2}
Dict3={'ab':'ac', 'ad':'ba'}
Dict4={}
for a in(Dict1,Dict2,Dict3):
    Dict4.update(a)
print(Dict4)
#Checking if a key is in a dictionary
def key_Finder(key):
    if key in Dict4:
        print('Key is in the dictionary')
    else:
        print('Key is not found')
key_Finder('ab')
#5
for key, value in Dict4.items():
    print( key," = ", value)
#6
n=10
dict6={}
for a in range(1, n+1):
    dict6[a]=a*a
print(dict6)
#7
n=15
dict6={}
for a in range(1, n+1):
    dict6[a]=a*a
print(dict6)
#8
dict8=Dict2.copy()
dict8.update(Dict3)
print('dictionary 8 -', dict8)
#9
for key, value in Dict1.items():
    print(key, 'has this value', value)
#10
print("the sum of the values is", sum(Dict1))
