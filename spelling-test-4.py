"""Module defining the randint"""
from random import randint

spellings = {
    "hypothermia": "Condition of having a 'low' body temperature",
    "Hypoglycaemic": "When blood sugar decreases to below normal levels",
    "Hypotenuse": "Side of a right triangle that is stretched 'under' the right angle",
    "hypodermic": "Pertaining to under the skin",
    "Hyperbole": "Overly praising something",
    "Hyperactive": "Overly active",
    "Hyperglycaemic": "When blood sugar increases to above normal levels",
    "Psychology": "The study of the human mind",
    "Technology": "The study of scientific knowledge",
    "Terminology": "A system of terms used in academic study",
    "Catalyst": "A substance that increases the rate of a chemical reaction without itself undergoing any permanent chemical change",
    "Chromosome": "A threadlike structure of nucleic acids and protein, found in the nucleus of most living cells, carrying genetic information in the form of genes",
    "Efficiency": "The ratio of useful work performed to the total energy expended",
    "Emission": "The production and discharge of something, especially gas or radiation",
    "Enzyme": "A substance produced by a living organism that acts as a catalyst to bring about a specific biochemical reaction",
    "Equilibrium": "A state in which opposing forces or influences are balanced",
    "Homeostasis": "A process by which biological systems tend to maintain stability",
    "Interference": "The combination of two or more waveforms to form a resultant wave in which the displacement is either reinforced or cancelled",
    "Mitochondria": "An organelle found in large numbers in most cells, in which the biochemical processes of respiration and energy production occur",
    "Polymerisation": "A chemical process that combines several monomers"
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
