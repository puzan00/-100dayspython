import random

def play():
    user=input("Enter Your choice 'r' from rock ,'s' for choice, 'p' for paper\n")
    computer=random.choice(['r', 's', 'p'])

    if user==computer:
        return 'It\'s a tie'
    
    if user_win(user,computer):
        return 'You win'
    return 'You lost!'
def user_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True
print(play())
