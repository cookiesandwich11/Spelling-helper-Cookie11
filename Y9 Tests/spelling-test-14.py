"""Module defining the randint"""
from random import randint

"""Module defining the randint"""
from random import randint

spellings = {
    "Manufacture": "To make something",
    "Benefactor": "A person who gives money or help to someone else",
    "Malefactor": "A person who has done something wrong",
    "Artefact": "An object made by a human being",
    "Chromogenic": "Involving the production of colour or pigments",
    "Monochrome": "Varying tones of only one colour, or black and white",
    "Audible": "Able to be heard",
    "Audience": "The assembled listeners at a public event",
    "Aqueous": "Made from water",
    "Aquamarine": "The blue green colour of water",
    
    # Commonly misspelt words
    "Extremely": "To a very great degree.",
    "Immediately": "Without any intervening time or space",
    "Necessary": "Needing to be done or achieved",
    "Neighbour": "To be situated next to or somewhere near",
    "Nervous": "Easily agitated or alarmed",
    "Opportunity": "A time or set of circumstances that make it possible to do something",
    "Persuade": "Cause someone to believe something through reasoning or argument",
    "Separate": "To cause to move or be apart",
    "Receive": "To be given or presented with something",
    "Sincerely": "To act in a sincere or genuine way."
}







rights = []
wrongs = 0
while True:
    if len(spellings) == len(rights):
        break

    word = list(spellings.keys())[randint(0, len(spellings) - 1)]
    while word in rights:
        word = list(spellings.keys())[randint(0, len(spellings) - 1)]

    print(spellings[word])
    ANSWER = str(input().strip())
    if ANSWER.lower() == word.lower():
        print("\nCorrect!")
        rights.append(word)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Wrong :( \n The word was: " + word.lower() + "\n Your word was: " + ANSWER)
        wrongs += 1

print("You have finished the practice! Your score: " + str(20-wrongs) + "/20")







rights = []
wrongs = 0
while True:
    if len(spellings) == len(rights):
        break

    word = list(spellings.keys())[randint(0, len(spellings) - 1)]
    while word in rights:
        word = list(spellings.keys())[randint(0, len(spellings) - 1)]

    print(spellings[word])
    ANSWER = str(input().strip())
    if ANSWER.lower() == word.lower():
        print("\nCorrect!")
        rights.append(word)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("Wrong :( \n The word was: " + word.lower() + "\n Your word was: " + ANSWER)
        wrongs += 1

print("You have finished the practice! Your score: " + str(20-wrongs) + "/20")
