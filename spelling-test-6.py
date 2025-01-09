"""Module defining the randint"""
from random import randint

spellings = {
    "Foliage": "Leaves of a plant",
    "Folio": "A large sheet of paper",
    "Portfolio": "A collection of one’s work",
    "Exfoliate": "To cast off in layers as skin, bark or rock",
    "Gregarious": "Outgoing; sociable",
    "Segregate": "To separate from the group",
    "Congregate": "To gather together",
    "Aggregate": "Collection from separate parts",
    "Congregation": "Gathering of people",
    "Egregious": "Standing out of the group for being bad or evil",
    "Aerobic": "With oxygen. When exercise is not too fast and is steady, the heart can supply all the oxygen that the working muscles need. Summarised as: glucose + oxygen → energy + carbon dioxide + water",
    "Anaerobic": "Without oxygen. When exercise duration is short and at high intensity, the heart and lungs cannot supply blood and oxygen to muscles as fast as the respiring cells need them. Summarised as: glucose → energy + lactic acid",
    "Body composition": "The percentage of body weight which is fat and non-fat (muscle and bone)",
    "Carbohydrate": "The body's preferred energy source",
    "Cardio-vascular endurance (aerobic power)": "The ability of the heart and lungs to supply oxygen to the working muscles",
    "Power/explosive strength (anaerobic power)": "The product of strength and speed, i.e. strength x speed",
    "Circuit training": "A series of exercise stations whereby periods of work are interspersed with periods of rest",
    "Continuous training": "Involves working for a sustained period of time without rest. It improves cardio-vascular fitness. Sometimes referred to as a steady state training",
    "Fartlek training": "Swedish for ‘speed play’. Periods of fast work with intermittent periods of slower work. Often used in running, i.e. sprint, jog, walk, jog, sprint, etc.",
    "Reliability": "Relating to the consistency and repeatability of a test"
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
