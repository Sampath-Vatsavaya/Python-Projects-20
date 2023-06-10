from random import randint
lower_num,higher_num=1,10

random_number: int = randint(lower_num,higher_num)

print(f"Guess the Number(In the range from {lower_num} to {higher_num}).")
chances=3
while True:
    try:
        user_guess : int = int(input("Enter your guess:"))
    except ValueError as e:
        print("Please enter a valid number.")
        continue
    if chances==0:
        print("You are out of chances.GAME OVER")
        break
    if user_guess>random_number:
        print(f"Your guess is larger than the number.You have {chances} chances left")
        chances-=1

    elif user_guess==random_number:
        print(f"Your guess is smaller than the number.You have {chances} chances left")
        chances-=1
    else:
        print("Correct Guess")
        break




