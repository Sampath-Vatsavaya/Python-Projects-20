import itertools
import time
import string

def common_guess(word:str) -> str | None:

    with open('words.txt','r') as words:
        word_list: list[str] = words.read().splitlines()

    for i,match in enumerate(word_list,start=1):
        if match==word:
            return f'Common match: {match} (#{i})'


def brute_force(word:str,length:int,digits:bool=False,symbols:bool = True) -> str|None:
    chars:str= string.ascii_lowercase
    if digits:
        chars+=string.digits
    if symbols:
        chars+=string.punctuation
    attempts:int =0
    for guess in itertools.product(chars,repeat=length):
        attempts+=1
        guess: str = ''.join(guess)
        if guess==word:
            print(f'"{word}" was cracked in {attempts:,} guesses.')
            return f'"{word} was cracked in {attempts:,} guesses.'
        #print(guess,attempts)
def main():
    print("Searching")
    password:str = "tate"
    start_time:float= time.perf_counter()
    if common_match:= common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password,length=4,digits=False,symbols=False):
            print("Cracked")
        else:
            print("No match found")

    end_time:float= time.perf_counter()
    print(round(end_time-start_time,2),'seconds')

if __name__ == '__main__':
    main()

