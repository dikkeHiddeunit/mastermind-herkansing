"""
Final assignment 1: mastermind game
Hidde Klinkhamer - 1838178

Opdracht: implementeer het spel Mastermind. Je moet als mens tegen de computer kunnen spelen en andersom.
Jij moet dus een code kunnen raden terwijl de computer feedback geeft,
maar de computer moet ook een code kunnen raden terwijl feedback automatisch gegenereerd wordt.

"""

#Importeer de nodige functies uit het mastermind_functies module
from mastermind_functies import *

#Stel het maximum aantal pogingen en de lengte van de code in
max_pogingen = 10
max_lengte = 4

#Definieer de mogelijke kleuren
kleuren_letters = ["r", "g", "b", "y", "o", "p", "w", "k", "l"]

#Vraag aan de gebruiker of ze een code willen raden of een code willen maken voor de computer
maak_radend = int(input("Typ '1' als je een code wilt raden. Typ '2' als je een code wilt maken voor de computer: "))

if maak_radend == 1:
    #Roep de self_play_mastermind functie aan om het spel te starten
    self_play_mastermind()

if maak_radend == 2:
    #Vraag aan de gebruiker om een code te maken
    code = list(input(f"Maak een code van {max_lengte} letters met behulp van de volgende kleuren: r, g, b, y, o, p, w, k en l: "))
    #Roep de run_mastermind_functies functie aan om de computer de code te laten raden
    code_computer_geraden = run_mastermind_functies(code)
    #print de gok van de computer
    print(f"De computer denkt dat de code {code_computer_geraden[0]} is. Is dit correct?")

if maak_radend != 1 and maak_radend != 2:
    #Print een foutmelding als er een ongeldig nummer wordt ingevoerd
    print(f"{LetterKleuren.FAIL}Dit nummer is niet verbonden aan een actie.{LetterKleuren.ENDC}")
