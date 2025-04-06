"""Module defining the randint"""
from random import randint

spellings = {
    "Incisive": "Penetrating, cutting, biting",
    "Incision": "A cut or gash",
    "Scissors": "Tools used for cutting",
    "Precise": "Clearly stated; accurate",
    "Decisive": "Definite; clear-cut",
    "Concise": "Brief and direct",
    "Infidel": "An unbeliever",
    "Confide": "To trust",
    "confidant": "One you trust with secrets",
    "Bona fide": "Genuine or real",
    "Connotation": "A related idea or feeling which a word invokes",
    "Prejudice": "a preconceived opinion that is not based on reason or actual experience",
    "Lexical set": "A group of words with the same topic, function or form.",
    "Allusion": "An expression designed to call something to mind without mentioning it explicitly",
    "Hamartia": "A fatal flaw in a tragic hero/heroine",
    "Denouement": "the final part of a narrative in which the strands of the plot are tied together",
    "Summary": "a brief statement or account of the main points of something",
    "Foreshadowing": "A literary device in which a writer provides certain hints for later events in the story.",
    "Rhetoric": "the art of effective or persuasive speaking or writing",
    "Anaphora": "repetition of a word or phrase at the beginning of successive lines"
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
