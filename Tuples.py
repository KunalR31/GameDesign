#1, #2
tuple= ('a','b','c','d','1','2','3','4','4.5',)
#3
print(tuple[2])
#4
print(tuple[0:6])
#5
a= ('e')
tuple2= tuple+(a,)
print(tuple2)
print(type(tuple))
#7
print(tuple[4])
print(tuple2[5])
#9
repeat = tuple.count('d')
print(repeat)
#10
print(type(tuple[8]))
#11
# list=['yes','1','hi']
# tuplelist=tuple(list)
# print(type(list))
# print(type(tuplelist))
print(len(tuple))
