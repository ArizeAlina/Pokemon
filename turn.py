import random

turn_rival_pokemon = "Base Rival Pokemon"
turn_own_pokemon = "Base own Pokemon"

own_health = int(100)
rival_health = int(100)

RAttack1 = "RAttack1"
RAttack2 = "RAttack2"
RAttack3 = "RAttack3"
RAttack4 = "RAttack4"

RAttack_damage1 = int(10)
RAttack_damage2 = int(20)
RAttack_damage3 = int(30)
RAttack_damage4 = int(40)

ODamage_reduced_by1 = int(0)
ODamage_reduced_by2 = int(0)
ODamage_reduced_by3 = int(0)
ODamage_reduced_by4 = int(0)

RDamage_buffed_by1 = int(0)
RDamage_buffed_by2 = int(0)
RDamage_buffed_by3 = int(0)
RDamage_buffed_by4 = int(0)

OAttack1 = "OAttack1"
OAttack2 = "OAttack2"
OAttack3 = "OAttack3"
OAttack4 = "OAttack4"

OAttack_damage1 = int(10)
OAttack_damage2 = int(20)
OAttack_damage3 = int(30)
OAttack_damage4 = int(40)

RDamage_reduced_by1 = int(0)
RDamage_reduced_by2 = int(0)
RDamage_reduced_by3 = int(0)
RDamage_reduced_by4 = int(0)

ODamage_buffed_by1 = int(0)
ODamage_buffed_by2 = int(0)
ODamage_buffed_by3 = int(0)
ODamage_buffed_by4 = int(0)

def rival_attack_effect1(own_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, ODamage_reduced_by1, RDamage_buffed_by1):

    if RAttack_damage1 >= int(0):
        own_health = own_health - RAttack_damage1
    else:
        own_health = own_health

    if ODamage_reduced_by1 >= int(0):
        OAttack_damage1 = OAttack_damage1 - ODamage_reduced_by1
        OAttack_damage2 = OAttack_damage2 - ODamage_reduced_by1
        OAttack_damage3 = OAttack_damage3 - ODamage_reduced_by1
        OAttack_damage4 = OAttack_damage4 - ODamage_reduced_by1
    else:
        OAttack_damage1 = OAttack_damage1
        OAttack_damage2 = OAttack_damage2
        OAttack_damage3 = OAttack_damage3
        OAttack_damage4 = OAttack_damage4

    if RDamage_buffed_by1 >= int(0):
        RAttack_damage1 = RAttack_damage1 + RDamage_buffed_by1
        RAttack_damage2 = RAttack_damage2 + RDamage_buffed_by1
        RAttack_damage3 = RAttack_damage3 + RDamage_buffed_by1
        RAttack_damage4 = RAttack_damage4 + RDamage_buffed_by1
    else:
        RAttack_damage1 = RAttack_damage1
        RAttack_damage2 = RAttack_damage2
        RAttack_damage3 = RAttack_damage3
        RAttack_damage4 = RAttack_damage4
        
    return own_health, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4


def rival_attack_effect2(own_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, ODamage_reduced_by2, RDamage_buffed_by2):

    if RAttack_damage1 >= int(0):
        own_health = own_health - RAttack_damage2
    else:
        own_health = own_health

    if ODamage_reduced_by1 >= int(0):
        OAttack_damage1 = OAttack_damage1 - ODamage_reduced_by2
        OAttack_damage2 = OAttack_damage2 - ODamage_reduced_by2
        OAttack_damage3 = OAttack_damage3 - ODamage_reduced_by2
        OAttack_damage4 = OAttack_damage4 - ODamage_reduced_by2
    else:
        OAttack_damage1 = OAttack_damage1
        OAttack_damage2 = OAttack_damage2
        OAttack_damage3 = OAttack_damage3
        OAttack_damage4 = OAttack_damage4

    if RDamage_buffed_by1 >= int(0):
        RAttack_damage1 = RAttack_damage1 + RDamage_buffed_by2
        RAttack_damage2 = RAttack_damage2 + RDamage_buffed_by2
        RAttack_damage3 = RAttack_damage3 + RDamage_buffed_by2
        RAttack_damage4 = RAttack_damage4 + RDamage_buffed_by2
    else:
        RAttack_damage1 = RAttack_damage1
        RAttack_damage2 = RAttack_damage2
        RAttack_damage3 = RAttack_damage3
        RAttack_damage4 = RAttack_damage4
        
    return own_health, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4


def rival_attack_effect3(own_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, ODamage_reduced_by3, RDamage_buffed_by3):

    if RAttack_damage1 >= int(0):
        own_health = own_health - RAttack_damage3
    else:
        own_health = own_health

    if ODamage_reduced_by1 >= int(0):
        OAttack_damage1 = OAttack_damage1 - ODamage_reduced_by3
        OAttack_damage2 = OAttack_damage2 - ODamage_reduced_by3
        OAttack_damage3 = OAttack_damage3 - ODamage_reduced_by3
        OAttack_damage4 = OAttack_damage4 - ODamage_reduced_by3
    else:
        OAttack_damage1 = OAttack_damage1
        OAttack_damage2 = OAttack_damage2
        OAttack_damage3 = OAttack_damage3
        OAttack_damage4 = OAttack_damage4

    if RDamage_buffed_by1 >= int(0):
        RAttack_damage1 = RAttack_damage1 + RDamage_buffed_by3
        RAttack_damage2 = RAttack_damage2 + RDamage_buffed_by3
        RAttack_damage3 = RAttack_damage3 + RDamage_buffed_by3
        RAttack_damage4 = RAttack_damage4 + RDamage_buffed_by3
    else:
        RAttack_damage1 = RAttack_damage1
        RAttack_damage2 = RAttack_damage2
        RAttack_damage3 = RAttack_damage3
        RAttack_damage4 = RAttack_damage4
        
    return own_health, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4


def rival_attack_effect4(own_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, ODamage_reduced_by4, RDamage_buffed_by4):

    if RAttack_damage1 >= int(0):
        own_health = own_health - RAttack_damage4
    else:
        own_health = own_health

    if ODamage_reduced_by1 >= int(0):
        OAttack_damage1 = OAttack_damage1 - ODamage_reduced_by4
        OAttack_damage2 = OAttack_damage2 - ODamage_reduced_by4
        OAttack_damage3 = OAttack_damage3 - ODamage_reduced_by4
        OAttack_damage4 = OAttack_damage4 - ODamage_reduced_by4
    else:
        OAttack_damage1 = OAttack_damage1
        OAttack_damage2 = OAttack_damage2
        OAttack_damage3 = OAttack_damage3
        OAttack_damage4 = OAttack_damage4

    if RDamage_buffed_by1 >= int(0):
        RAttack_damage1 = RAttack_damage1 + RDamage_buffed_by4
        RAttack_damage2 = RAttack_damage2 + RDamage_buffed_by4
        RAttack_damage3 = RAttack_damage3 + RDamage_buffed_by4
        RAttack_damage4 = RAttack_damage4 + RDamage_buffed_by4
    else:
        RAttack_damage1 = RAttack_damage1
        RAttack_damage2 = RAttack_damage2
        RAttack_damage3 = RAttack_damage3
        RAttack_damage4 = RAttack_damage4
        
    return own_health, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4


def own_attack_effect1(rival_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by1, ODamage_buffed_by1):

    if RAttack_damage1 >= int(0):
        rival_health = rival_health - OAttack_damage1
    else:
        rival_health = rival_health

    if ODamage_reduced_by1 >= int(0):
        RAttack_damage1 = RAttack_damage1 - RDamage_reduced_by1
        RAttack_damage2 = RAttack_damage2 - RDamage_reduced_by1
        RAttack_damage3 = RAttack_damage3 - RDamage_reduced_by1
        RAttack_damage4 = RAttack_damage4 - RDamage_reduced_by1
    else:
        RAttack_damage1 = RAttack_damage1
        RAttack_damage2 = RAttack_damage2
        RAttack_damage3 = RAttack_damage3
        RAttack_damage4 = RAttack_damage4

    if RDamage_buffed_by1 >= int(0):
        OAttack_damage1 = OAttack_damage1 + ODamage_buffed_by1
        OAttack_damage2 = OAttack_damage2 + ODamage_buffed_by1
        OAttack_damage3 = OAttack_damage3 + ODamage_buffed_by1
        OAttack_damage4 = OAttack_damage4 + ODamage_buffed_by1
    else:
        OAttack_damage1 = OAttack_damage1
        OAttack_damage2 = OAttack_damage2
        OAttack_damage3 = OAttack_damage3
        OAttack_damage4 = OAttack_damage4
        
    return rival_health, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4


def own_attack_effect2(rival_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by2, ODamage_buffed_by2):

    if RAttack_damage1 >= int(0):
        rival_health = rival_health - OAttack_damage2
    else:
        rival_health = rival_health

    if ODamage_reduced_by1 >= int(0):
        RAttack_damage1 = RAttack_damage1 - RDamage_reduced_by2
        RAttack_damage2 = RAttack_damage2 - RDamage_reduced_by2
        RAttack_damage3 = RAttack_damage3 - RDamage_reduced_by2
        RAttack_damage4 = RAttack_damage4 - RDamage_reduced_by2
    else:
        RAttack_damage1 = RAttack_damage1
        RAttack_damage2 = RAttack_damage2
        RAttack_damage3 = RAttack_damage3
        RAttack_damage4 = RAttack_damage4

    if RDamage_buffed_by1 >= int(0):
        OAttack_damage1 = OAttack_damage1 + ODamage_buffed_by2
        OAttack_damage2 = OAttack_damage2 + ODamage_buffed_by2
        OAttack_damage3 = OAttack_damage3 + ODamage_buffed_by2
        OAttack_damage4 = OAttack_damage4 + ODamage_buffed_by2
    else:
        OAttack_damage1 = OAttack_damage1
        OAttack_damage2 = OAttack_damage2
        OAttack_damage3 = OAttack_damage3
        OAttack_damage4 = OAttack_damage4
        
    return rival_health, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4


def own_attack_effect3(rival_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by3, ODamage_buffed_by3):

    if RAttack_damage1 >= int(0):
        rival_health = rival_health - OAttack_damage3
    else:
        rival_health = rival_health

    if ODamage_reduced_by1 >= int(0):
        RAttack_damage1 = RAttack_damage1 - RDamage_reduced_by3
        RAttack_damage2 = RAttack_damage2 - RDamage_reduced_by3
        RAttack_damage3 = RAttack_damage3 - RDamage_reduced_by3
        RAttack_damage4 = RAttack_damage4 - RDamage_reduced_by3
    else:
        RAttack_damage1 = RAttack_damage1
        RAttack_damage2 = RAttack_damage2
        RAttack_damage3 = RAttack_damage3
        RAttack_damage4 = RAttack_damage4

    if RDamage_buffed_by1 >= int(0):
        OAttack_damage1 = OAttack_damage1 + ODamage_buffed_by3
        OAttack_damage2 = OAttack_damage2 + ODamage_buffed_by3
        OAttack_damage3 = OAttack_damage3 + ODamage_buffed_by3
        OAttack_damage4 = OAttack_damage4 + ODamage_buffed_by3
    else:
        OAttack_damage1 = OAttack_damage1
        OAttack_damage2 = OAttack_damage2
        OAttack_damage3 = OAttack_damage3
        OAttack_damage4 = OAttack_damage4
        
    return rival_health, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4


def own_attack_effect4(rival_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by4, ODamage_buffed_by4):

    if RAttack_damage1 >= int(0):
        rival_health = rival_health - OAttack_damage4
    else:
        rival_health = rival_health

    if ODamage_reduced_by1 >= int(0):
        RAttack_damage1 = RAttack_damage1 - RDamage_reduced_by4
        RAttack_damage2 = RAttack_damage2 - RDamage_reduced_by4
        RAttack_damage3 = RAttack_damage3 - RDamage_reduced_by4
        RAttack_damage4 = RAttack_damage4 - RDamage_reduced_by4
    else:
        RAttack_damage1 = RAttack_damage1
        RAttack_damage2 = RAttack_damage2
        RAttack_damage3 = RAttack_damage3
        RAttack_damage4 = RAttack_damage4

    if RDamage_buffed_by1 >= int(0):
        OAttack_damage1 = OAttack_damage1 + ODamage_buffed_by4
        OAttack_damage2 = OAttack_damage2 + ODamage_buffed_by4
        OAttack_damage3 = OAttack_damage3 + ODamage_buffed_by4
        OAttack_damage4 = OAttack_damage4 + ODamage_buffed_by4
    else:
        OAttack_damage1 = OAttack_damage1
        OAttack_damage2 = OAttack_damage2
        OAttack_damage3 = OAttack_damage3
        OAttack_damage4 = OAttack_damage4
        
    return rival_health, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4


def turn(turn_rival_pokemon, turn_own_pokemon, own_health, rival_health, RAttack1, RAttack2, RAttack3, RAttack4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, ODamage_reduced_by1, ODamage_reduced_by2, ODamage_reduced_by3, ODamage_reduced_by4, RDamage_buffed_by1, RDamage_buffed_by2, RDamage_buffed_by3, RDamage_buffed_by4, OAttack1, OAttack2, OAttack3, OAttack4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by1, RDamage_reduced_by2, RDamage_reduced_by3, RDamage_reduced_by4,ODamage_buffed_by1, ODamage_buffed_by2, ODamage_buffed_by3, ODamage_buffed_by4):
    print("")
    
    rival_attacks = [RAttack1, RAttack2, RAttack3, RAttack3]
    chosen_rival_attack = random.choice(rival_attacks)
    print(turn_rival_pokemon + " uses " + chosen_rival_attack)
    
    if (chosen_rival_attack == RAttack1):
        rival_attack_effect1(own_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, ODamage_reduced_by1, RDamage_buffed_by1)
    elif (chosen_rival_attack == RAttack2):
        rival_attack_effect2(own_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, ODamage_reduced_by2, RDamage_buffed_by2)  
    elif (chosen_rival_attack == RAttack3):
        rival_attack_effect3(own_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, ODamage_reduced_by3, RDamage_buffed_by3)
    elif (chosen_rival_attack == RAttack4):
        rival_attack_effect4(own_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, ODamage_reduced_by4, RDamage_buffed_by4)
    else:
        print("error")   
    
    print(turn_own_pokemon + " got damaged!")
    print("")
    
    print("Its your turn!")
    own_attacks = [OAttack1, OAttack2, OAttack3, OAttack4]
    print(OAttack1, OAttack2, OAttack3, OAttack4, sep=", ")
    invalide_eingabe = True
    while invalide_eingabe:
        chosen_attack = input("Choose your Attack! ")
        invalide_eingabe = False
        
        if (chosen_attack == OAttack1):
            own_attack_effect1(rival_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by1, ODamage_buffed_by1) 
        elif (chosen_attack == OAttack2):
            own_attack_effect2(rival_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by2, ODamage_buffed_by2)  
        elif (chosen_attack == OAttack3):
            own_attack_effect3(rival_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by3, ODamage_buffed_by3) 
        elif (chosen_attack == OAttack4):
            own_attack_effect4(rival_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by4, ODamage_buffed_by4) 
        else:
            invalide_eingabe = True
            print("Attack not viable")

    print(turn_own_pokemon + " uses " + chosen_attack)
    print("")
    print(turn_own_pokemon + " has " + str(own_health) + " hp left!")
    print(turn_rival_pokemon + " has " + str(rival_health) + " hp left!")

    return own_health, rival_health, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4

turn(turn_rival_pokemon, turn_own_pokemon, own_health, rival_health, RAttack1, RAttack2, RAttack3, RAttack4, RAttack_damage1, RAttack_damage2, RAttack_damage3, RAttack_damage4, ODamage_reduced_by1, ODamage_reduced_by2, ODamage_reduced_by3, ODamage_reduced_by4, RDamage_buffed_by1, RDamage_buffed_by2, RDamage_buffed_by3, RDamage_buffed_by4, OAttack1, OAttack2, OAttack3, OAttack4, OAttack_damage1, OAttack_damage2, OAttack_damage3, OAttack_damage4, RDamage_reduced_by1, RDamage_reduced_by2, RDamage_reduced_by3, RDamage_reduced_by4, ODamage_buffed_by1, ODamage_buffed_by2, ODamage_buffed_by3, ODamage_buffed_by4)


