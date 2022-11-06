
#assessment 1
import random


first_range = input("Enter the start of the range: ")
while not first_range.isdigit():
    print("Enter a valid number.")
    first_range = input("Enter the start of the range: ")

second_range = input("Enter the end of the range: ")
while not second_range.isdigit() or int(second_range) < int(first_range):
    print("Enter a valid number.")
    second_range = input("Enter the end of the range: ")

random_number = random.randint(int(first_range), int(second_range))
guesser = 0
guess = None

while guess != random_number:
    guessed_number = int(input("Guess number: "))
    guess = guessed_number
    guesser += 1
    print(random_number)


print(f"You guessed {guesser} time(s)")