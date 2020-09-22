# #Kunal Rai
# print("1 2 3 4 5 6 7 8 9")
# print("1\n"+"2\n"+"3\n"+"4\n"+"5\n"+"6\n"+"7\n"+"8\n"+"9\n")
# print("1\n")
# print("2 2\n")
# print("3 3 3\n" )
# print("4 4 4 4\n")
# print("5 5 5 5 5\n")
# print("6 6 6 6 6 6\n" )
# print("7 7 7 7 7 7 7\n")
# print("8 8 8 8 8 8 8 8 \n")
# print("9 9 9 9 9 9 9 9 9\n" )
#
# for a in range(10):
#      print(a)
# for b in range(1,10):
#     print(b, end = '')
#     print(" ", end = '')
# print("\nI Am Done")
# for line in range(1,10):
#     for number in range(line):
#         print(line, end = '')
#         # print("A", end = '')
#     print()
#


for line in range (1,10):
    for space in range(9-line):
        print(" ", end = '')
    for number in range(line):
        print(line, end = '')
        print()
    # for space in range(1)
    # for space in range(line):
    #     print(" ", end = '')
