import sys

if __name__ == '__main__':

	alphabet = 'abcdefghijklmnopqrstuvwxyz'

	for index in range(len(alphabet)):
		if alphabet[index] >= sys.argv[1]:
			print(alphabet[index],end='')

	print(f'\t')