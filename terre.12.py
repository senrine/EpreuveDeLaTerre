import sys

if __name__ == '__main__':

	try:
		argument = str(sys.argv[1])
		heure = int(argument[0] + argument[1])
		minutes = int(argument[len(argument)-2] + argument[len(argument) - 1])

	except:
		print('erreur')

	else:
		if len(argument)<5 or len(argument)>5 or minutes>59 or heure>23 or argument[2] != ':':
			print('erreur')
		else:

			if heure > 12 or heure == 0:
				pm = True
				am = False
			else:
				am = True
				pm = False

			if heure == 0:
				print(heure+12,end='')

			elif heure <= 12:
				print(heure,end='')

			else:
				print(heure-12,end='')

			for index in range(2,len(argument)):
				print(argument[index],end='')

			if pm:
				print(f'PM\t')
			elif am:
				print(f'AM\t')