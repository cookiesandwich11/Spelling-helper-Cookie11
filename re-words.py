"""Module defining the randint"""
from random import randint

spellings = {
    "Omniscient": "All knowing",
    "Omnipotent": "All powerful",
    "Omnibenevolent": "All loving",
    "Omnipresent": "Being present all of the time",
    "Eternal": "Timeless, having no beginning or end",
    "Father": "One part of the trinity, showing the loving caring character of God.",
    "Creator": "Name given to god to describe that he made the universe",
    "Holy": "God is different from humans",
    "Judge": "The name given to god to show that he will judge whether people will go to heaven or hell",
    "Immanent": "The word used to describe that God is present on the earth",
    "Transcendent": "God is beyond tge natural limits of the earth",
    "trinity": "God is one but also 3",
    "Saviour": "Word used to describe Jesus because humans recieved salvation through him.",
    "Design": "SOme humans believe this is present in the world because it cannot have happened by chance",
    "Bible": "The book which Christians belive is the word of God.",
    "Miracle": "A supernatural event that seems to break the law of science and could be caused by God.",
    "Cosmological": "God exists because he was the cause of the universe",
    "Conservative christian": "A christian who believes the bible is litterally true",
    "Liberal Christian": "A christian who uses the bible as symbolism",
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

print("You have finished the practice! Your score: " + str(19-wrongs) + "/19")
