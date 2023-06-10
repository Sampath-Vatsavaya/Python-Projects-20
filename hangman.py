from random import choice

def run_game():
    word : str = choice(['cat','dog','sun','happy','tree','book','run','blue','smile','bird','flower','friend','jump','sweet','water','green','moon','song','sleep','star'])
    username : str = input("What is your name? >>")
    print(f"Welcome to hangman,{username}!")

    guessed: str=''
    tries: int = 5
    while tries>0:
        blanks:int =0

        print('Word:',end='')
        for char in word:
            if char in guessed:
                print(char,end='')
            else:
                print('_',end='')
                blanks+=1
        print()
        if blanks==0:
            print("You got it")
            break
        guess: char = input("Enter a letter(If you want to enter the word directly then enter '0' to go to word mode where you will have only 3 chances to attempt the game):")[0]
        #Entering into word mode
        if guess=='0':
            if word_mode(word):
                print("Congrats, You got it")
            else:
                print("No more attempts left, YOU LOST!!!!!")
            break

        if guess in guessed:
            print(f"You already used {guess},Please try with another letter!")
            continue
        guessed+=guess
        if guess not in word:
            tries-=1
            print(f"Sorry, that was wrong ,'{guess}' was not in the word...{tries} tries left.")
            if tries==0:
                print("No more tries left, GAME OVER")
                break
def word_mode(word:str)->int:
    word_guess_chance: int =3
    result : int =0
    while word_guess_chance>0:
        word_guess: str = input("Enter a word:")
        if word_guess==word:
            result=1
            break
        else:
            word_guess_chance -= 1
            print(f"Sorry that was wrong, you have only {word_guess_chance} attempts left.")

    return result


if __name__ == '__main__':
    run_game()