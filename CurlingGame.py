import random

class CurlingSheet:
    def __init__(self):
        self.target = random.randint(1, 10)
        self.player_scores = 0
        self.computer_scores = 0
    
    def throw_stone(self, stone):
        stone_difference = abs(self.target - stone)
        
        if stone_difference == 0:
            print("Perfect throw! The stone lands exactly on the target.")
        elif stone_difference <= 2:
            print("Great throw! The stone is close to the target.")
        elif stone_difference <= 5:
            print("Good throw! The stone is near the target.")
        else:
            print("The stone missed the target.")
        
        if stone_difference < 3:
            self.player_scores += 1
            print("Player scores a point!")
        elif stone_difference > 5:
            self.computer_scores += 1
            print("Computer scores a point!")
    
    def print_scores(self):
        print("Player scores:", self.player_scores)
        print("Computer scores:", self.computer_scores)

class Player:
    def __init__(self, name):
        self.name = name
    
    def throw_stone(self):
        return int(input("Enter your throw (1-10): "))

class ComputerPlayer:
    def throw_stone(self):
        return random.randint(1, 10)

def play_curling_game():
    sheet = CurlingSheet()
    player = Player("Player")
    computer = ComputerPlayer()

    print("Welcome to the Curling Game!")
    print("The target is:", sheet.target)

    while True:
        player_throw = player.throw_stone()
        computer_throw = computer.throw_stone()

        print("Player's throw:", player_throw)
        print("Computer's throw:", computer_throw)

        sheet.throw_stone(player_throw)
        sheet.throw_stone(computer_throw)

        sheet.print_scores()

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

    print("Thanks for playing!")

play_curling_game()
