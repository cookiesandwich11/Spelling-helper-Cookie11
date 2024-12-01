"""Module defining the randint"""
from random import randint

spellings = {
    "Thermometer": "A device that measures heat",
    "Symmetry": "The quality of being the same on both sides",
    "Asymmetry": "The quality of not being the same on both sides",
    "Geometry": "Maths dealing with the measurement of angles, area, space and volume",
    "Microscope": "An instrument that makes ‘small’ things perceptible",
    "Microphone": "Makes a small voice loud",
    "Microbe": "Very small life form",
    "Monopoly": "Control by one",
    "Monologue": "Speech given by one person",
    "Monotone": "Using one tone only",
    "Fabricating": "Creating products by assembling parts and components together",
    "Aluminium": "Lightweight silvery-grey metallic element that resists rust or corrosion",
    "Malleable": "Able to be hammered or pressed into shape without breaking",
    "Obsolescence": "Becoming outdated or no longer needed",
    "Gauge": "A tool for measuring or marking out",
    "Orthographic": "Third angle, a type of 2D technical drawing",
    "Micrometre": "A precision measurement tool",
    "Ferrous": "Containing iron",
    "Gelatinisation": "When starch granules swell when cooked with liquid, then burst open and release the starch, causing the liquid to thicken",
    "Cuisine": "A traditional style of cooking and eating that has developed in a country or region of the world"
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
