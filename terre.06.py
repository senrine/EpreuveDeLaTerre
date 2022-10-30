import sys

if __name__ == '__main__':

	try:
		argument_01 = int(sys.argv[1])
		argument_02 = int(sys.argv[2])

	except:
		print('erreur')
	else:
		if argument_01 < argument_02 or argument_02 == 0:
			print('erreur.')
		else:
			result = argument_01//argument_02
			reste = argument_01 % argument_02
			print("résultat: ", result, "\nreste: ",reste)