import time
import os

def start():
	GameEnd = False
	Cash = 20000.00
	Stamina = 100
	Months = 0
	Age = 22
	TimeAtCompany = 0
	Company = 'Google'
	Salary = 120000.00
	CorporateWarnings = 0
	Companylist = ['Amazon' , 'Facebook' , 'Microsoft' , 'Start Up']
	CompanyPay =  [ 130000.00  ,  160000.00   ,  140000.00     ,  110000.00  ]

	print("Welcome to Google!")
	time.sleep(0.1)
	print("You'll be working here and trying to make your way up!")
	time.sleep(0.1)
	print("Here are the commands you can use for the month")
	print("	!Work: You spend your month entirely working")
	print("	!Rest: Earn back some Stamina")
	print("	!Stats: Shows current stats and conditions")
	print("	!Move: Switch to a new company. You lose benefits,") 
	print("       	    but get better pay")
	print("	!Retire: Collect savings and end the game")
	print("	!Clear: Clears the screen of text")
	time.sleep(0.1)
	print("You can always bring this panel back up by typing help")
	time.sleep(0.1)
	print("You are now employed at Google and have 20,000 saved")

	""" Actual Game Loop """
	while GameEnd == False:
		command = input("Type a command: ") 
		if command == '!help':
			print("	!Work: You spend your month entirely working")             #command 1
			print("	!Rest: Earn back some Stamina")                            #command 2
			print("	!Stats: Shows current stats and conditions")               #command 3
			Print("	!Move: Switch to a new company. You lose benefits,")       #command 4
			print("             but get better pay")                                              
			print("	!Retire: Collect savings and end the game")                #command 5
			print("	!Clear: Clears the screen of text")                        #command 6
			print("You can always bring this panel back up by typing help")

		elif command == '!Work': #command 1
			if Stamina >= 5:
				Cash += (Salary/12.00)
				Stamina -= 5
				Months += 1
				TimeAtCompany += 1
				print("You worked hard this month and got paid " + str(Salary/12.00) + " dollars")
				time.sleep(0.1)
				print("You have " + str(Stamina) + " Stamina")
			else:
				print("You are too tired. Take a !Rest")

		elif command == '!Stats': #command 2
			print('Cash: ' + str(Cash))
			print('Stamina: ' + str(Stamina))
			print('Age: '+ str(Age))
			print('Company: ' + str(Company))
			print('TimeAtCompany: ' + str(TimeAtCompany))
			print('CorporateWarnings: ' + str(CorporateWarnings))
			time.sleep(0.1)

		elif command == '!Rest': #command 3
			Months += 1
			TimeAtCompany += 1
			Stamina += 20
			if Stamina > 100:
				Stamina = 100
				CorporateWarnings += 1
			print(" You've rested and recovered 20 Stamina")
			print("You have " + str(Stamina) + " Stamina")
			time.sleep(0.1)

		elif command == '!Move': #command 4
			print("0: " + Companylist[0])
			print("1: " + Companylist[1])
			print("2: " + Companylist[2])
			print("3: " + Companylist[3])
			CompanyNumber = input('Choose A Number:')
			Companylist.append(Company)
			Company = Companylist[int(CompanyNumber)]
			CompanyPay.append(Salary)
			Salary = CompanyPay[int(CompanyNumber)]
			TimeAtCompany = 0
			CorporateWarnings = 0

		elif command == '!Retire': #command 5
			GameEnd = True

		elif command == '!Clear': #command 6
			os.system('cls')

		else:
			print('INVALID COMMAND')

		if Months == 12:
			Months = 0
			Age += 1
			print("A year has passed")
			print("Time to do taxes!")
			Tax = 0.31 * Salary
			CorporateWarnings = CorporateWarnings - 2
			if CorporateWarnings < 0:
				CorporateWarnings = 0
			Cash = Cash - Tax
			print("You paid " + str(Tax) + " in taxes")
			time.sleep(2)
			print("Time to pay for cost of living!")
			Budget = Salary - Tax
			Remaining = Budget * 0.60
			Cash = Cash + Remaining
			print("You saved " + str(Remaining) + " this year")

			time.sleep(2)

		if TimeAtCompany == 12:
			Salary = Salary * 1.15
			for offer in CompanyPay:
				offer = offer * 1.15
			print("You got a 15%% raise!")

		if TimeAtCompany == 24:
			Salary = Salary * 1.25
			for offer in CompanyPay:
				offer = offer * 1.25 
			print("You got a 25% raise!")
			print("You now have Industry Experience!")		

		if TimeAtCompany == 48:
			Salary = Salary * 1.30
			for offer in CompanyPay:
				offer = offer * 1.30  
			print("You got a 30% raise!")

		if TimeAtCompany == 96:
			Salary = Salary * 1.20
			for offer in CompanyPay:
				offer = offer * 1.20 
			print("You got a 20% raise!")
			print("You're an Industry Expert!")		

		if TimeAtCompany == 120:
			Salary = Salary * 1.50
			for offer in CompanyPay:
				offer = offer * 1.50
			print("You got a 50% raise!")

		if TimeAtCompany == 180:
			Salary = Salary * 1.25
			for offer in CompanyPay:
				offer = offer * 1.25
			print("You got a 25% raise!")

		if TimeAtCompany == 240:
			Salary = Salary * 2.00
			for offer in CompanyPay:
				offer = offer * 2.00 
			print("You got a 100% raise!")
			print("You're now the Industry Leader!")

		if CorporateWarnings >= 4:
			print("HR is mad at you for not working")
			print("You're Fired!")
			GameEnd = True

	print("Thank You For Playing!")

start()