#Kunal Rai
#10/28/20
myFile = open("newFile.txt", "w")
myFile.write("I am writing stuff")
myFile.close()
myFile = open("newFile.txt","r")
print(myFile.read())
myFile.close()
myFile = open("newFile.txt", "w")
myFile.write("Oops I deleted my stuff!")
myFile.close()
myFile = open("newFile.txt","r")
print(myFile.read())
myFile.close()
myFile = open("newFile.txt", "a")
myFile.write(" I add more stuff")
myFile.close()
myFile = open("newFile.txt","r")
print(myFile.read())
myFile.close()
