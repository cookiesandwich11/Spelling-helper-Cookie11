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
    "Programming": "The creation of software code for microcontrollers and electronics",
    "Environment": "The space or situation that a product will be placed and/or used",
    "Macronutrient": "A type of food (e.g. fat, protein, carbohydrate) required in large amounts in the diet",
    "Prototyping": "A process that involves the production of a test model, on which the final product is based",
    "Soldering": "A way of joining electronic components to a circuit board",
    "Recipe": "A list of ingredients and instructions for cooking",
    "Mechanisms": "For example, gears, pulleys. Used to convey movement",
    "Oscillating": "Pendulum motion",
    "Reciprocating": "Backwards and forwards motion",
    "Nutrition": "The process of providing or obtaining the food necessary for health and growth"
}


rights = []

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
    else:
        print("Wrong :( \n The word was: " + word.lower() + "\n Your word was: " + ANSWER)

print("You have finished the practice!")
