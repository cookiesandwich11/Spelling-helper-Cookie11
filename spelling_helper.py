"""Module defining the randint"""
from random import randint

spellings = {
    'hypothermia': 'Condition of having a low body temperature',
    'Hypoglycaemic': 'When blood sugar decreases to below normal levels',
    'Hypotenuse': 'Side of a right triangle that is stretched under the right angle',
    'hypodermic': 'Pertaining to under the skin',
    'Hyperbole': 'Overly praising something',
    'Hyperactive': 'Overly active',
    'Hyperglycaemic': 'When blood sugar increases to above normal levels',
    'Psychology': 'The study of the human mind',
    'Technology': 'The study of scientific knowledge',
    'Terminology': 'A system of terms used in academic study',
    'Aerobic': 'Meaning with oxygen',
    'Bronchioles': 'The small tubes in the lungs that extend from the bronchi',
    'Diaphragm': 'The sheet of muscle at the base of the chest cavity',
    'Ventricles': 'The lower muscular chambers in the heart',
    'Respiration': 'A chemical reaction that reacts glucose with oxygen',
    'Vaccination': 'Trains your immune system on how to respond to a pathogen',
    'Adaptation': 'Evolution produces organisms that are well suited to their environment',
    'Chromosome': 'The structure made of DNA in a cell',
    'Ecosystem': 'A large area on Earth with similar weather, conditions, and living things',
    'Pesticide': 'A chemical sprayed on crops to kill insects or tackle plant diseases',
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
