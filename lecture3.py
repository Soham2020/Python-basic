#guess the number game
import random

r = random.randint(1,20)

while(True):
	a = int(input())
	if(a>r):
		print("Try a smaller number")
	elif(a<r):
		print("Try a greater number")
	else:
		print("Congrats you guessed the correct number")
		break