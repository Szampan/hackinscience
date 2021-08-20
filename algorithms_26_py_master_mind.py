from random import choice
from string import ascii_uppercase

def gen_colors(code_size):
    if code_size < len(ascii_uppercase):
        letters = [ascii_uppercase[i] for i in range(code_size)]
    else:
        letters = ascii_uppercase
    return "".join(letters)


def gen_code(code_size, colors):        
    code = [choice(colors) for i in range(code_size)]
    return code

def check_guess(guess, code_size, colors):
    for i in guess:
        if i not in colors:            
            return False
    if len(guess) != code_size:
        return False
    return True
        
def score_guess(code, guess):
    code = list(code)
    guess = list(guess)
    right_pos = 0
    wrong_pos = 0
    missed = []
    for i in range(len(code)):
        if code[i] == guess[i]:            
            right_pos += 1            
        else:
            missed.append(code[i])
    for i in range(len(guess)):
        if guess[i] != code[i] and guess[i] in missed:                        
            wrong_pos += 1
            missed.pop(missed.index(guess[i]))  
    return (right_pos, wrong_pos)  

def play_cli(code_size, nb_colors):    
    code = "".join(gen_code(code_size, nb_colors))    
    attempts = 1                   
    print(f"Possible colors are: {nb_colors} \nCode is size {code_size}")
    # print("pswd: ", code)
    while True:
        x = input()        
        if not check_guess(x, code_size, nb_colors):
            print("Wrong size or color!")
        elif x == code:
            print(f"Congrats, you won after {attempts} attempts")
            return
        else:
            print(score_guess(code, x))
        attempts+=1


    
if __name__ == "__main__":
    play_cli(4, "ABCDEF")
    # print(gen_colors(28))

