#Kunal Rai
# # for number in range(line):
# #     print(6-line, end='')
# #     print( )
# #     for line in range(1,6):
# #     for number in range(1):
# #         print(6-line, end='')
# #      print( )
# #      for space in range(6-line):
# #     print(" ", end='')
# for line in range(1,6):
#     for number in range(1):
#         print(6-line,5-line,4-line,3-line, end='')
#     for space in range(line):
#         print(" ", end='')
#     print( )
#     # for number in range(line):
#     #     print(line,end='')
begin=5
lines=begin
for line in range(lines):
    for number in range(begin-line,0,-1):
        print(number,end=' ')
    print('')
