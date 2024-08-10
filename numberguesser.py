import random

print('***Welcome To Number Guesser***')
print('Choose which level you want play??')
print('1. Essay guess number between 1 to 100 with 100 tries')
print('2. Mid guess number between 1 to 100 with 10 tries')
print('3. Hard guess number between 1 to 100 with 5 tries')
print('4. Custom level')
print('**************************************************')

choose_level = True
lowest_number = 1
highest_number = 100
guesses = 0
tries = 0
score = 0

while choose_level:

    level = int(input('Enter the level you want to play: '))

    if level == 1:
        tries = 100  # Set tries to infinity for unlimited tries
        choose_level = False
    
    elif level == 2:
        tries = 10
        choose_level = False

    elif level == 3:
        tries = 5
        choose_level = False

    elif level == 4:
        tries = int(input('Enter the number of tries you want: '))
        choose_level = False

    else:
        print('Please enter a valid level number (1, 2, 3 ,4)')

answer = random.randint(lowest_number, highest_number)
is_running = True

while is_running:
    guess = input(f'Enter a number between {lowest_number} and {highest_number}: ')
    if guess.isdigit():
        guess = int(guess)
        tries -= 1
        guesses += 1               
        if guess < 1 or guess > 100:
            print('This number is out of range!')
            print(f'You have {tries} left')
        elif guess < answer:
            print('Too low try again!')
            print(f'You have {tries} left')
        elif guess > answer:
            print('Too high try again!')
            print(f'You have {tries} left')
        else:
            print(f'Correct you guessed the number in {guesses} tries')
            print(f'The number was {answer}')
            

            # Calculate score
            def save_score(score, filename="high_score.txt"):
                with open(filename, 'w') as file:
                    file.write(str(score))

            def get_high_score(filename="high_score.txt"):
                try:
                    with open(filename, 'r') as file:
                        return int(file.read())
                except FileNotFoundError:
                    return 0  # If the file doesn't exist, return 0 as the high score

            def check_and_update_high_score(current_score, filename="high_score.txt"):
                high_score = get_high_score(filename)
                if current_score > high_score:
                    save_score(current_score, filename)
                    print(f"Congratulations! You broke the highest score! your score is {current_score}")
                else:
                    print(f"Your score: {current_score}. High score: {high_score}.")
            
            current_score = 1000 - guesses * 10
            
            # Check and update high score
            check_and_update_high_score(current_score)
            save_score(current_score)  # Save the score to the file

            is_running = False

        if tries == 0:
            print('You have run out of tries')
            is_running = False
        
    else:
        print('Please enter a number not word!')
