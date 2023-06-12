from random import choice
import sys

class RPS:
    def __init__(self):
        print("Welcome to Rock Paper Scissor Game:\n(Enter exit when you want to quit)")

        self.moves:dict ={'rock' : '🪨' , 'paper' : '📄' , 'scissor' : '✂' }
        self.valid_moves: list[str] = list(self.moves.keys())
        self.user_score=0
        self.ai_score=0
    def play_game(self):
        user_move:str = input("Rock,Paper or Scissor:").lower()
        if user_move=="exit":
            if self.user_score== self.ai_score:
                print("It's a Tie")
            elif self.user_score>self.ai_score:
                print("You won the game")
            else:
                print("AI won the game")
            print("Thanks for Playing")
            sys.exit()
        if user_move not in self.valid_moves:
            print("Invalid move")
            return self.play_game()
        ai_move= choice(self.valid_moves)

        self.display_moves(user_move,ai_move)
        self.check_move(user_move,ai_move)

    def display_moves(self,user_move,ai_move):
        print('--------------')
        print(f"Your Move:{self.moves[user_move]}")
        print(f"AI Move:{self.moves[ai_move]}")
        print('--------------')

    def check_move(self,user_move,ai_move):
        if user_move==ai_move:
            print("It's a Tie")
            self.user_score+=1
            self.ai_score+=1
            print(f"Your Score :{self.user_score} ----- AI Score:{self.ai_score}")
        elif user_move=="rock" and ai_move=="scissor":
            print("You won the round")
            self.user_score += 1
            print(f"Your Score :{self.user_score} ----- AI Score:{self.ai_score}")
        elif user_move=="paper" and ai_move=="rock":
            print("You won the round")
            self.user_score += 1
            print(f"Your Score :{self.user_score} ----- AI Score:{self.ai_score}")
        elif user_move=="scissor" and ai_move=="paper":
            print("You won the round")
            self.user_score += 1
            print(f"Your Score :{self.user_score} ----- AI Score:{self.ai_score}")
        else:
            print("AI won the round")
            self.ai_score += 1
            print(f"Your Score :{self.user_score} ----- AI Score:{self.ai_score}")

if __name__ == '__main__':
    rps=RPS()
    while True:
        rps.play_game()


