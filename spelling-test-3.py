"""Module defining the randint"""
from random import randint

spellings = {
    "Cardiogram": "The tracing (writing) made by a heart monitor",
    "Grammar": "The study of the way words are used in a language",
    "Autograph": "A person’s own signature",
    "Graphite": "A type of carbon used in pencils",
    "Epigraph": "An inscription on a monument or at the end of a book",
    "Graphic": "Providing a clear picture; vivid and realistic",
    "Graph": "A diagram showing the relation between two variable quantities",
    "Hydrate": "To add water to",
    "Hydraulics": "Operated by or using a liquid",
    "Hydrosphere": "The watery areas of the earth including oceans, lakes etc.",
    "Repeatable": "A measurement is this if the original experimenter uses the same method and equipment and obtains the same results",
    "Reproducible": "A measurement is this if the investigation is repeated by another person, or by using different equipment or techniques, the same results are obtained",
    "Resolution": "This is the smallest change in the quantity being measured of a measuring instrument that gives a perceptible change in the reading",
    "Sketch graph": "A line graph, not necessarily on a grid, that shows the general shape of the relationship between two variables. It will not have any points plotted and although the axes are labelled they may not be scaled",
    "True value": "This is the value that would be obtained in an ideal measurement",
    "Uncertainty": "The interval within which the true value can be expected to lie, with a given level of confidence or probability",
    "Validity": "Suitability of the investigative procedure to answer the question being asked",
    "Valid conclusion": "Supported by valid data, obtained from an appropriate experimental design and based on sound reasoning",
    "Variable": "These are physical, chemical or biological quantities or characteristics",
    "Anomalies": "These are values in a set of results which are judged not to be part of the variation caused by random uncertainty"
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
