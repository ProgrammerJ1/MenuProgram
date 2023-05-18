import time
import types
import random
import inquirer
import colorama
import datetime
class Grade:
	def __init__(self,Score=0,Points=0) -> None:
		self.Score=Score
		self.Points=Points
	def correct(self,worth: int=1):
		self.Score+=worth
		self.Points+=worth
	def partcredit(self,gotten: int,worth: int):
		self.Score+=gotten
		self.Points+=worth
	def incorrect(self,got: int=1,worth: int=1):
		self.Points+=worth
PointsDictionary={"Math Question":Grade(),"Rotation Question":Grade(),"Logic Question":Grade(),"Guessing Game":Grade(),"One Player Game":Grade(),"Chatbot":Grade()}
ColorsDict={"Black":colorama.Fore.BLACK,"Blue":colorama.Fore.BLUE,"Cyan":colorama.Fore.CYAN,"Green":colorama.Fore.GREEN,"Magenta":colorama.Fore.MAGENTA,"White":colorama.Fore.WHITE,"Yellow":colorama.Fore.YELLOW,"":""}
class User:
	def __init__(self,a:str="User",b:int=-1,c:str=""):
		print(ColorsDict[c])
		self.Name=a
		self.Age=b
		self.FavoriteColor=ColorsDict[c]
UserStats:User=User()

def Printing(String:str,delay:float=0.0625,enddelay:float=1):
	global UserStats
	print(UserStats.FavoriteColor)
	for i in String:
		print(i,end="",flush=True)
		time.sleep(delay)
	time.sleep(enddelay)
def oscillating_animation(name,speed: int=0.1):
    # Set the animation speed (lower value = faster animation)

    # Calculate the number of spaces needed for oscillation
    oscillation_range = len(name) - 1

    # Generate empty spaces to clear the screen
    clear_spaces = " " * len(name)

    # Iterate over the oscillation range back and forth
    for T in range(10):                      # Or "while True:" if you want it to oscillate forever
        for i in range(oscillation_range):
            # Clear the screen by printing empty spaces
            print(clear_spaces, end="\r")

            # Generate the animated name by shifting it to the right
            animated_name = " " * i + name

            # Print the animated name
            print(animated_name, end="\r")

            # Pause the animation for a specific duration
            time.sleep(speed)

        for i in range(oscillation_range, -1, -1):
            # Clear the screen by printing empty spaces
            print(clear_spaces, end="\r")

            # Generate the animated name by shifting it to the right
            animated_name = " " * i + name

            # Print the animated name
            print(animated_name, end="\r")

            # Pause the animation for a specific duration
            time.sleep(speed)
def MathQuestion():
	global PointsDictionary, UserStats
	Choice=0
	Operations=["{}+{}","{}-{}","{}*{}","{}//{}","{}%{}","{}/{}"]
	a=random.randint(1,10)
	b=random.randint(1,10)
	if (Choice==3):
		print("The quotient of {} divided by {}=")
	else:
		Printing(Operations[Choice].format(a,b)+"=")
	c=float(input())
	if c!=eval(Operations[Choice].format(a,b)):
		Printing("Unfortunately, that answer is not correct.\n",enddelay=2)
		Printing("The correct answer is {}, {}\n".format(eval(Operations[Choice].format(a,b)),UserStats.Name))
		if UserStats.Age>20:
			Printing("You should be able to do that, you're {}\n".format(UserStats.Age))
		PointsDictionary["Math Question"].incorrect()
	else:
		Printing("Correct, {}\n".format(UserStats.Name))
		PointsDictionary["Math Question"].correct()
def RotationOption():
	global PointsDictionary, UserStats
	nums=[]
	Size=random.randint(5,10)
	for i in range(Size):
		nums.append(random.randint(1,100))
	Index=random.randint(0,Size-1)
	Direction=random.randint(0,1)
	NumofRots=random.randint(1,Size-1)
	Printing("My list of numbers currently equals {}\n".format(nums))
	Printing("Now I decide to Rotate my list {} times {}\n".format(NumofRots,["left","right"][Direction]),enddelay=2)
	RotResults=[]
	if Direction:
		for i in range(NumofRots):
			nums=nums[-1:] + nums[:-1]
			RotResults.append("Rotation {}: {}, Element {} is {}\n".format(i+1,nums,Index+1,nums[Index]))
	else:
		for i in range(NumofRots):
			nums=nums[1:] + nums[:1]
			RotResults.append("Rotation {}: {}, Element {} is {}\n".format(i+1,nums,Index+1,nums[Index]))
	Printing("I just finished rotating the list.\n",enddelay=2)
	Printing("Now, what is element {} (element 1 is the first element, as we are not using zero indexing) of the new list: ".format(Index+1))
	x=int(input())
	if x==nums[Index]:
		Printing("You are correct, {}".format(UserStats.Name),enddelay=2)
		if UserStats.Age < 10 and UserStats.Age!=-1:
			PointsDictionary["Rotation Question"].partcredit(2,1)
			Printing("I am impressed you got that correct considering your age.\n")
		else:
			PointsDictionary["Rotation Question"].correct()
	else:
		Printing("That is incorrect, {}\n".format(UserStats.Name),enddelay=2)
		Printing("I will show you the rotations\n")
		for i in RotResults:
			Printing(i,enddelay=2)
		if UserStats.Age < 10 and UserStats.Age!=-1:
			Printing("It's alright, I would not expect you to know this stuff considering your age.\n")
		else:
			PointsDictionary["Rotation Question"].incorrect()

def LogicTest():
	def BooleanExpressionGenerator()->str:
		numofnums=random.randint(2,5)
		Numbers=[]
		for i in range(numofnums):
			Numbers.append(random.randint(1,100))
		Operators=[]
		for i in range(numofnums-1):
			Operators.append(["+","-","*","/","%"][random.randint(0,4)])
		BooleanExpression="("
		for i in range(numofnums-1):
			BooleanExpression+=str(Numbers[i])
			BooleanExpression+=str(Operators[i])
		BooleanExpression+=str(Numbers[numofnums-1])
		BooleanExpression+=["==",">","<","<=",">="][random.randint(0,4)]
		BooleanExpression+=str(random.randint(0,100**numofnums))
		BooleanExpression+=")"
		return BooleanExpression

	global PointsDictionary, UserStats
	TestExpression=""
	if (random.randint(0,1)):
		BitwiseSymbol=["&","|","^"][random.randint(0,2)]
		TestExpression=BooleanExpressionGenerator()+BitwiseSymbol+BooleanExpressionGenerator()
	else:
		TestExpression=BooleanExpressionGenerator()
		TestExpression=TestExpression[1:len(TestExpression)-2]
	Correctness=not bool((inquirer.prompt([inquirer.Confirm("answer",message="{}Do you believe the expression {} is true".format(UserStats.FavoriteColor,TestExpression.replace("&"," and ").replace("|"," or ").replace("^"," xor ").replace("=="," equals ").replace("<="," less than or equal to ").replace(">="," greater than or equal to ").replace("<"," less than ").replace(">"," greater than ")))])["answer"])^eval(TestExpression))
	if Correctness:
		Printing("You are correct, {}.\n".format(UserStats.Name),enddelay=2)
		if UserStats.Age < 10 and UserStats.Age!=-1:
			PointsDictionary["Logic Question"].partcredit(2,1)
			Printing("{}, I am impressed you got that correct considering your age.\n".format(UserStats.Name))
		else:
			PointsDictionary["Logic Question"].correct()
	else:
		Printing("You are unfortunately incorrect, {}.".format(UserStats.Name),enddelay=2)
		if UserStats.Age < 10 and UserStats.Age!=-1:
			Printing("It's alright, I would not expect you to know this stuff considering your age.")
		else:
			PointsDictionary["Logic Question"].incorrect()
def SlowMoTextDisplay():
	Printing("How many times would you like to print your string, {}?: ".format(UserStats.Name))
	NumberofTimestoPrint=int(input())
	Printing("Enter your string: ")
	String=input()
	for i in range(NumberofTimestoPrint):
		Printing("Enter in seconds how long you want to wait before printing another character: ")
		chardelay=float(input())
		Printing("Enter in seconds how long you want to wait at the end: ")
		afterdelay=float(input())
		oscillating_animation(String,chardelay)
		time.sleep(afterdelay)
def GuessingGame():
	global PointsDictionary, UserStats
	Num=random.randint(0,100)
	Printing("I have a number in my head from 0-100 in my head, what is it?: ".format(Num))
	GuessedNum=int(input())
	if GuessedNum==Num:
		Printing("Correct, you get a point, {}\n".format(UserStats.Name))
		PointsDictionary["Guessing Game"].correct()
	else:
		Printing("Incorrect, the number was {},{}\n".format(Num,UserStats.Name))
		PointsDictionary["Guessing Game"].incorrect()
def PersonalInformation()->bool:
	global PointsDictionary, UserStats
	Printing("What is your name: ")
	Name=input()
	Age=-1
	if UserStats.Age==-1:
		Printing("What is your age: ")
		Age=int(input())
	else:
		Age=UserStats.Age
	Printing("What is your favorite color: ")
	FavColor=inquirer.prompt([inquirer.List("color",message="What is your favorite color?: ",choices=["Black", "Blue", "Cyan", "Green", "Magenta", "White", "Yellow"])])["color"]
	UserStats=User(Name,Age,FavColor)
	return "Tell me about yourself"
def OnePlayerGame():
	global PointsDictionary, UserStats
	ComparisonOperators=["==",">","<",">=","<="]
	ComparisonIndex=random.randint(0,4)
	ComparisonOperator=ComparisonOperators[ComparisonIndex]
	a=0
	b=random.randint(0,100)
	Printing("I have a number from 0-100 in my head, your number has to be {} mine, and it has to be in my range\n".format([" equal to "," greater than "," less than "," greater than or equal to "," less than or equal to "][ComparisonIndex]),enddelay=2)
	Printing("Enter your number: ")
	a=int(input())
	if 0>a or a>100:
		Printing("You do not get to use an invalid number you cheater!!! ",enddelay=2)
		Printing("Cheater {}".format(UserStats.Name))
		PointsDictionary["One Player Game"].incorrect(2)
	elif (eval("a{}b".format(ComparisonOperator))):
		Printing("You succeeded, my number was {}, {}".format(a,UserStats.Name), enddelay=2)
		PointsDictionary["One Player Game"].correct()
	else:
		Printing("You unfortunately failed, my number was {}".format(a,UserStats.Name), enddelay=2)
		PointsDictionary["One Player Game"].incorrect()
def Chatbot()->str:
	Greetings=""
	
	currenthour=datetime.datetime.now().hour
	
	if currenthour>=6 and currenthour<12:
		Greetings="Good morning"
	elif currenthour>=12 and currenthour<18:
		Greetings="Good afternoon"
	else:
		Greetings="Good evening"
	
	Questions=["How are you feeling today?","How many siblings do you have?","How many pets do you have?","What color is your hair?","How old are you?","What is your favorite animal?","What is your favorite sport to watch?","What country would you like to visit next?","What is your favorite color?","What is your favorite number?"]
	
	def Dots(x=3):
		Printing("."*x,delay=0.5)
	
	def FeelingRes():
		global PointsDictionary
		Points=0
		Printing("{}, {}. {}: ".format(Greetings,UserStats.Name,Questions[0]))
		Feeling: str=input()
		StrongPosRes=["better than yesterday","happy","amazing",]
		PosRes=["good","fine"]
		NeutralRes=["ok","alright"]
		NegativeRes=["sad"]
		StrongNegativeRes=["depressed"]
		if Feeling.lower() in StrongPosRes:
			Points=3
			Printing("Very nice")
		elif Feeling.lower() in PosRes:
			Printing("Glad to hear that.")
			Points=2
		elif Feeling.lower() in NegativeRes:
			Printing("I am sorry to hear that, {}.".format(UserStats.Name))
			Points=2
		elif Feeling.lower() in NeutralRes:
			Printing("Alright then.")
			Points=1
		elif Feeling.lower() in StrongNegativeRes:
			Points=3
			Printing("I am so sorry hear that, {}.".format(UserStats.Name))
		else:
			Dots()
			Printing("🙄")
			time.sleep(0.5)
			Printing("Next Question")
		PointsDictionary["Chatbot"].partcredit(Points,3)
	
	def Sibs():
		global PointsDictionary
		Points=0
		NumofSibs: int
		
		SibsRes=["You're not very bright are you.","Whatever, if you don't want to answer this question let's move on.","Ah, an only child. I never thought I would meet one of my own, ","well not exactly, but I might as well be one.","So you have a sibling, I don't live with mine.","So you have {} siblings. I don't live with my siblings. They are already adults who have their own lives."]
		Printing("{}: ".format(Questions[1]))
		try:
			NumofFrats=input()
			x=int(NumofFrats)
		except ValueError:
			if PointsDictionary["Chatbot"].Score==0:
				Dots()
				print(SibsRes[0])
			else:
				Dots()
				Printing(SibsRes[1])
		else:
			NumofSibs=x
			if NumofSibs<0:
				Dots()
				Printing(SibsRes[1])
			elif NumofSibs==0:
				Printing(SibsRes[2])
				time.sleep(0.5)
				Printing(SibsRes[3])
				Points=2
			elif NumofSibs==1:
				Printing(SibsRes[4])
				Points=1
			else:
				Printing(SibsRes[5].format(NumofSibs))
		PointsDictionary["Chatbot"].partcredit(Points,2)
	
	def Pets():
		global PointsDictionary
		Points=0
		PetsRes=["I HATE YOU! ","Why did you waste my time!","Well I guess the place where you keep your pets made a deal with the universe to allow it to defy reality to for you to keep {} amount of pets","Well I guess the place where you keep your pets made deal with the universe to allow it to defy reality to allow to keep {} amount of pets","Ah you are petless like me.","Cherish your single pet.","Cherish your pets."]
		Pets: int
		Printing("{}: ".format(Questions[2]))
		try:
			NumofAnimals=input()
			x=int(NumofAnimals)
		except ValueError:
			if PointsDictionary["Chatbot"].Score==0:
				Dots()
				for i in range(3):
					Printing(PetsRes[0],delay=0.5)
				Printing(PetsRes[1])
			else:
				Printing(PetsRes[2].format(NumofAnimals))
		else:
			Pets=x
			if Pets<0:
				Dots()
				Printing(PetsRes[3].format(NumofAnimals))
			elif Pets==0:
				Printing(PetsRes[4])
				Points=2
			elif Pets==1:
				Printing(PetsRes[5])
				Points=1
			else:
				Printing(PetsRes[6])
				Points=1
		PointsDictionary["Chatbot"].partcredit(Points,2)
	
	def HairColorFunc():
		global PointsDictionary
		Points=0
		UsualHairColor=["brown","blonde","red","black"]
		BaldingHairColor=["white","gray"]
		UnusualHairColor=["blue","green","yellow","purle"]
		Printing("{}: ".format(Questions[3]))
		HairColor=input()
		if HairColor in UsualHairColor:
			Points=2
			Printing("A great hair color")
		elif HairColor in BaldingHairColor:
			Points=2
			print("I'm sorry that you are balding.")
		elif HairColor in UnusualHairColor:
			Printing("Hm, interesting, are you really. That's unusual")
			Points=1
		else:
			if PointsDictionary["Chatbot"].Score==0:
				Printing("DIDN\'T YOUR FAMILY TEACH YOU TO NOT WASTE PEOPLE\'S TIME!!!!!\n",0.125)
			else:
				Printing("That's not even a color, my dopey conversation partner")
		PointsDictionary["Chatbot"].partcredit(Points,2)
	def Age():
		global PointsDictionary
		Points=0
		Age: int
		try:
			Printing("{}: ".format(Questions[4]))
			NumofYears=input()
			x=int(NumofYears)
		except ValueError:
			if PointsDictionary["Chatbot"].Score==0:
				Dots(6)
			else:
				Printing("You physically cannot be {} age".format(NumofYears))
		else:
			UserStats.Age,Age=x
			if Age<0:
				Printing("You cannot be a negative age but whatever")
			elif Age<=0 and Age>=3:
				Printing("I cannot believe a baby knows how to use technology, you are a liar")
			elif Age<=4 and Age>=12:
				Printing("Your still a child, like I once was")
				Points=1
			elif Age==13 or (Age<=15 and Age>=17):
				Printing("Your a teenager like me")
				Points=2
			elif Age==14:
				Printing("Your my age")
				Points=3
			else:
				Printing("Your an adult, that's nice, you get freedom.")
			PointsDictionary["Chatbot"].partcredit(Points,3)
	def FavAnimalFunc():
		global PointsDictionary
		Points=0
		FavAnimals=["lions", "leopards", "elephants", "rhinos", "buffalos","lion", "leopard", "elephant", "rhino", "buffalo"]
		Printing("{}: ".format(Questions[5]))
		FavoriteAnimal=input()
		if FavoriteAnimal in FavAnimals:
			Printing("Wow, good choice")
			Points=1
		else:
			if PointsDictionary["Chatbot"].Score==0:
				Printing("Wow, the animal is lame like you")
			else:
				Printing("Wow, lame")
			Printing("You have bad taste.")
		PointsDictionary["Chatbot"].partcredit(Points,1)
	def Sports():
		global PointsDictionary
		Points=0
		FavoriteSport1=["baseball","volleyball","soccer","lacrosse"]
		FavoriteSport2=["football","rugby","golf"]
		Printing("{}: ".format(Questions[6]))
		FavoriteSport=input()
		if FavoriteSport in FavoriteSport1:
			Points=2
			Printing("Wow, nice choice!")
		elif FavoriteSport in FavoriteSport2:
			Points=1
			Printing("Interesting choice, though not my favorite")
		else:
			if PointsDictionary["Chatbot"].Score==0:
				Dots(18)
				Printing("You should have spent your skill points on grey matter for your brain, because it lacks it.\n",delay=0.125)
			else:
				Printing("Lame sport")
		PointsDictionary["Chatbot"].partcredit(Points,2)
	
	def FavCountry():
		global PointsDictionary
		Points=0
		Countries2=["Italy","France","Spain"]
		Countries3=["Thailand","Germany","India"]
		Printing("{}: ".format(Questions[7]))
		Country=input()
		if Country=="United States":
			Points=4
			Printing("I actually live in the United States of America!")
		elif Country=="Greece":
			Points=3
			Printing("I actually am going to Greece at the time of writing this program")
		elif Country in Countries2:
			Points=2
			Printing("That's a nice tourist destination")
		elif Country in Countries3:
			Points=1
			Printing("Interesting choice")
		elif PointsDictionary["Chatbot"].Score==0:
			Printing("😡"*94,delay=0.125)
		else:
			if PointsDictionary["Chatbot"].Score==0:
				Printing("YYYYYYYYYYEEEEEEEEEEEESSSSSSSSSSSS!!!!!!!!!!!!!\n",0.125,0.25)
				Printing("Just one more question before I can give my verdict and stop talking to you\n",0.125)
			Printing("You have bad taste.")
		PointsDictionary["Chatbot"].partcredit(Points,4)
	
	def FavNumber():
		global PointsDictionary
		Points=0
		FavNumb: float
		try:
			Printing("{}: ".format(Questions[9]))
			FavNum=input()
			x=float(FavNum)
		except ValueError:
			if PointsDictionary["Chatbot"].Score==0:
				Dots(25)
				Printing("Finally, ",end="",flush=True)
				
				Printing("It's over",flush=True)
			else:
				Printing("That is no number")
		else:
			FavNumb=x
			if FavNumb==18:
				Printing("That's my favorite number too!")
				Points=2
			else:
				Printing("Thats an intersting choice, for favorite number")
				Points=1
		PointsDictionary["Chatbot"].partcredit(Points,2)
	FeelingRes()
	Sibs()
	Pets()
	HairColorFunc()
	if UserStats.Age==-1:
		Age()
	else:
		PointsDictionary["Chatbot"].correct(3)
	FavAnimalFunc()
	Sports()
	FavCountry()
	FavNumber()
	if PointsDictionary["Chatbot"].Score<9:
		Printing("Well, this was a nightmare, thank you for being my conversation partner. ",0.125,2)
		Printing("Now get out of here.",0.5,2)
	elif PointsDictionary["Chatbot"].Score<18:
		Printing("This was a pleasant conversation")
	elif PointsDictionary["Chatbot"].Score<21:
		Printing("This was an enjoyable chat. I hope to talk to you again")
	else:
		Printing("You might be potential best friend material.")
	return "Talk to a chatbot"

def Quit():
	global PointsDictionary, UserStats
	Printing("You got a {}/{} on answering math questions\n".format(PointsDictionary["Math Question"].Score,PointsDictionary["Math Question"].Points))
	Printing("You got a {}/{} on answering rotations questions\n".format(PointsDictionary["Rotation Question"].Score,PointsDictionary["Rotation Question"].Points))
	Printing("You got a {}/{} on answering logic questions\n".format(PointsDictionary["Logic Question"].Score,PointsDictionary["Logic Question"].Points))
	Printing("You got a {}/{} on guessing numbers\n".format(PointsDictionary["Guessing Game"].Score,PointsDictionary["Guessing Game"].Points))
	Printing("You got a {}/{} on advanced guessing\n".format(PointsDictionary["One Player Game"].Score,PointsDictionary["One Player Game"].Points))
	Printing("You got a {}/{} on talking to the chatbot\n".format(PointsDictionary["Chatbot"].Score,PointsDictionary["Chatbot"].Points))
	GlobalGrade=Grade(PointsDictionary["Math Question"].Score+PointsDictionary["Rotation Question"].Score+PointsDictionary["Logic Question"].Score+PointsDictionary["Guessing Game"].Score+PointsDictionary["One Player Game"].Score+PointsDictionary["Chatbot"].Score,PointsDictionary["Math Question"].Points+PointsDictionary["Rotation Question"].Points+PointsDictionary["Logic Question"].Points+PointsDictionary["Guessing Game"].Points+PointsDictionary["One Player Game"].Points+PointsDictionary["Chatbot"].Points)
	Printing("In total you got a {}/{} for tasks with points.\n".format(
        GlobalGrade.Score,GlobalGrade.Points
    ))
	if GlobalGrade.Points==0 and GlobalGrade.Score==0:
		Printing("Hey, wait a minute. Why did you call me up to do nothing with me.",0.03125,5)
		Printing("Whatever")
	elif GlobalGrade.Score/GlobalGrade.Points>=0.8 and UserStats.Age<10:
		Printing("That is impressiving for your age",enddelay=5)
	Printing("Anyway, thank you for your time.")
	Printing("Goodbye, {}\n".format(UserStats.Name))
	print(colorama.Fore.RESET)
	print(colorama.Back.RESET)
	exit(0)
def Menu():
	OptionsDict={
		"Answer a math question for a point":MathQuestion,
		"Answer a rotation question for a point":RotationOption,
		"Answer a logic question":LogicTest,
		"Print your text in slow motion":SlowMoTextDisplay,
		"Guess a number for a point":GuessingGame,
		"Tell me about yourself":PersonalInformation,
		"Play a game with advanced guessing": OnePlayerGame,
		"Talk to a chatbot":Chatbot,
		"Quit":Quit
	}
	Printing("Welcome to the J Menu\n",enddelay=2)
	while True:
		answer: str=str(inquirer.prompt([inquirer.List("Option",message="{}What would would you like to do?".format(UserStats.FavoriteColor),choices=OptionsDict.keys())])["Option"])
		returnres=OptionsDict[answer]()
		if returnres:
			if returnres=="Tell me about yourself":
				OptionsDict.pop(returnres)
				OptionsDictKeys=[]
				for i in OptionsDict.keys():
					OptionsDictKeys.append(i)
				for i in OptionsDictKeys:
					OptionsDict[UserStats.FavoriteColor+i]=OptionsDict.pop(i)
			else:
				OptionsDict.pop(UserStats.FavoriteColor+returnres)
Menu()



'''
Menu #1 - A menu with 5 options (including a quit option). 
One of the options must be mathematical in nature (basic calculator, tip calculator, grade calculator, etc…)
One of the options must involve lists
One of the options must involve conditional statements (ifs, elses, elifs)
One of the options must involve loops

Menu #2 - A menu with 7 options (including a quit option).
All five options from Menu #1, plus
An option that involves some sort of guessing game
Something that gets personal information from the user like name, age, favorite color, etc… and uses it throughout all programs

Menu #3 - A menu with 9 options (including a quit option).
All seven options from Menu #2, plus
An option that involves a one-player game like rock, paper, scissors
An option that includes a simple chatbot
'''
