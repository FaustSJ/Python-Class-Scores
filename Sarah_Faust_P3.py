#-------------------------------------------------------------------------------
# Student Name: Sarah Faust / Assignment: P #3 / Date: 09/23/2012
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: Notes and class owerpoints
#-------------------------------------------------------------------------------
# Comments: 
#-------------------------------------------------------------------------------
# Pseudocode: 
# BEGIN
#	Answer = 11
#	while Answer != 7:
#		while Answer is not 0 through 7:
#				print menu
#			Answer = user input
#		if Answer==0:
#			Score_list=[]
#		if Answer==1:
#			Score_num=-1
#			while Score_num<0
#				Score_num=ask user for amount of scores
#			for i in range(1:Score_num+1):
#				Value=user inputs a score
#				Score_list + Value
#		if Answer==2:
#			print length of Score_list
#			for i in range(0:length of Score_list):
#				print \t Score_list[i]
#		if Answer==3:
#			ScoreSum=0
#			for i in range(0:length of Score_list):
#				ScoreSum=ScoreSum+Score_list[i]
#			ScoreAverage=ScoreSum/length of Score_list
#			print ScoreAverage
#		if Answer==4:
#			ScoreSum=0
#			for i in range(0:length of Score_list):
#				ScoreSum=ScoreSum+Score_list[i]
#			ScoreAverage=ScoreSum/length of Score_list
#			StandardDev=0
#			for i in range(0:length of Score_list):
#				StandardDev += (Score_list[i] - ScoreAverage)**2
#			StandardDev = (StandardDev/Length of Score_list)**(1/2)
#			print StandardDev
#		if Answer==5:
#			ScoreMax=max(Score_list)
#			CountMax=0
#			for i in range(0:length of Score_list)
#				if Score_list[i]==ScoreMax
#					CountMax+=1
#			print ScoreMax and CountMax
#		if Answer==6:
#			ScoreMin=min(Score_list)
#			CountMin=0
#			for i in range(0:length of Score_list)
#				if Score_list[i]==ScoreMin:
#					CountMin+=1
#			print ScoreMin and CountMin
#		print Menu
#		Answer = 11
#		while Answer is not 0 through 7:
#			Answer = user input
# END
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------

# Sets up the score list of the program and a variable to start the program with
Score_list=[]
Answer = 11
while Answer != 7:
	
# Prints the menu and prompts for a selection
	while Answer<0 or Answer>7:
		print ("0 - clear out scores")
		print ("1 - input more scores")
		print ("2 - display all scores")
		print ("3 - get average score")
		print ("4 - get standard deviation of scores")
		print ("5 - get high score")
		print ("6 - get low score")
		print ("7 - quit")
		Answer = int(input("What option from above do you choose? "))
		print ("------------------------------")
		print ("------------------------------")
		
# If the variable = 0, delete all the scores
	if Answer==0:
		Score_list=[]
		
# If the variable = 1, allow the user to add scores to the score list
	if Answer==1:
		Score_num=-1
		while Score_num<0:
			Score_num=int(input("How many scores will be entered? "))
		temp=list(range(Score_num))
		for i in range(0,Score_num):
			temp[i]=eval(input("> "))
		Score_list=Score_list + temp
		
# If the variable = 2, print the list of scores for the user to see
	if Answer==2:
		print ("There are ",len(Score_list)," scores:")
		for i in range(0,len(Score_list)):
			print ("\t", Score_list[i])
			
# If the variable = 3, average the scores and show the average to the user
	if Answer==3:
		if len(Score_list)<1:
			print("There aren't any scores yet!")
		else:
			ScoreSum=0
			for i in range(0,len(Score_list)):
				ScoreSum += Score_list[i]
			ScoreAverage=ScoreSum/len(Score_list)
			print ("Average score: ", ScoreAverage)
		
# If the variable = 4, the standard deviation of the scores is calculated
# and shown to the user
	if Answer==4:
		if len(Score_list)<1:
			print("There aren't any scores yet!")
		else:
			ScoreSum=0
			for i in range(0,len(Score_list)):
				ScoreSum += Score_list[i]
			ScoreAverage=ScoreSum/len(Score_list)
			StandardDev=0
			for i in range(0,len(Score_list)):
				StandardDev += (Score_list[i] - ScoreAverage)**2
			StandardDev = (StandardDev/len(Score_list))**(1/2)
			print ("Standard deviation: ", StandardDev)
		
# If the variable = 5, the maximum score is found and a for loop counts how
# often it occurs in the list of scores, then tells the user the max and
# how much it's repeated
	if Answer==5:
		if len(Score_list)<1:
			print("There aren't any scores yet!")
		else:
			ScoreMax=0
			for i in range(0,len(Score_list)):
				if Score_list[i]>ScoreMax:
					ScoreMax=Score_list[i]
			CountMax=0
			for i in range(0,len(Score_list)):
				if Score_list[i]==ScoreMax:
					CountMax+=1
			print ("High score: ", ScoreMax)
			print (CountMax, " people got this score.")
		
# If the variable = 6, the minimum score is found and a for loop counts how
# often it occurs in the list of scores, then tells the user the min and
# how much it's repeated
	if Answer==6:
		if len(Score_list)<1:
			print("There aren't any scores yet!")
		else:
			ScoreMin=999999999999999999999999999
			for i in range(0,len(Score_list)):
				if Score_list[i]<ScoreMin:
					ScoreMin = Score_list[i]
			CountMin=0
			for i in range(0,len(Score_list)):
				if Score_list[i]==ScoreMin:
					CountMin+=1
			print ("Low score: ", ScoreMin)
			print (CountMin, " people got this score.")
		
# If the variable = 7, the program ends
	if Answer==7:
		print("Goodbye!")	
		
# If the program doesn't end, the menu is reprinted and the user is prompted
# for another command
	if Answer !=7:
		print ("------------------------------")
		print ("------------------------------")
		print ("0 - clear out scores")
		print ("1 - input more scores")
		print ("2 - display all scores")
		print ("3 - get average score")
		print ("4 - get standard deviation of scores")
		print ("5 - get high score")
		print ("6 - get low score")
		print ("7 - quit")
		Answer = 11
		while Answer<0 or Answer>7:
			Answer = int(input("What option from above do you choose? "))
			print ("------------------------------")
			print ("------------------------------")
			if Answer==7:
				print("Goodbye!")








