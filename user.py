import os
import time

while True:
    #input the statements
    name = input("enter user's name : ")
    start = int(input("start : "))
    stop = int(input("stop : "))
    password = input("enter user's password : ")
    #confirm
    time.sleep (0.5)
    print ("\nuser name\t: ")
    #list from name user if adduser 
    for i in range (start,stop):
        print ((name)+str(i),end=" ")

    print ("\n\npassword\t: ",password)
    #confirm if statements is correct
    confirm = input("\nif this statement is correct enter 'y' to continue : ")
    if confirm == "y":
        break
    else :
        time.sleep (0.5)
        print("\n")
        continue

#echo the statements in user.sh
many = ("echo for i in {"+str(start)+".."+str(stop)+"} >> user.sh")
do = ("echo do >> user.sh")
user = ("echo adduser "+ str(name) + "$i --disabled-password --gecos " + (name) + "$i >> user.sh")
passwd = ("echo passwd " + str(name) + "$i <<< " + (password)+"$'\n'"+ str(password)+ ">> user.sh")
#crearte file script for user.sh
os.system ("touch user.sh")
os.system (do)
os.system (user)
os.system (passwd)
os.system ("echo done >> user.sh")
#run the script
os.system ("chmod +x user.sh ")
os.system ("bash user.sh")





