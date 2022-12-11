import math
user1=abs(int(input("the value of user1:")))
user2=abs(int(input("the value of user2:")))
user3=abs(int(input("the value of user3")))
user4=abs(int(input("the value of user4")))
user5=abs(int(input("the value of user5")))
total=(user1)+(user2)+(user3)+(user4)+(user5)

file=open("text.txt","w")
file.write(str(user1)+" ")
file.write(str(user2)+" ")
file.write(str(user3)+" ")
file.write(str(user4)+" ")
file.write(str(user5)+" ")
file.close()
print(total)



