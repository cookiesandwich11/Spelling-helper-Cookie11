"""Module defining the randint"""
from random import randint

spellings = {
    "Corrupt": "Crooked; immoral",
    "Erupt": "To burst forth",
    "Rupture": "To break or burst",
    "Disrupt": "To cause disorder",
    "Abrupt": "Sudden",
    "Bankrupt": "Having no money; ‘broke’",
    "Interrupt": "To cause a break in the flow",
    "Condolence": "Sympathy",
    "Doleful": "Full of sadness or sorrow",
    "Dolorous": "Feeling, showing or causing grief",
    "Muhammad": "the seal of the prophets in Islam",
    "Qur’an": "the Muslim holy book",
    "Sunni": "a denomination of Islam that believes that Abu Bakr should have been Muhammad’s successor",
    "Shi’a": "a denomination of Islam that believes that Ali should have been Muhammad’s successor",
    "Omnipotent": "the quality of being all powerful",
    "Omnibenevolent": "the quality of being all loving",
    "Omniscient": "the quality of being all knowing",
    "Transcendent": "the quality of being above or beyond the human world",
    "Immanent": "the quality of being present in the human world",
    "Resurrection": "the action of rising from the dead"
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
