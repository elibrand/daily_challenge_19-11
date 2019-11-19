code = input("Write in the code")

crypt = input("Are you trying to encrypt or decrypt?")

ordList = []
doneDeal = []

if crypt == "encrypt":

	for letter in code:
		letter = ord(letter) + 5
		ordList.append(letter)

	for number in ordList:
		number = chr(number)
		doneDeal.append(number)

	doneDeal = "".join(doneDeal)

	print(doneDeal)


elif crypt == "decrypt":

	for letter in code:
		letter = ord(letter) - 5
		ordList.append(letter)

	for number in ordList:
		number = chr(number)
		doneDeal.append(number)

	doneDeal = "".join(doneDeal)

	print(doneDeal)


	


