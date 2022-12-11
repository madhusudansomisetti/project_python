colour = input("enter the car colour :")
carBrand = input("enter car brand :")
car={colour:carBrand }
file=open("car.txt","w")
file.write(colour+" ")
file.write(carBrand+" ")
file.close()
print(car)