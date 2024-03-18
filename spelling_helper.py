"""Module defining the randint"""
from random import randint

spellings = {
    "Corrupt": "Crooked; immoral",
    "Erupt": "To burst forth",
    "Rupture": "To break or burst",
    "Disrupt": "To cause disorder",
    "Abrupt": "Sudden",
    "Bankrupt": "Having no money; 'broke'",
    "Interrupt": "To cause a break in the flow",
    "Condolence": "Sympathy",
    "Doleful": "Full of sadness or sorrow",
    "Dolorous": "Feeling, showing or causing grief",
    "Buddhist": "A person who follows the path of Siddhartha Gautama.",
    "Buddhism": "A religious philosophy founded by Siddhartha Gautama.",
    "Meditate": "A form of Buddhist worship that focuses the mind.",
    "Precepts": "Five moral rules to help a Buddhist live a better life.",
    "Siddhartha Gautama": "The founder of Buddhism.",
    "Buddha": "The title given to Siddhartha Gautama when he reached enlightenment.",
    "Morality": "A system of values concerning right and wrong.",
    "Morals": "Standards of behaviour e.g. right or wrong.",
    "Absolute": "An action that is right or wrong all of the time.",
    "Relative": "An action that is right or wrong depending on the situation."
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
        print("Wrong :( \n The word was: " + word.lower() + "\n Your word was: " + ANSWER)
        wrongs += 1

print("You have finished the practice! Your score: " + str(20-wrongs) + "/20")
