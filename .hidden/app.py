import string
import random
import time
def password():
	digits = 2
	password = '';
	for digit in range(0, digits):
		letter = string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase))]
		password += letter
	password = "ze"
#print(password); 
	while(True):
		guess= input("What is the password(2 char): ");
		if(guess == password):
			print("Login Correct");
			break;
		else:
			time.sleep(.5)
			print("Login Incorrect");


if __name__ == "__main__":
	password();
