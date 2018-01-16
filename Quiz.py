#Farzyab Gohar
#Program purpose: Simple quiz of 10 questions


list1 = [[1, "What is 2+2? ", -1, ["a. 3", "b. 7", "c. 4"], 3], [2, "If you have one bucket that holds 2 gallons, and another bucket that holds 5 gallons, how many buckets do you have?", -1, ["a. 1", "b. 2", "c. 3"], 2], [3, "When you hear the fire alarm you", -1, ["a. Accept your fate", "b. Run", "c. Cry in fetal position"], 2], [4, "Chickens are", -1, ["a. Descended from dinosaurs", "b. Descended from penguins", "c. Secretly plotting to take over the world"], 1], [5, "This is", -1, ["a. A multiple choice question", "b. A talking potato", "c. A chinese proverb"], 1], [6, "The famous quote: ""When anger rises, think of the consequences"" was said by", -1, ["a. Jake from state farm", "b. Confucius", "c. Eminem"], 2], [7, "Generally, when coding, it's a good idea to", -1, ["a. Stare at the screen until the program works", "b. Pay some kid in China to write it", "c. Comment your code"], 3], [8, "Malaria is spread by", -1, ["a. Mosquitoes", "b. Matt", "c. Microwaves"], 1], [9, "When you're drinking alcohol, it's a good idea to", -1, ["a. Stay hydrated", "b. Let the existential dread set in", "c. Question your life choices"], 1], [10, "How many moons does the Earth have?", -1, ["a. 2", "b. 3", "c. 1"], 3]]

list2 = [[1, "1 + 1 is 2. True or False?", -1, True], [2, "The Sun is a Star. True or False?", -1, True], [3, "The Earth is a Star. True or False?", -1, False], [4, "Beef comes from chickens. True or False?", -1, False], [5, "China is in Asia. True or False?", -1, True]]



retake = "yes"	#initialise retake
flag = True	#The point of this flag is to check if the user has completed all the questions

while retake == "yes": #This loop runs until the user enters anything other than "yes" for the variable retake
	score = 0	#Score needs to initialise to 0 every time the user retakes the quiz
	percentage = 0 #Percentage needs to initialise every time the user retakes the quiz
	for i in range(0, 10): #this loop will loop through all the questions in list 1. Since list has 10 questions, the stop value needs to be 10.
		print() #printing a new line for aesthetic reasons.
		print("   ", "Question", list1[i][0], ":", list1[i][1], "\n\t", list1[i][3][0], "\n\t",list1[i][3][1], "\n\t", list1[i][3][2])	#This function will print out 3 empty spaces (aesthetic reasons), the question number(0) of the question the loop is currently in, the question itself(1), and the multiple choices(3(0)) to (3(2))
		
		answer = input() #gets users answer
		answer = answer.lower()
		if answer == "a":  #this control statement here is to check which letter output the user enters, and stores the equivalent integer value in the space in list1 which is for storing the user's answers.
			list1[i][2] = 1
		elif answer == "b":
			list1[i][2] = 2
		elif answer == "c":
			list1[i][2] = 3
		else:	#validation check
			print("Wrong input. Please choose either a, b or c")
		
		if list1[i][4] == list1[i][2]:	#Checks if user answer equals the right answer, and then increases user's score by 1
			score = score + 1
		
		if not(i == 9):	#I put this here since there's no need to ask the user if he wants to quit when he's answered the last question.
			quit = input("Quit?: ")
			quit = quit.lower()
		
		if quit == "yes":	#if the user quits after a question, flag is set to false (so score isn't displayed), retake is set to "no" (So user isn't asked if he wants to take the quiz again), and break command is passed so the for loop breaks. 
			flag = False
			retake = "no"
			break

	if flag == True: #Since we only need to display the user's score when he complete's the quiz, flag will remain true only if he completes all the questions. If user has done all the questions, then the score will be displayed and he'll be asked if he wants to take the quiz again.
		percentage = round((score / 10) * 100)
		print()	#Aesthetic reasons
		print ("You got ", percentage, "% of the questions correct!")	#prints the percentage score
		retake = input("Would you like to take the test again?: ") #asks if user wants to take the test again
		retake = retake.lower()

retake = "yes" #initialise retake
flag = True #initialise flag. I reused these two variables since They're not being used by the first loop after the first quiz ends.
		
while retake == "yes": #Repeat loop if user wants to retake quiz
	score = 0 #initialise. 
	percentage = 0
	print("Quiz 2 starts here: ") 
	for i in range(0, 5): #will loop through all questions in list 2
		print()
		print("   ", "Question", list2[i][0], ":", list2[i][1]) #prints question number, and then the question itself.
		
		answer = input() #gets user answer
		answer = answer.lower()
		if answer == "true": #stores True if user inputs "true" and False if user enters "false"
			list2[i][2] = True
		elif answer == "false":
			list2[i][2] = False
		else: #Validation
			print("Invalid input. Only True and False accepted")
		 
		if list2[i][3] == list2[i][2]: #increments score by 1 if user answer is right
			score = score + 1
		
		if not(i == 4):  #don't need to ask user if he wants to quit quiz if he's already answered the last question
			quit = input("Quit?: ")
			quit = quit.lower()
		
		if quit == "yes": #if user quits, flag is set to false
			flag = False
			retake = "no"
			break #breaks out of foor loop

	

	if flag == True:	#if user answered all questions, then flag will remain true and user score as a percentage will be displayed
		percentage = round((score / 5) * 100) #rounding the score
		print()
		print ("You got ", percentage, "% of the questions correct!")
		retake = input("Would you like to take the test again?: ")
		retake = retake.lower()
