##Rent Calculator
##INnpu we needed from the user
#total rent
#Tatal food ordered for snacking
#Electricity charge
#Charge per unit

##output
#Total amoutnt you've to pay
rent = int(input("Enter your hostel rent: "))
food = int(input("Enter the price of snacks you have ordered: "))
electricity_charge = int(input("Amount of electricity bill: "))
charge_per_unit = int(input("Enter the amount of unnit charge: "))
persons = int(input("No of persons living in one room: "))

total_bill = electricity_charge * charge_per_unit

output = (rent + food + total_bill)  // persons
print("The amount paid by singe person is: ",output)