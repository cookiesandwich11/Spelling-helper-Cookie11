"""Module defining the randint"""
from random import randint

spellings = {
    "Levity": "Lack of seriousness",
    "Elevate": "To raise; to lift up",
    "Alleviate": "To lessen in intensity",
    "Levitate": "To float in the air",
    "Lever": "A tool which makes something light enough to be lifted.",
    "Eloquent": "Skilful with words",
    "Colloquial": "Informal, common language",
    "Loquacious": "Very talkative",
    "Soliloquy": "Speaking of one’s thoughts",
    "Elocution": "Effective public speaking",
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

print("You have finished the practice! Your score: " + str(10-wrongs) + "/10")
