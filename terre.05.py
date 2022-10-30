import sys

if __name__ == '__main__':

	try:
		argument = int(sys.argv[1])

	except:
		print("Tu me la mettras pas à l'envers...")

	else:
		if argument >= 0:

			if argument % 2 == 0:
				print('pair')

			else:
				print('impair')

		else:
			print('negatif')
