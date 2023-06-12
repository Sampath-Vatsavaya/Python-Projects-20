from random import randint

def roll_dice(amount: int = 2) -> list[int]:
    if amount <=0:
        raise ValueError
    rolls : list[int] =[]
    for i in range(amount):
        random_roll =randint(1,6)
        rolls.append(random_roll)

    return rolls

def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll(Enter 'exit' if you want to quit):")
            if user_input.lower()== "exit":
                print("Thanks for playing")
                break
            rolled_values=roll_dice(int(user_input))
            print(*rolled_values,sep=', ')
            print("Sum of the roll values=",sum(rolled_values))
        except ValueError as e:
            print("(Please Enter a Valid Number)")

if __name__== '__main__':
    main()
