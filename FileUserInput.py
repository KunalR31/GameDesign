#Kunal Rai
print('What would you like to name your file')
#This is to ask the user for the name of the file
filename = input ("filename: ");
#This is to write into the file
with open (filename, "w") as f:
  print('Whatever you type will be put into the file')
  f.write (input ())
  print('Whatever you type now will add to the last thing you typed')
  f.write(input ())
contents=open(filename)
# filename.read()
print(contents)
