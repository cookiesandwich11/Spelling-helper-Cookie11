"""Module defining the randint"""
from random import randint

spellings = {
    "Kaleidoscope": "A complex pattern of constantly changing colours and shapes",
    "Microscope": "Magnifier of the image of small objects",
    "Horoscope": "A prediction of someone’s future based on the position of the planets",
    "Periscope": "An optical instrument that provides a view of an otherwise obstructed field",
    "Scope": "An area in which something acts or operates or has power or control",
    "Incontinent": "Having no control over urination or defecation",
    "Discontinue": "Put an end to a state or activity",
    "Continual": "Occurring without interruption",
    "Pertinent": "Directly related or relevant to the subject under consideration",
    "Abstinence": "The practice of keeping away from or avoiding something you enjoy",
    "Acknowledge": "Accept or admit existence or truth",
    "Acquaintance": "A person one knows slightly, but is not a close friend",
    "Exhilarate": "Make someone feel very happy, animated or elated",
    "Hierarchy": "A system in which members are ranked according to relative status",
    "Imitate": "To copy or follow as a model",
    "Maintenance": "The process of preserving a condition or situation",
    "Extraordinary": "Very unusual or remarkable",
    "Feminine": "Having qualities or an appearance traditionally associated with women, especially delicacy and prettiness",
    "Vicious": "Deliberately cruel or violent",
    "Rhythm": "A strong, regular repeated pattern of movement or sound"
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
