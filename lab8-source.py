# Partner lab 8 example

import random

print "A monster approaches! Prepare to fight!"

playerHealth = 100
monsterHealth = 100
punchDmg = 5
swordDmg = 10
fireballDmg = 30

# TODO:
# Loop - When should it stop?
# Input - user gets to choose attack
# Calculating the damage done by the user and the monster
# Output - printing damage
# Printing a victory message

mana = 2
while (playerHealth > 0) and (monsterHealth > 0):
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "You have " +str(playerHealth)+ " health."
    print "The monster has " +str(monsterHealth)+ " health."
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "What attack do you wish to use?"
    print "1 - Punch. 2 - Sword. 3 - Fireball"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    attack = int(raw_input())
    if attack == 1:
        print "You Punch the monster!"
        monsterHealth = monsterHealth - punchDmg
        print "The monster now has " +str(monsterHealth)+ " health."
    if attack == 2:
        print "You slice the monster!"
        monsterHealth = monsterHealth - swordDmg
        print "The monster now has " +str(monsterHealth)+ " health."
    if attack == 3:
        if mana % 2 == 0:
            mana = mana - 2
            print "You set the monster ablaze."
            monsterHealth = monsterHealth - fireballDmg
            print "The monster now has " +str(monsterHealth)+ " health."
        if mana % 2 != 0:
            print "You do not have enough mana to cast fireball."
            print "2 mana is required. You currently have " +str(mana) "."
            print "Try another attack."
    if attack == 1337:
        print "How Much Damage Yo Wanna Do M8????"
        leetDmg = int(raw_input())
        print "Those 1337 Hacks Doe"
        monsterHealth = monsterHealth - leetDmg
        print "The monster has " +str(monsterHealth)+ " health."
    mana = mana + 1