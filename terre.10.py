import sys

if __name__ == '__main__':

	try:
		number = int(sys.argv[1])

	except:
		print("erreur")

	else:

		if len(sys.argv) < 2 or len(sys.argv)>2:
			print("erreur.")
			sys.exit()

		if number <=1 and number>=0:
			print(number)
			sys.exit()

		elif number <0:
			print("Rentrez un entier positif...")
			sys.exit()

		else:
			trouvé = False

			for racine in range(1,number//2):
				if number/racine == racine :
					print(racine)
					trouvé = True

			if trouvé == False:
				print("N'a pas de racine..")