"""Module defining the randint"""
from random import randint

spellings = {
    "Foliage": "Leaves of a plant",
    "Folio": "A large sheet of paper",
    "Portfolio": "A collection of one’s work",
    "Exfoliate": "To cast off in layers as skin, bark, or rock",
    "Gregarious": "Outgoing; sociable",
    "Segregate": "To separate from the group",
    "Congregate": "To gather together",
    "Aggregate": "Collection from separate parts",
    "Congregation": "Gathering of people",
    "Egregious": "Standing out of the group for being bad or evil",
    "Dehydration": "Excessive loss of body water interrupting the function of the body",
    "Hydration": "Having enough water to enable normal functioning of the body",
    "Rehydration": "Consuming water to restore hydration",
    "Fitness": "The ability to meet/cope with the demands of the environment",
    "Gamesmanship": "Attempting to gain an advantage by stretching the rules to their limit, e.g., time wasting",
    "Intrinsic Motivation": "The drive that comes from within",
    "Extrinsic Motivation": "The drive to perform well or to win in order to gain external rewards",
    "Recovery": "Time required to repair the damage to the body caused by training or competition",
    "Sedentary lifestyle": "A lifestyle with irregular or no physical activity",
    "Well-being": "Involves physical, mental, and social well-being",
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
