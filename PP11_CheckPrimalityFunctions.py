from math import sqrt


def check_prime():
	number = int(input("Please provide a number: "))
	is_prime = [num for num in range(2, int(sqrt(number))) if number % num == 0]
	if is_prime == []:
		print ("This number is a prime number")
	else:
		print ("This is not a prime number as it is divisible by " + ", ".join(str(i) for i in is_prime))
	
	while True:
		all_divisors = str(input("Would you like to know all the divisors of your number?  Y or N: "))
		if all_divisors.lower() == "y":
			is_prime_all = [num for num in range(2, (number)) if number % num == 0]
			print ("This number is divisible by " + ", ".join(str(i) for i in is_prime_all))
			break
		elif all_divisors.lower() == "n":
			print ("Good bye")
			break
		else:
			print ("You need to enter Y for yes or N for no")


if __name__ == "__main__":
	check_prime()
