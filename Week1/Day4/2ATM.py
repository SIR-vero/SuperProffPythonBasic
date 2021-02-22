#Pooja would like to withdraw some amount from an ATM. 
#The cash machine will only accept the transaction 
#if X is a multiple of 5, and Pooja's account balance 
#has enough cash to perform the withdrawal transaction (including bank charges). 
#For each successful withdrawal the bank charges 1 rupees. 
#Calculate Pooja's account balance after an attempted transaction.

#First take the initial bank balance of Pooja in int.
#Then take the amount she wants to withdraw.

#If it is possible to withdraw that amount then print her bank balance after 
#withdrawl, else print u can't withdraw.

# initial bal -> 500			withdraw -> 100
# 500 - 100 = 400-1 = 399

initial_bal = int(input("Enter the initial balance : "))
withdraw = int(input("Enter the Amount you want to withdraw : "))


if initial_bal >= withdraw + 1:
	if withdraw%5 == 0:
		diff = initial_bal - withdraw - 1
		print("your remaining balance is ", diff)
	else :
		print("Cannot dispense amount which is not a multiple of 5")
else :
	print("you can't withdraw, but you can take loan ")
