"""Module defining the randint"""
from random import randint

spellings = {
    "Thermal": "Relating to or caused by heat",
    "Hypothermia": "Subnormal body temperature",
    "Thermometer": "An instrument for measuring temperature",
    "Hyperthermia": "Abnormally high body temperature",
    "Thermodynamics": "The branch of physics concerned with the conversion of different forms of energy",
    "Technique": "A special way of or skill of doing something",
    "Technology": "Advanced or modern scientific knowledge of new machines",
    "Pyrotechnics": "The art of manufacturing or setting off fireworks",
    "Technicality": "A small detail of a set of rules",
    "Technician": "One who is known for a skill in an intellectual or artistic technique",
    "Parameter": "Data that is to be passed into another bit of code",
    "Function": "A small piece of reusable code into which data can be passed and which returns a value",
    "Procedure": "A small piece of reusable code into which data can be passed and which does not return a value",
    "Casting": "Converting a variable from one data type to another",
    "Modulus": "Returns the remainder from a division",
    "Volatile": "Data is lost when the power is removed. This happens in RAM",
    "Internet": "A global computer network of cables used for data sharing",
    "Cache": "Memory in the processor which provides fast access to frequently used instructions and data",
    "Accumulator": "A part of the CPU that holds the results of calculations",
    "Boolean": "AND, OR, NOT, Used in conditions"
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
