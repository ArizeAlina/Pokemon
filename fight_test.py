#!/bin/python3

import random

RAttack1 = "RBaseAttack1"
RAttack2 = "RBaseAttack2"
RAttack3 = "RBaseAttack3"
RAttack4 = "RBaseAttack4"

def rival_attack():
    rival_attacks = [RAttack1, RAttack2, RAttack3, RAttack4]
    print(random. choice(rival_attacks))

rival_attack()


OAttack1 = "OBaseAttack1"
OAttack2 = "OBaseAttack2"
OAttack3 = "OBaseAttack3"
OAttack4 = "OBaseAttack4"
own_attack_damage = int(0)

def own_attack():
    print("Its your turn!")
    own_attacks = [OAttack1, OAttack2, OAttack3, OAttack4]
    print(OAttack1, OAttack2, OAttack3, OAttack4, sep=",")
    invalide_eingabe = True
    while invalide_eingabe:
        chosen_attack = input("Choose your Attack! ")
        invalide_eingabe = False
        
        if (chosen_attack == OAttack1):
            own_attack_damage = int(30)
        elif (chosen_attack == OAttack2):
            own_attack_damage = int(35)
        elif (chosen_attack == OAttack3):
            own_attack_damage = int(25)
        elif (chosen_attack == OAttack4):
            own_attack_damage = int(50)
        else:
            invalide_eingabe6 = True
            print("Attack not viable")
        print(chosen_attack)

own_attack()

def rival_damage_taken():
    rival_health = int(100)
    if (chosen_attack == OAttack1):
        rival_health = rival_health - int(30)
    elif (chosen_attack == OAttack2):
        rival_health = rival_health - int(35)
    elif (chosen_attack == OAttack3):
        rival_health = rival_health - int(25)
    elif (chosen_attack == OAttack4):
        rival_health = rival_health - int(50)
    else:
        print("Attack not viable")
    print(rival_health)

rival_damage_taken()
    
    
