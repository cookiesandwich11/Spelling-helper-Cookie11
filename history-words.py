"""Module defining the randint"""
from random import randint

spellings = {
    "Armistice": "A truce, when both sides agree to stop fighting.",
    "Capitalism": "An economic and political system in which a country's trade and industry are controlled by private owners for profit, rather than by the state.",
    "Ghetto": "A part of a city, especially a slum area, occupied by a minority group or groups.",
    "Conscription": "A law that forces all men to join the armed forces.",
    "Great Depression": "A long period of financial and industrial decline.",
    "Fascism": "A political belief or party with extreme right-wing views.",
    "Communism": "A political belief or party who believes all private property should be state-owned and people paid equally.",
    "Stock Market": "Where companies buy and sell stocks and shares.",
    "Reparations": "Compensation for war damage paid by the losing country.",
    "Alliance": "An agreement between two or more countries to support each other.",
    "Blitzkrieg": "A sudden, or 'lightning' military strike to gain a quick military victory.",
    "Propaganda": "Publicity specially selected to put forward one point of view, usually political.",
    "Abdicate": "Stand down from power.",
    "Nationalism": "Identification with one's own nation and support for its interests, especially to the exclusion or detriment of the interests of other nations.",
    "Genocide": "The deliberate killing of a large number of people from a particular nation or ethnic group with the aim of destroying that nation or group.",
    "Persecution": "Persecution is the systematic mistreatment of an individual or group by another individual or group.",
    "Anti-semitism": "Hostility to or prejudice against Jewish people.",
    "Diaspora": "The dispersion or spread of any people from their original homeland.",
    "Memorial": "A statue or structure established to remind people of a person or event.",
    "Assassinate": "Murder (an important person) for political or religious reasons."
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
