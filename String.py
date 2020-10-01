#Kunal Rai
strVar= "Here are the instructions to install Drivers 1. After the download is completed go to where you saved the folder.(By default everything you download from the Internet is saved to the Downloads folder) 2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again.  3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon. 4. Next, open and Run the SETUP file. (In most cases it is a setup .exe file OR one listed below: * setup application *Asussetup *pnpinstal64 *pnputil *Igxpin 5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the setup."
print(len(strVar))
print(strVar.replace('Extract','EXTRACT'))
print(strVar.replace('setup','SETUP'))
#Finding the 1
print(strVar.find('4'))
print(strVar.find('1.'))
print(strVar.find(')'))
print(strVar[45:200])
#Finding the 2
print(strVar.find('2.'))
print(strVar.find('n.'))
print(strVar[201:291])
#Finding the 3
print(strVar.find('3.'))
print(strVar.find('on.'))
print(strVar[293:392])
#Finding the 4
print(strVar.find('4.'))
print(strVar.find('xpin'))
print(strVar[393:551])
#Finding the 5
print(strVar.find('5.'))
print(strVar.find('up.'))
print(strVar[552:685])
