import sys

if __name__ == '__main__':

	try:
		argument = str(sys.argv[1])
		heure = int(argument[0] + argument[1])
		minutes = int(argument[3] + argument[4])
		pm_or_am = str(argument[len(argument) - 2] + argument[len(argument)-1])

	except:
		print("erreur.")

	else:
		if len(argument)<7 or len(argument)>7 or heure==0 or heure>12 or minutes>59:
			print('erreur')

		else:
			if pm_or_am == "pm" or pm_or_am == "PM": 
				pm = True
				am = False

			elif pm_or_am == "am" or pm_or_am == "AM": 
				am = True
				pm = False
			else:
				print('erreur')
				sys.exit()

			if pm:
				if heure == 12:
					print('00',end='')
				else:
					print(heure+12,end='')
			else:
				print(heure,end='')

			for index in range(2,len(argument)-2):
				print(argument[index],end='')

			print(f'\t')