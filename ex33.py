i = 0
numbers = []

def make_list(number, step):
	while i < number:
		print(f"At the top i is {i}")
		numbers.append(i)
		i = i + step
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
		print("The numbers: ")

	for num in numbers:
		print(num)

numbers_1 = []

def make_list_1(number, step):
	for j in range(0, number, step):
		print(f"At the top j is {j}")
		numbers_1.append(j)
		print("Numbers now: ", number)
		print(f"At the bottom j is {j}")
		print("The numbers: ")
	for num in numbers_1:
16 		print(num)
