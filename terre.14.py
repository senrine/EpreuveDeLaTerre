import sys

if __name__ == '__main__':
		
	try:
		for index in range(1,len(sys.argv)):
			int(sys.argv[index])
	except:
		print('erreur')

	else:
		if len(sys.argv) <= 1 or len(sys.argv)>4:
			print("erreur")
		
		else:
			
			minimum = int(sys.argv[1])
			maximum = minimum

			for index in range(1,len(sys.argv) -1):

				if minimum > int(sys.argv[index + 1]):
					minimum = int(sys.argv[index + 1])

				if maximum < int(sys.argv[index + 1]):
					maximum = int(sys.argv[index + 1])

				if int(sys.argv[index]) == int(sys.argv[index + 1]):
					print("erreur")
					sys.exit()

			trouvé = False
			index =1

			while trouvé == False or index < len(sys.argv):

				if int(sys.argv[index]) != maximum and int(sys.argv[index]) != minimum:
					moy = sys.argv[index]
					trouvé = True
				index +=1


			print(moy)
		