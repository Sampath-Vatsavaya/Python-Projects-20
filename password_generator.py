import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

def generate_password(length:int,uppercase:bool,symbol:bool):
    combination : str = string.ascii_lowercase+string.digits
    if uppercase:
        combination+= string.ascii_uppercase
    if symbol:
        combination+=string.punctuation
    combination_length=len(combination)
    new_password:str=''
    for _ in range(length):
        new_password+= combination[secrets.randbelow(combination_length)]

    return new_password


if __name__ == '__main__':
    for i in range(1,100):
        new_pass:str= generate_password(length=15,uppercase=True,symbol=True)
        spec=f" Upper:{contains_upper(new_pass)} , Symbol:{contains_symbols(new_pass)}"
        print(f"{i} -> {new_pass}   {spec} ")