import sys

if __name__ == '__main__':

		if len(sys.argv)<1 or len(sys.argv)>2:
			print("erreur")
		else:
			try:
				type(int(sys.argv[1]))
			except:
				argument = str(sys.argv[1])

				word = ''

				for index in range(len(argument)):
					word = argument[index] + word

				print(word)
			else:
				print('erreur')