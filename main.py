import random

def display_welcome_message():
    print('*** Welcome To Number Guesser ***')
    print('Choose which level you want to play:')
    print('1. Easy: Guess number between 1 to 100 with unlimited tries')
    print('2. Medium: Guess number between 1 to 100 with 10 tries')
    print('3. Hard: Guess number between 1 to 100 with 5 tries')
    print('4. Custom level')
    print('********************************************')

def get_level():
    while True:
        try:
            level = int(input('Enter the level you want to play: '))
            if level in [1, 2, 3]:
                return level
            elif level == 4:
                tries = int(input('Enter the number of tries you want: '))
                return tries
            else:
                print('Please enter a valid level number (1, 2, 3, 4).')
        except ValueError:
            print('Invalid input. Please enter a number.')

def set_tries(level):
    if level == 1:
        return 99999999  
    elif level == 2:
        return 10
    elif level == 3:
        return 5
    else:
        return level  

def play_game(lowest_number, highest_number, tries):
    answer = random.randint(lowest_number, highest_number)
    guesses = 0
    while tries > 0:
        guess = input(f'Enter a number between {lowest_number} and {highest_number}: ')
        if guess.isdigit():
            guess = int(guess)
            if guess < lowest_number or guess > highest_number:
                print('This number is out of range!')
            else:
                tries -= 1
                guesses += 1
                if guess < answer:
                    print('Too low, try again!')
                elif guess > answer:
                    print('Too high, try again!')
                else:
                    print(f'Correct! You guessed the number in {guesses} tries.')
                    print(f'The number was {answer}.')
                    return  
            print(f'You have {tries} tries left.')
        else:
            print('Please enter a number, not a word!')

    print('You have run out of tries.')

def main():
    display_welcome_message()
    level = get_level()
    tries = set_tries(level)
    play_game(1, 100, tries)

if __name__ == "__main__":
    main()
