import sys

if __name__ == '__main__':

	if len(sys.argv) > 2 or len(sys.argv) < 1:
		print('erreur.')
	else:
		try:
			type(int(sys.argv[1]))
		except:
			print(len(str(sys.argv[1])))
		else:
			print('erreur')