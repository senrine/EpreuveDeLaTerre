import sys

if __name__ == '__main__':
	
	try:
		number = int(sys.argv[1])
	except:
		print("erreur")
	else:
		if len(sys.argv) > 2 or len(sys.argv) == 1:
			print("erreur")
			sys.exit()

		if number > 1:
			div = 2
			while div <= number//2:
				if number % div == 0 :
					print("Non,",number,"n'est pas premier")
					sys.exit()
				div +=1

			print("Oui,",number,"est premier")

		elif number >=0:
			print("Non,",number,"n'est pas premier")

		elif number<0:
			print("Ce nombre est négatif")
