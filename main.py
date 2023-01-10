import random
from asciiArts import dictionary, logo, stages
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')


def displayfillup(display):
    for i in range(len(display)):
        x = display[i]
        print(x, end=" ")


if __name__ == '__main__':
    chosenWord = random.choice(dictionary).lower()
    end = False
    lives = 6
    blankCount = len(chosenWord)
    display = []

    for i in range(blankCount):
        display.append("_")

    # visual elements
    print(logo)
    #print("answer is : " + chosenWord)
    displayfillup(display)

    # core logic
    while not end:
        guess = input("\nGuess a letter! ").lower()
        clear()
        notExist = True

        # prompts
        if guess in display:
            print(f"You already guessed {guess} ")
        elif guess in chosenWord:
            print(f"You guessed {guess} which is correct")
        else:
            print(f"You guessed {guess} which is wrong.left life : {lives}")

        # checking the guessed letter with correct answer
        for i in range(len(chosenWord)):
            if guess == chosenWord[i]:
                display[i] = guess
                notExist = False

        displayfillup(display)

        # lives reduced if guessed wrong
        if notExist:
            print(stages[lives])
            lives -= 1

        # exit conditions
        if "_" not in display:
            end = True
            print("\nYou win")
        elif lives < 0:
            end = True
            print("\nGame Over")
