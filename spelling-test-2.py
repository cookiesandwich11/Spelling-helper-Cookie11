"""Module defining the randint"""
from random import randint

spellings = {
    "Chronicle": "Events in time",
    "Chronic": "Something persisting for a long time or constantly reoccurring",
    "Chronological": "In time order sequence",
    "Synchronised": "Happens at the same time",
    "Dynasty": "A series of leaders or rulers who are all from the same family",
    "Dynamite": "A powerful explosive",
    "Dynamic": "Full of energy and power",
    "Dystopia": "An imaginary place where living conditions are dreadful",
    "Dysphoria": "A sense of great unhappiness or dissatisfaction",
    "Dysfunction": "Abnormal functioning, as of an organ of the body",
    "Accuracy": "A measurement which is judged to be close to the true value",
    "Calibration": "A scale on a measuring instrument",
    "Data": "Information, either qualitative or quantitative, that has been collected",
    "Evidence": "Data which has been shown to be valid",
    "Fair test": "One in which only the independent variable has been allowed to affect the dependent variable",
    "Hypothesis": "A proposal intended to explain certain facts or observations",
    "Interval": "The quantity between readings",
    "Precision": "Precise measurements are ones in which there is very little spread about the mean value",
    "Prediction": "A statement suggesting what will happen in the future, based on observation, experience, or a hypothesis",
    "Range": "The maximum and minimum values of the independent or dependent variables"
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
