import random

wantRun = True
wantRun2=True
wantRun3=True

l1=[]
l2=[]

def rand():
	global n1,n2,n3,n4,strn,n,nr,randlist,marks,Nlist,Nchance,count
	marks=0
	n1=random.randint(1,6)
	n2=random.randint(1,6)
	n3=random.randint(1,6)
	n4=random.randint(1,6)
	strn=(str(n1)+str(n2)+str(n3)+str(n4))
	nr=[]
	randlist=[]
	Nlist = ["1","2","3","4","5","6"]
	Nchance = 1
	count=0
	for i in range (4):
		randlist.append(strn[i])


Sname = input("Enter your Name : ")

while wantRun :
	while wantRun3:
		rand()
		print(randlist)  # print generated 4 digits###################### 
		
		print("\n\n\t\t\tHi "+Sname+ " Welcome to GameInt\n")

		print("Number to Guess - X X X X \t \t Color Mapping :")
		
		print("\t\t\t\t\t\t1-White 2-Blue 3-Red \n\t\t\t\t\t\t4-Yellow 5-Green 6-Purple")
		
		print("Attempt No\t\tGuess\t\tResult\n")

		while Nchance<=8:
			try:
				attempt=input(str(Nchance)+"\t\t\t")
				intA=int(attempt)
				strA=attempt
				if strA[0]=="0" and strA[1]=="0" and strA[2]=="0" and strA[3]=="0":
					print("\n"+("__"*40)+("\n"))
					print("\t\t\tThank you !!!")
					wantRun=False
					wantRun3=False
					wantRun2=False
					break

				
				if len(str(attempt))!=4:
					print("You Can Enter only 4 Digit Number from Color Mapping !\n")
				else:
					try:
						count=0

						for j in range(4):
							if str(attempt)[j] in Nlist:
								count +=1
						if count==4:
							for i in range(4):
								if str(attempt)[i] in Nlist:
									if str(attempt)[i] in randlist:
										if str(attempt)[i]== randlist[i]:
											nr.append("1")
										else:
											nr.append("0")
									else:
										nr.append(".")
							print( "  \t\t\t\t\t"+nr[0] +" "+nr[1])
							print( "  \t\t\t\t\t"+nr[2] +" "+nr[3])
						

						else:
							print("\nYou Can Enter 4 Digit Number & each one Number between 1-6 \n")
			
						if nr[0] == "1" and nr[1]=="1" and nr[2]=="1" and nr[3]=="1":
							print("\nCongratulations!!!!!     You have won the game...\n")
							marks=100-(Nchance-1)*10
							print("You have scored "+str(marks)+" points.\n")
							Nchance=1
							wantRun3=False
							wantRun2=True
							break

						else:
							if Nchance==8:
								print("\nOops!!!! You have lost the game.. ")
								print("You have scored "+str(marks)+" points.\n")
								wantRun3=False
								wantRun2=True
								break
					except:
						print("you entered an out of range number! \n ")
				
			
					nr.clear()		
					Nchance+=1
				
					print("\n"+("__"*40)+("\n"))		
			except:
				print("Wrong character type ! you must enter 'positive intiger' type data\n")
				
#####################################   Run Again      ##############################################
				
		while wantRun2:
			runAgain=input("Do you want to play another game (Yes/No) : ")
			if runAgain.lower()== "no" or runAgain.lower()=="yes":
				if runAgain.lower()=="no":
					print("\n"+("__"*40)+("\n"))
					print("\t\t\tThank you !!!")
					wantRun=False
					wantRun2=False
					break
				elif runAgain.lower()=="yes":
					wantRun2=False
					wantRun3=True
					Nchance=1
					break
			elif runAgain.lower()!= "no" or runAgain.lower()!="yes":
				print("You can only input 'yes' or 'no'\n")

