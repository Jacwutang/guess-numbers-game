import random, argparse


def create_game(min_range: int, max_range: int) -> int:
    
    winner = random.randrange(min_range, max_range + 1, 1)
    
    guess = None
    while guess != winner:
        guess = int(input(f'Enter a number between {min_range}-{max_range}: '))

        if guess < winner:
            print("Too low")
        elif guess > winner:
            print("Too high")
        else:
            print("Correct!")
            return guess


if __name__ == "__main__":
    create_game(1,10)

    
    
    



    
