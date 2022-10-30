import sys

if __name__ == '__main__':

	try:
		base = int(sys.argv[1])
		exposant = int(sys.argv[2])
	except:
		print('erreur')
	else:
		if exposant >= 0:
			print(base**exposant)
		else:
			print('erreur')