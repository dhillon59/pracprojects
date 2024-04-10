import random

def computer_choice():
    compic = random.randint(1,3)
    if compic == 1:
        return "r"
    elif compic  == 2:
        return "r"
    else:
        return "s"

def player_choice():
    usin = input('Enter ur choice from Rock(r), Paper(p), or Scissor(s) : ')
    return usin 

def rpk(x, y):
    win = ""
    if x == y:
        win =  "Tie"
    elif x == 'r' and y == 's':
        win = "Rock beats scissor, Computer wins"
    elif x == 'p' and y == 'r':
        win = "Paper beats rock, Computer wins"
    elif x == 's' and y == 'p':
        win = "Scissor beats paper, Computer wins"
    elif y == 'r' and x == 's':
        win = "Rock beats scissor, Player wins"
    elif y == 'p' and x == 'r':
        win = "Paper beats rock, Player wins"
    elif y == 's' and x == 'p':
        win = "Scissor beats paper, Player wins"
    return win 

def play():
    want =  True
    count = 0
    while want:
        x = computer_choice()
        y = player_choice()
        print(rpk(x,y))
        again = input('Would you like to play again (y or n): ')
        if again == 'n':
            want = False 
    print("Thanks for playing!")
    
play()