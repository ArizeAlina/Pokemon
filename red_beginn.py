#!/bin/python3

print("Eich: Willkommen in der wundersamen Welt von Pokemon")
print("Eich: Mein Name ist Eich, ich arbeite hier als Pokemon Professor")

ownname = input("Eich: und dein Name war? ")

remember1 = "Eich: Richtig, dein Name ist "

print(remember1 + ownname)

print("Eich: Dies ist mein Enkel, von jeher wollt ihr einander übertrumpfen!")

rivalname = input("Eich: Hmm, wie war noch gleich sein Name? ")
Proftalk = "Eich: "
remember2 = " Stimmt! Es lag mir auf der Zunge!"

print(Proftalk + rivalname + remember2)

print(" ")

print("Eich: Ich habe hier drei Pokemon für euch!")
print("Eich: Du kannst von Bisasam, Glumanda oder Schiggy wählen")

print("[1] Bisasam")
print("[2] Glumanda")
print("[3] Schiggy")

invalide_eingabe1 = True
while invalide_eingabe1:
    own_pokemon = input("Wähle dein Pokemon: ") #"2" != 2
    invalide_eingabe1 = False

    if (own_pokemon == "1"):
        print("Eich: Du hast Bisasam gewählt!")
        
    elif (own_pokemon == "2"):
        print("Eich: Du hast Glumanda gewählt!")
    elif (own_pokemon == "3"):
        print("Eich: Du hast Schiggy gewählt!")
    elif (own_pokemon == "4"):
        print("Eich: Nun ich hätte nicht gedacht dass jemand Pikachu wählt aber nun gut.")
    else:
        print("Eich: Dies ist keine Pokemon was ich besitze.")
        invalide_eingabe1 = True

if (own_pokemon == "1"):
    own_pokemon = "Bisasam"
elif (own_pokemon == "2"):
    own_pokemon = "Glumanda"
elif (own_pokemon == "3"):
    own_pokemon = "Schiggy"
elif (own_pokemon == "4"):
    own_pokemon = "Pikachu"

own_pokemon_number = int(1)
own_pokemon_level = "5"
    
print(" ")

print("Eich: Dies ist ein Pokedex, er wird euch auf eurer Reise helfen!")
print("Eich: Jetzt aber mal los, eure Reise beginnt!")

print(" ")

print("Pokedex: guck vor uns ist ein Taubsi!")
question1 = input("Mehr über es erfahren? (j/n) ")
if question1 == "j":
    print("Pokedex: Taubsi ist ein vorwiegend in Wäldern lebendes Pokemon,")
    print("das zur Verteidigung mit den Flügeln sand aufwirbelt.")
    question2 = input ("Es angreifen? (j/n) ")
    if question2 == "j":
        print("Du greifst das Taubsi an!")
        print("Los " + own_pokemon)
    elif question2 == "n":
        print("Das wilde Taubsi greift dich an!")
if question1 == "n":
    question2 = input ("Es angreifen? (j/n) ")
    if question2 == "j":
        print("Du greifst das Taubsi an!")
        print("Los " + own_pokemon)
    elif question2 == "n":
        print("Das wilde Taubsi greift dich an!")
print("Ok " + own_pokemon + " ich brauche dich jetzt!")

Attacke = ["Tackle", "Kratzer", "Heuler"]
print(Attacke)

Attacke[0] = "Tackle"
Attacke[1] = "Kratzer"
Attacke[2] = "Heuler"

invalide_eingabe2 = True
while invalide_eingabe2:
    chosen_attack = input("Welche Attacke wählst du? ")
    if (chosen_attack == "Tackle"):
        print("Das Taubsi wurde geschwächt!")
        question3 = input ("Es fangen? (j/n) ")
        invalide_eingabe2 = False
        if question3 == "j":
            print("Ein schütteln")
            print("Zweites schütteln")
            print("Drittes schütteln")
            print("Du hast es gefangen!")
            print("Pokedex: Super! Taubsi wurde in deinem Pokedex regestriert!")
            own_pokemon_number = int(2)
        elif question3 == "n":
            print("Pokedex: Oh nein! Das Taubsi ist geflohen!")
    elif (chosen_attack == "Kratzer"):
        print("Das Taubsi wurde geschwächt!")
        question3 = input ("Es fangen? (j/n) ")
        invalide_eingabe2 = False
        if question3 == "j":
            print("Ein schütteln")
            print("Zweites schütteln")
            print("Drittes schütteln")
            print("Du hast es gefangen!")
            print("Pokedex: Super! Taubsi wurde in deinem Pokedex regestriert!")
            own_pokemon_number = int(2)
        elif question3 == "n":
            print("Pokedex: Oh nein! Das Taubsi ist geflohen!")
    elif (chosen_attack == "Heuler"):
        print("Der Angriff des Pokemons wurde geschwächt!")
    else:
        print("Diese Attacke besitzt dieses Pokemon nicht")

print (" ")

print(rivalname + ": Wen seh ich denn da?")
print(rivalname + ": Wenn ich mich nicht irre heisst das, dass wir kämpfen müssen!")
print("Dein Rivale fordert dich heraus!")
print(rivalname + ": Los Evoli du bist dran!")

rivalhealth = int(20)
rivalattack_tackle = int(4)
rivalattack_kratzer = int(5)
beginn_ownhealth = int(20)
rival_pokemon = "Evoli"


print("Los du bist dran " + own_pokemon + "!")

print(" ")

print("Evoli benutzt Kratzer!")

beginn_ownhealth = beginn_ownhealth - rivalattack_kratzer

print(own_pokemon + " hat schaden erhalten")

print(Attacke)

invalide_eingabe3 = True
while invalide_eingabe3:
    chosen_attackrivalbattle = input("Welche Attacke wählst du? ")
    invalide_eingabe3 = False
    
    if (chosen_attackrivalbattle == "Tackle"):
        print("Los " + own_pokemon + " setze Tackle ein!")
        print("Evoli hat Schaden bekommen!")
        rivalhealth = rivalhealth - int(4)
    elif (chosen_attackrivalbattle == "Kratzer"):
        print("Los " + own_pokemon + " setze Kratzer ein!")
        print("Evoli hat Schaden bekommen!")
        rivalhealth = rivalhealth - int(5)
    elif (chosen_attackrivalbattle == "Heuler"):
        print("Los " + own_pokemon + " setze Heuler ein!")
        print("Die Angriffsstärke von Evoli ist gesinkt.")
        rivalattack_tackle - int(1)
        rivalattack_kratzer - int(1)
    else:
        invalide_eingabe3 = True
        print("Diese Attacke besitzt dieses Pokemon nicht")

print(" ")

print("Evoli benutzt Silberblick.")
print("Die Verteidigung von " + own_pokemon + " wurde gesinkt!")
rivalattack_tackle + int(1)
rivalattack_kratzer + int(1)

print(Attacke)

invalide_eingabe4 = True
while invalide_eingabe4:
    chosen_attackrivalbattle = input("Welche Attacke wählst du? ")
    invalide_eingabe4 = False
    
    if (chosen_attackrivalbattle == "Tackle"):
        print("Los " + own_pokemon + " setze Tackle ein!")
        print("Evoli hat Schaden bekommen!")
        rivalhealth = rivalhealth - int(4)
    elif (chosen_attackrivalbattle == "Kratzer"):
        print("Los " + own_pokemon + " setze Kratzer ein!")
        print("Evoli hat Schaden bekommen!")
        rivalhealth = rivalhealth - int(5)
    elif (chosen_attackrivalbattle == "Heuler"):
        print("Los " + own_pokemon + " setze Heuler ein!")
        print("Die Angriffsstärke von Evoli ist gesinkt.")
        rivalattack_tackle - int(1)
        rivalattack_kratzer - int(1)
    else:
        invalide_eingabe4 = True
        print("Diese Attacke besitzt dieses Pokemon nicht")

print(" ")

print("Evoli benutzt Silberblick.")
print("Die Verteidigung von " + own_pokemon + " wurde gesinkt!")
rivalattack_tackle + int(1)
rivalattack_kratzer + int(1)

print(Attacke)

invalide_eingabe5 = True
while invalide_eingabe5:
    chosen_attackrivalbattle = input("Welche Attacke wählst du? ")
    invalide_eingabe5 = False
    
    if (chosen_attackrivalbattle == "Tackle"):
        print("Los " + own_pokemon + " setze Tackle ein!")
        print("Evoli hat Schaden bekommen!")
        rivalhealth = rivalhealth - int(4)
    elif (chosen_attackrivalbattle == "Kratzer"):
        print("Los " + own_pokemon + " setze Kratzer ein!")
        print("Evoli hat Schaden bekommen!")
        rivalhealth = rivalhealth - int(5)
    elif (chosen_attackrivalbattle == "Heuler"):
        print("Los " + own_pokemon + " setze Heuler ein!")
        print("Die Angriffsstärke von Evoli ist gesinkt.")
        rivalattack_tackle - int(1)
        rivalattack_kratzer - int(1)
    else:
        invalide_eingabe5 = True
        print("Diese Attacke besitzt dieses Pokemon nicht")

print(" ")

print("Evoli benutzt Kratzer!")
print(own_pokemon + " hat schaden erhalten")
beginn_ownhealth = beginn_ownhealth - rivalattack_kratzer

print(Attacke)

invalide_eingabe6 = True
while invalide_eingabe6:
    chosen_attackrivalbattle = input("Welche Attacke wählst du? ")
    invalide_eingabe6 = False
    
    if (chosen_attackrivalbattle == "Tackle"):
        print("Los " + own_pokemon + " setze Tackle ein!")
        print("Evoli hat Schaden bekommen!")
        rivalhealth = rivalhealth - int(4)
    elif (chosen_attackrivalbattle == "Kratzer"):
        print("Los " + own_pokemon + " setze Kratzer ein!")
        print("Evoli hat Schaden bekommen!")
        rivalhealth = rivalhealth - int(5)
    elif (chosen_attackrivalbattle == "Heuler"):
        print("Los " + own_pokemon + " setze Heuler ein!")
        print("Die Angriffsstärke von Evoli ist gesinkt.")
        rivalattack_tackle - int(1)
        rivalattack_kratzer - int(1)
    else:
        invalide_eingabe6 = True
        print("Diese Attacke besitzt dieses Pokemon nicht")

print(" ")

if rivalhealth == int(0):
    print("Du hast gewonnen!")
    print("Du erhälts 256 Pokedollar.")
    print(rivalname + ": Nein! Das kann nicht wahr sein! Ich habe verloren?!")
    print(" ")
    own_pokemon_level = "7"
    print("Dein Pokemon ist 2 lvl aufgestiegen")

    new_attack = "unknown"

    if (own_pokemon == "Bisasam"):
        new_attack = "Rankenheib"
        Attacke = ["Tackle", "Kratzer", "Heuler", "Rankenhieb"]
        Attacke[3] = "Rankenhieb"
        print(own_pokemon + " hat Rankenheib erlernt!")
    elif (own_pokemon == "Glumanda"):
        new_attack = "Glut"
        Attacke = ["Tackle", "Kratzer", "Heuler", "Glut"]
        Attacke[3] = "Glut"
        print(own_pokemon + " hat Glut erlernt!")
    elif (own_pokemon == "Schiggy"):
        new_attack = "Blubber"
        Attacke = ["Tackle", "Kratzer", "Heuler", "Blubber"]
        Attacke[3] = "Blubber"
        print(own_pokemon + " hat Blubber erlernt!")
    else:
        new_attack = "Donnerschock"
        Attacke = ["Tackle", "Kratzer", "Heuler", "Donnerschock"]
        Attacke[3] = "Donnerschock"
        print(own_pokemon + " hat Donnerschock erlernt!")
    
else:
    print("Evoli benutzt Kratzer!")
    print(own_pokemon + " hat schaden erhalten")
    beginn_ownhealth = beginn_ownhealth - rivalattack_kratzer

    print(Attacke)

    invalide_eingabe6 = True
    while invalide_eingabe6:
        chosen_attackrivalbattle = input("Welche Attacke wählst du? ")
        invalide_eingabe6 = False
    
        if (chosen_attackrivalbattle == "Tackle"):
            print("Los " + own_pokemon + " setze Tackle ein!")
            print("Evoli hat Schaden bekommen!")
            rivalhealth = rivalhealth - int(4)
        elif (chosen_attackrivalbattle == "Kratzer"):
            print("Los " + own_pokemon + " setze Kratzer ein!")
            print("Evoli hat Schaden bekommen!")
            rivalhealth = rivalhealth - int(5)
        elif (chosen_attackrivalbattle == "Heuler"):
            print("Los " + own_pokemon + " setze Heuler ein!")
            print("Die Angriffsstärke von Evoli ist gesinkt.")
            rivalattack_tackle - int(1)
            rivalattack_kratzer - int(1)
        else:
            invalide_eingabe6 = True
            print("Diese Attacke besitzt dieses Pokemon nicht")

    print(" ")

    if (rivalhealth < int(0)):
        print("Du hast gewonnen!")
        print("Du erhälts 256 Pokedollar.")
        print(rivalname + ": Nein! Das kann nicht wahr sein! Ich habe verloren?!")

    if beginn_ownhealth == int(0):
        print("Du hast verloren!")
        print(rivalname + ": Ich wusste, dass ich gewinnen werde!")
        print(rivalname + ": Wie du hast keine Pokedollar? Na gut dieses mal über nehme ich.")

if beginn_ownhealth == int(0):
    print("Du hast verloren!")
    print(rivalname + ": Ich wusste ich werde gewinnen!")
    print(rivalname + ": Wie du hast keine Pokedollar? Na gut dieses mal über nehme ich.")
    











