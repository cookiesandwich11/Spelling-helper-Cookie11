"""Module defining the randint"""
from random import randint
rights = []
spellings = {
    "Chronicle": "Events in time",
    "Chronic": "Something persisting for a long time or constantly reoccurring",
    "Chronological": "In 'time' order sequence",
    "Synchronised": "Happens at the same time",
    "Dynasty": "A series of leaders or rulers who are all from the same family",
    "Dynamite": "A powerful explosive",
    "Dynamic": "Full of energy and power",
    "Dystopia": "An imaginary place where living conditions are dreadful",
    "Dysphoria": "A sense of great unhappiness or dissatisfaction",
    "Dysfunction": "Abnormal functioning as of an organ of the body",
    "Reversible": "A reaction where the products can change back into the reactants",
    "Chromatography": "A way of separating out the pigments in a dye",
    "Distillation": "Used to extract a pure liquid from a solution",
    "Evaporation": "When liquid particles gain enough energy to break free from the liquid as a gas",
    "Reactants": "The substances that you start with in a chemical reaction",
    "Combustion": "The proper chemistry name for burning",
    "Effervescence": "The proper chemistry name for fizzing",
    "Oxidation": "A chemical reaction with oxygen",
    "Exothermic": "A reaction where heat energy is given out",
    "Neutralisation": "When an acid and alkali are reacted together"
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
