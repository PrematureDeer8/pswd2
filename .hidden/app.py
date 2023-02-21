import string
import random
def password():
	digits = 2
	password = '';
	for digit in range(0, digits):
		letter = string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase))]
		password += letter
#print(password); 
	while(True):
		guess= input("What is the password(2 char): ");
		if(guess == password):
			print("Correct password");
			break;
		else:
			print("Incorrect password");


if __name__ == "__main__":
	password();
