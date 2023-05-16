# George Couch
# 5/13/2023
# This program uses various functions from within the Textblob api to perform actions on user entered text.
# Time spent: 5 hours
# Time description: I originally wanted to make this a gui program by using TKinter,
# however, it didn't quite meet the assignment requirements due to the menu needing to be a loop along with functions
# needing parameters. I ended up rewriting the menu system which added on some time.

# imports
from textblob import TextBlob
from textblob import Word

# vars for looping
continueLoop = True
invalidChoice = True
usrChoice = 0
usrNum = 0


# Returns the definition of a word
def define_word(text: str) -> str:
    return Word(text).define()[0]


# Returns a list of all words passed through text parameter
def get_all_words_as_list(text: str) -> str:
    text = TextBlob(text)
    return text.words


# Returns a list of synonyms of a word
def get_synsets_for_word(text: str) -> str:
    return str(Word(text).synsets)


# Returns ngrams for the given text. The number of ngrams is also given by the user
def get_ngrams_for_text(text: str, ngrams: int) -> str:
    txt = TextBlob(text)
    return txt.ngrams(ngrams)


# Menu function
def menu_display():
    global invalidChoice
    invalidChoice = True
    while invalidChoice:
        try:
            print("1: Define a word.")
            print("2: Get all words entered as a list.")
            print("3: Get synsets for a word")
            print("4: Get ngrams for a word")
            print("5: Exit")
            global usrChoice
            usrChoice = int(input("Please choose an option (1/2/3/4/5): "))
            if usrChoice > 5 or usrChoice < 1:
                print("Please enter a number between 1 and 5")
            else:
                invalidChoice = False
        except ValueError:
            print("Please enter an integer")


# Loop for bringing user back to the menu
while continueLoop:

    menu_display()

    # if else for prompting user and selecting correct function
    invalidChoice = True
    if usrChoice == 1:
        usrText = input("Enter a word that you would like defined: ")
        usrText = usrText.strip()
        while invalidChoice:
            if " " in usrText:
                usrText = input("Please only enter a single word: ")
            else:
                definedWord = define_word(usrText)
                print(definedWord)
                invalidChoice = False
    elif usrChoice == 2:
        usrText = input("Please enter some words: ")
        while invalidChoice:
            if len(usrText) == 0:
                usrText = input("No words were entered, please enter some words: ")
            else:
                wordsEntered = get_all_words_as_list(usrText)
                print(wordsEntered)
                invalidChoice = False
    elif usrChoice == 3:
        usrText = input("Enter a word that you would like the synsets for: ")
        usrText = usrText.strip()
        while invalidChoice:
            if " " in usrText:
                usrText = input("Please only enter a single word: ")
            else:
                synsets = get_synsets_for_word(usrText)
                print(synsets)
                invalidChoice = False
    elif usrChoice == 4:
        usrText = input("Enter some text that you'd like the ngrams for: ")
        while invalidChoice:
            try:
                usrNum = int(input("Enter the number of ngrams you'd like: "))
                invalidChoice = False
            except ValueError:
                print("Invalid type entered")
        ngramsTxt = get_ngrams_for_text(usrText, usrNum)
        print(ngramsTxt)
    else:
        quit()
    print()
