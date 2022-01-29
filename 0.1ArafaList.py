#!/usr/bin/python3

#Libraries
import random
from colorama import *
import os
class bcolors:
	GREEN = '\033[92m'
	ENDC = '\033[0m'
	FAIL = '\033[91m'
#Clear the terminal
os.system("clear")
#Banner and about Author
print(bcolors.GREEN + '''

░█████╗░░░░░░███╗░░░█████╗░██████╗░░█████╗░███████╗░█████╗░
██╔══██╗░░░░████║░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗				2021/08/30
██║░░██║░░░██╔██║░░███████║██████╔╝███████║█████╗░░███████║				Author: Abd Almoen Arafa
██║░░██║░░░╚═╝██║░░██╔══██║██╔══██╗██╔══██║██╔══╝░░██╔══██║				Country: Syria
╚█████╔╝██╗███████╗██║░░██║██║░░██║██║░░██║██║░░░░░██║░░██║				Age: 15
░╚════╝░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝
''' + bcolors.ENDC)
print(Fore.YELLOW + '''
					\_/_______________________________\_/
					 |				   |
		   		         |   Make your own huge Wordlist   |
					 |				   |
					 -----------------------------------
''')
def content():
	print(Fore.BLUE + ''' ''')
	try:
		#File to save
		ask_file= input("Enter the name of txt file without deleting the content or create a new one,without .txt: ")
		file= open(ask_file, "a")
		yourchoice= input("Enter the begging of Sentence(Symbols,Letters,Numbers...): ")
		ran1= int(input("Enter the lowest number: "))
		ran2= int(input("Enter the highest number + 1: "))
		end= input("Enter anything in the end if you want(Symbols,Letters,Numbers,...: ")
		ran= input("Do you want to add numbers or guess on phone number? (Y,N): ")
		list= ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
		if ran.lower() == "y" or ran.lower() == "yes" or ran.lower() == "yep":
			call= str(input("Enter the country calling code without + or with + as you like: "))
			many= int(input("How many numbers you want to add: "))
			putting= input("Do you want to add the guessing on phone number or numbers in the begging of Sentence or in the end? (begging,end): ")
			if putting.lower() == "end":
				for i in range(ran1,ran2):
					for n in list:
						guess= random.choices(list,k= many)
						answer= "".join(guess)
						file.write(f"{yourchoice}{i}{end}{call}{answer}" + "\n" + f"{yourchoice.lower()}{i}{end.lower()}{call}{answer}" + "\n" + f"{yourchoice.upper()}{i}{end.upper()}{call}{answer}" + "\n")
			else:
				for i in range(ran1,ran2):
					for n in list:
						guess= random.choices(list,k= many)
						answer= "".join(guess)
						file.write(f"{call}{answer}{yourchoice}{i}{end}" + "\n" + f"{call}{answer}{yourchoice.lower()}{i}{end.lower()}" + "\n" + f"{call}{answer}{yourchoice.upper()}{i}{end.upper()}" + "\n")
		else:
			for i in range(ran1,ran2):
				file.write(f"{yourchoice}{i}{end}" + "\n" + f"{yourchoice.lower()}{i}{end.lower()}" + "\n"  + f"{yourchoice.upper()}{i}{end.upper()}" + "\n")
		file.close()
		print(bcolors.GREEN + "Completed successfully ;)" + """

	      (¯`v´¯)
	       •.¸.•
	    ¸.•´
	   (
	☻/
	/▌
	/ \			""" + bcolors.ENDC)
	except ValueError:
		content()
	except FileNotFoundError:
		print(bcolors.FAIL + "Make sure you're writing the right path" + bcolors.ENDC)
		content()
	except KeyboardInterrupt:
		print(bcolors.GREEN + "\nBye!!" + bcolors.ENDC)
content()
#I hope to be useful for everyone
