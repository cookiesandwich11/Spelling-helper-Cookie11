"""Module defining the randint"""
from random import randint
rights = []
spellings = {
    "Autocracy": "A government where one person has power over others",
    "Automatic": "Working by itself",
    "Autotroph": "Makes its own food, e.g., a plant",
    "Autobiography": "A story of someone’s life written by that person",
    "Anthropology": "The study of humans",
    "Anthropoid": "Human-like in shape",
    "Philanthropist": "Someone who loves humans",
    "Biology": "Study of life",
    "Biography": "A story of someone’s life",
    "Biosphere": "Part of the earth where organisms live",
    "Integer": "A whole positive or negative number",
    "Parallel": "When it is the same distance apart, never touching",
    "Perpendicular": "At right angles to another object or line",
    "Vertices": "When two arms of an angle meet or the adjacent sides of a polygon or solid meet",
    "Symmetrical": "When an object can be divided by one or more lines of symmetry",
    "Polygon": "A 2D shape with three or more straight sides",
    "Quadrilateral": "A polygon with four angles and four sides",
    "Circumference": "The distance around a circle",
    "Substitute": "To replace letters in algebra with numbers",
    "Multiplier": "A number used to facilitate a percentage increase or decrease",
    "Significant": "In maths, the digits that give the most meaning to a number"
}

while True:
    if len(spellings) == len(rights):
        break
    word = list(spellings.keys())[randint(0, len(spellings)-1)]
    while word in rights:
        word = list(spellings.keys())[randint(0, len(spellings)-1)]
    print(spellings[word])
    ANSWER = str(input().strip())
    if ANSWER.lower() == word.lower():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCorrect!")
        rights.append(word)
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWrong :( \n The word was: " +
              word.lower() + "\n Your word was: " + ANSWER)
print("You have finished the practice!")
