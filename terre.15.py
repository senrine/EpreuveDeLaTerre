import sys

if __name__ == '__main__':

	try:
		for index in range(1,len(sys.argv)):
			int(sys.argv[index])
	except:
		print("erreur")
	else:
		index = 1
		trié = True
	
		while index < (len(sys.argv)-1):
			if int(sys.argv[index]) > int(sys.argv[index + 1]):
				trié = False
			index +=1

		if trié:
			print("Triée")
		else:
			print("Non triée")


