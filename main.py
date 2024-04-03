import csv
import os
from time import sleep
import random

ownkingdom = ''
cooldown = 'F'
monsterhp = 60
mdamage = 3
mname = 'Monster'
pts = 0
atkrange = [1, 5]
defrange = [1, 3]
hp = 30
class1 = ""
level = 1
exp = 0
expgained = 0
goldgained = 15
kvisit = 0
Kingdom_visit = {}
alliance = []
monencountered = 0
ex = 'T'
ability = False
abilities = []
Kingdoms = [
    'orc kingdom', 'elf kingdom', 'wizarding abode', 'human settlement',
    'centaur forest'
]
inv = []


def orc():
    global baseatk1
    global powerup1
    global ownkingdom
    baseatk1 = "hit with axe"
    powerup1 = "bite enemy"
    ownkingdom = 'orc kingdom'
    Kingdoms.remove('orc kingdom')


def mage():
    global baseatk1
    global powerup1
    global ownkingdom
    baseatk1 = "throw fireball"
    powerup1 = "blast enemy with a fireball"
    ownkingdom = 'wizarding abode'
    Kingdoms.remove('wizarding abode')


def humanwarrior():
    global baseatk1
    global powerup1
    global ownkingdom
    ownkingdom = 'human settlement'
    baseatk1 = "Stab with dagger"
    powerup1 = "Fiery slash with sword"
    Kingdoms.remove('human settlement')


def centaur():
    global baseatk1
    global powerup1
    global ownkingdom
    ownkingdom = 'centaur forest'
    baseatk1 = "kick with hooves"
    powerup1 = "Speed attack"
    Kingdoms.remove('centaur forest')


def elf():
    global baseatk1
    global powerup1
    global ownkingdom
    ownkingdom = 'elf kingdom'
    baseatk1 = "hit with spear"
    powerup1 = "harness the power of the dead"
    Kingdoms.remove('elf kingdom')


def monster():
    global hp
    global mdamage
    global mname
    global defrange
    global defense
    defense = random.randint(defrange[0], defrange[1])
    dmg = random.randint(mdamage[0], mdamage[1])
    somename = (dmg - defense)
    if somename <= 0:
        somename = 0
    hp -= somename
    print("the", mname, "has done \u001b[31m", somename,
          "\u001b[0m points of damage to you")
    print("\u001b[32m\nyou have", hp, "health points remaining\u001b[0m\n")


def shop():
    global goldgained
    global hp
    global defense
    global atk
    global ex

    def check(m):
        global ex
        if m > goldgained:
            print("you don't have enough gold bars")
            ex = 'F'
            return

    print("\n\u001b[32mWelcome to Unagi~The magical store\u001b[0m\n")

    print('You currently have', goldgained, 'gold bars.')
    while True:
        try:
            what = int(
                input('''What would you like to buy?
                  0: Exit.
                  1: Lesser health potion costs 12 gold.
                  2: Greater health potion costs 35 gold.
                  3: Rusty sword costs 24 gold.
                  4: Battered shield costs 17 gold.
                  5: Runic axe costs 35 gold.
                  6: Runic shield costs 35 gold.\n'''))
        except ValueError:
            print("Invalid Input. Try again")
            continue
        else:
            break
    if what == 0:
        print('Have a safe journey!')
    elif what == 1:
        check(12)
        if ex == 'T':
            goldgained -= 12
            inv.append('Lesser Health Potion')
            print('Lesser health potion has been added to your inventory')
            print('\u001b[33;1mGold bars remaining=\u001b[0m', goldgained)
    elif what == 2:
        check(35)
        if ex == 'T':
            goldgained -= 35
            inv.append('Greater Health Potion')
            print('Greater health potion has been added to your inventory')
            print('\u001b[33;1mGold bars remaining=\u001b[0m', goldgained)
    elif what == 3:
        check(24)
        if ex == 'T':
            goldgained -= 24
            atkrange[0] += 2
            atkrange[1] += 2
            inv.append("Rusty Sword")
            print(
                '''Your Attack has been increased by 2.
            Attack power=''', atkrange[0], '''
            \u001b[33;1mGold bars remaining=\u001b[0m''', goldgained)
    elif what == 4:
        check(17)
        if ex == 'T':
            goldgained -= 17
            defrange[0] += 1
            defrange[1] += 1
            inv.append("Battered Shield")
            print(
                '''Your Defence has been increased by 1 .
            Defence shielding=''', defrange[0], '''
            \u001b[33;1mGold bars remaining=\u001b[0m''', goldgained)
    elif what == 5:
        check(35)
        if ex == 'T':
            goldgained -= 35
            atkrange[0] *= 2
            atkrange[1] *= 2
            inv.append("Runic Axe")
            print(
                '''Your Attack has been doubled.
            Attack power=''', atkrange[0], '''
            \u001b[33;1mGold bars remaining=\u001b[0m''', goldgained)
    elif what == 6:
        check(35)
        if ex == 'T':
            goldgained -= 48
            defrange[0] = 2 * defrange[0]
            defrange[1] = 2 * defrange[1]
            inv.append("Runic Shield")
            print(
                '''Your Defence has been doubled.
            Defence shielding=''', defrange[0], '''
            \u001b[33;1mGold bars remaining=\u001b[0m''', goldgained)
    else:
        print("You haven't choosen from the given options")
        print('Thanks for vising Unagi~The magical store')


def inventory():
    global hp
    print("Inventory contents:")
    if len(inv) != 0:
        for i in range(1, len(inv) + 1):
            print(i, inv[i - 1])
    else:
        print("Inventory is empty")
        print()
        return
    while True:
        try:
            want = int(
                input('''What would you like to use(number)?
  Press 0 to exit'''))
        except ValueError:
            print("Invalid input. Try again")
            continue
        else:
            break

        if want <= len(inv) and want > 0:
            a = inv[want - 1]
            if a == 'Lesser Health Potion':
                hp += 10
                print(
                    '''Your Health points have been increased by 10
Current Health Points=''', hp)
                inv.remove(a)
                '''with open("inventory.txt", "r") as f:
                lines = f.readlines()
            with open("inventory.txt", "w") as f:
                count = 0
                for line in lines:
                    if line.strip(
                            "\n") != "Lesser Health Potion" or count == 1:
                        f.write(line)
                    else:
                        count += 1'''

            elif a == 'Greater Health Potion':
                hp += 20
                print(
                    '''Your Health points have been increased by 20
            Current Health Points=''', hp)
                inv.remove(a)
                '''with open("inventory.txt", "r") as f:
                lines = f.readlines()
            with open("inventory.txt", "w") as f:
                count = 0
                for line in lines:
                    if line.strip(
                            "\n") != "Greater Health Potion" or count == 1:
                        f.write(line)
                    else:
                        count += 1'''

            elif a == 'Rusty Sword' or 'Battered Shield' or 'Runic axe' or 'Runic Shield' or 'Ivan The Terrible':
                print('Item is not usuable during fights')
        else:
            print("Item is not in the inventory.")
            return


def monsterchoose():
    global level
    global monsterhp
    global mdamage
    global mname
    global expgained
    global goldgained
    if level == 1 or level == 2:
        choose = random.randint(1, 2)
        if choose == 1:
            mname = 'Bandit'
            monsterhp = 35
            mdamage = [2, 5]
            expgained = 5
            goldgained += 5
        elif choose == 2:
            mname = 'Trog'
            monsterhp = 40
            mdamage = [3, 6]
            expgained = 7
            goldgained += 7
    elif level == 3 or level == 4 or level == 5:
        choose = random.randint(1, 2)
        if choose == 1:
            mname = 'Evil Gnome'
            monsterhp = 45
            mdamage = [4, 7]
            expgained = 9
            goldgained += 10
        elif choose == 2:
            mname = 'Pirate'
            monsterhp = 50
            mdamage = [5, 8]
            expgained = 11
            goldgained += 13
    elif level >= 6:
        choose = random.randint(1, 2)
        if choose == 1:
            mname = 'Demon'
            monsterhp = 65
            mdamage = [6, 9]
            expgained = 13
            goldgained += 17
        elif choose == 2:
            mname = 'Witch'
            monsterhp = 60
            mdamage = [7, 10]
            expgained = 15
            goldgained += 20


def gf():
    global monsterhp
    global pts
    global atk
    global defense
    global hp
    global baseatk1
    global powerup1
    global abilities

    def choose():
        options = [baseatk1, powerup1, 'Check inventory']
        if ability == True:
            options.extend(abilities)
        print('What do you choose to do?')
        for i in range(1, len(options) + 1):
            print('Press', i, 'to', options[i - 1])
        while True:
            try:
                Input = int(input())
            except ValueError:
                print("Invalid input. Try again.")
                continue
            else:
                break
        if Input == 1:
            baseatk()
        elif Input == 2:
            powerup()
        elif Input == 3:
            inventory()
        elif ability == True and Input == 4:
            specialability(options[3])
        elif ability == True and Input == 5:
            specialability(options[4])
        else:
            print("invalid input")
            choose()

    def specialability(x):
        global monsterhp
        global cooldown
        if cooldown == 'F':
            if x == 'Blast enemy with a thunderbolt':
                damage = (random.randint(atkrange[0], atkrange[1])) * 3
                print("you have used your powerup and caused", damage,
                      "damage")
                monsterhp -= damage
                cooldown = 'T'
            elif x == 'Guns blazing':
                damage = (random.randint(atkrange[0] + 10, atkrange[1] + 10))
                print("you have used your powerup and caused", damage,
                      "damage\n")
                monsterhp -= damage
                cooldown = 'T'
        else:
            print(x, 'is on cooldown\n')
            choose()

    def baseatk():
        global monsterhp
        global cooldown
        damage = random.randint(atkrange[0], atkrange[1])
        print("you have done \u001b[31m", damage,
              "\u001b[0m points of damage with your base attack\n")
        monsterhp -= damage
        cooldown = 'F'

    def powerup():
        global monsterhp
        global cooldown
        if cooldown == 'F' and class1.lower == 'centaur':

            damage = 4 * (random.randint(atkrange[0], atkrange[1]))
            print("you have used your powerup and caused", damage, "damage\n")
            monsterhp -= damage
            cooldown = 'T'
        elif cooldown == 'F':
            damage = (random.randint(atkrange[0], atkrange[1])) * 2
            print("you have used your powerup and caused", damage, "damage\n")
            monsterhp -= damage
            cooldown = 'T'
        else:
            print("Ability is on cooldown\n")
            choose()

    choose()


def fight():
    global cooldown
    global monsterhp
    global mname
    global exp
    global expgained
    global goldgained
    global monencountered
    monsterchoose()
    print("\u001b[33;1mA", mname,
          "is in your way and ready to fight\u001b[0m ")
    while monsterhp > 0 and hp > 0:
        gf()
        if monsterhp <= 0:
            print("You have defeated the", mname)
            print("You have", hp, "health points remaining")
            print()
            exp += expgained
            monencountered += 1
            print(
                "You have gained", expgained,
                "experience points for fighting the", mname,
                "\n You will automatically level up once you have gained enough experience points.\nYou now have ",
                goldgained, "goldbars, which can be used in the shop.")
            print()
            expgained = 0
            levelup()
            return
        elif monsterhp > 0 and hp > 0:
            print("\u001b[36mthe", mname, "has", monsterhp,
                  "health points remaining\u001b[0m\n")
            monster()
        elif hp <= 0:
            print("you have been defeated by the", mname)
            print("you must restart from the previous quest point")
            print()


def charbuild():
    global class1
    class1 = input('''
It is time to choose your class. 
Beware you cannot alter your class once chosen. 
               
The available classes are: Mage, Elf, Orc, Warrior, Centaur. 
Enter your chosen class here: ''')
    if class1.lower() == "mage":
        mage()
    elif class1.lower() == "orc":
        orc()
    elif class1.lower() == "elf":
        elf()
    elif class1.lower() == "warrior":
        humanwarrior()
    elif class1.lower() == "centaur":
        centaur()
    else:
        charbuild()


def statslevelup():
    global pts
    global atkrange
    global defrange
    global hp

    while pts >= 1:
        print('''
\u001b[33;1mYour current attribute values are:\u001b[0m
\u001b[31mAttack (a): {}\u001b[0m
\u001b[34mDefense (d): {}\u001b[0m
\u001b[32mHealth (h): {}\u001b[0m'''.format(atkrange[0], defrange[0], hp))

        try:
            a = input("\nWhich attribute would you like to increase ? ")
            p = int(input('How many points would you like to allocate ? '))
            if p <= 0:
                print('Enter non-negative value')
                statslevelup()
                break
            elif p <= pts:
                if a.lower() == 'attack' or a.lower() == 'a':
                    atkrange[0] += p
                    atkrange[1] += p
                elif a.lower() == 'defense' or a.lower() == 'd':
                    defrange[0] += p
                    defrange[1] += p
                elif a.lower() == 'health' or a.lower() == 'h':
                    hp += 3 * p
                else:
                    print("Invalid Input. Try again. \n")
                    statslevelup()
                    break
                pts -= p
                print('''Attributes have successfully been updated.
\u001b[46;1mPoints left:{}\u001b[0m'''.format(pts))
                print('''
Your updated attribute values are:
\u001b[31mAttack: {}\u001b[0m
\u001b[34mDefense: {}\u001b[0m
\u001b[32mHealth: {}\u001b[0m'''.format(atkrange[0], defrange[0], hp))
            else:
                print("Not enough points. Try again")
                statslevelup()
                break
                print()
        except ValueError:
            print("Invalid Input. Try again.")


def dice():
    import random
    global dicecount
    global level
    global goldgained
    levelbackup = level
    spin = random.randint(1, 20)
    print(
        '''
\u001b[32mSPINNING
\u001b[36m...
\u001b[35m..
\u001b[34m.
\u001b[33mYou rolled a 
''', spin, '\u001b[0m\n')
    if spin in range(1, 6):
        if level <= 2:
            level = 3
            print(
                "\u001b[34mYou have encountered a high-level monster\u001b[0m")
            fight()
            level = levelbackup
        else:
            level = 5
            print(
                "\u001b[34mYou have encountered a high-level monster\u001b[0m")
            fight()
            level = levelbackup

    if spin in range(6, 11):
        print("\u001b[34mYou have encountered a low-level monster\u001b[0m")
        fight()
    if spin in range(11, 16):
        print("\u001b[34mYou encountered nothing\u001b[0m")
    if spin in range(16, 21):
        import random
        gcount = random.randint(2, 10)
        print("\u001b[34mYou stumbled across", gcount,
              "gold. Congratulations !\u001b[0m")
        goldgained += gcount


def levelup():
    global level
    global exp
    global pts
    if exp > 0:
        while exp >= level * 5:
            exp -= level * 5
            level += 1
            print("You have levelled up to", level)
            print(
                "Beware, the level of monsters will also increase. Tread carefully."
            )
            print(
                "You have gained 2 points, you can now level up your attributes"
            )
            pts += 2
            statslevelup()


def elfkingdom():
    global Kingdoms
    global atkrange
    global ability
    global abilities
    os.system('clear')
    print('''A scrawny elf approaches you

You are here to meet our Queen Vecna right ?
To do so, first answer the riddle

If you wish to give up, press 'n' \n''')

    cond = 'n'
    while cond == 'n':
        print(
            "\u001b[31mMany have heard me, yet nobody has seen me. I won't speak back unless spoken to. What am I?\u001b[0m"
        )
        answer = input()
        if answer.lower() == 'echo' or answer.lower(
        ) == 'an echo' or answer.lower() == 'a echo' or answer.lower(
        ) == 'alexa':
            cond = 'y'
        elif answer.lower() == 'n':
            return

    sleep(0.5)
    print('''
\u001b[33;1mThe Elf queen Vecna looks warily at you.

If you want Vecna, The Superior Elf to support you in the war,
Then you have to reduce your attack by 5 points.

Press 'y' to agree with the proposal.
Press 'n' to continue with your travels.\u001b[0m
        ''')
    if atkrange[0] >= 5:
        a = input('')
        if a.lower() == 'y':

            atkrange[0] -= 5
            atkrange[1] -= 5
            Kingdoms.remove('elf kingdom')
            alliance.append('elf kingdom')
            ability = True
            abilities.append("Blast enemy with Thor's Thunderbolt")
            print('''
Your updated attribute values are:
\u001b[31mAttack: {}\u001b[0m
\u001b[34mDefense: {}\u001b[0m
\u001b[32mHealth: {}\u001b[0m'''.format(atkrange, defrange, hp))
            print('''
\nYou have gained the support of the Elf kingdom.
Vecna, the Superior Elf also grants you the ability to:
          'Blast enemy with a thunderbolt'

This ability will cause a threefold increase in damage. It is a cooldown ability.  
          ''')

        else:
            print(
                "Aren't you a silly traveller ? Coming upto to our Queen Vecna and still refusing her help ?"
            )
        return
    else:
        print(
            "You don't have enough attack points to accept this proposal. Come back later."
        )
        return


def orckingdom():
    os.system('clear')
    global Kingdoms
    global hp
    global atkrange
    print('''You are greeted by loud war cries. 

A burly orc grabs you by the collar - 

'You puny mortal, state your business'

\u001b[31m 1. I'm here to meet your Chieftain Xenoria 
2. Eh- I'm sorry I'll leave 
3. Your breath stinks you big oaf\u001b[0m \n''')

    cond = int(input())
    if cond == 2:
        print("Don't disturb us ever again")
        return
    elif cond == 1:
        print('Very well Foreigner')
    elif cond == 3:
        hp -= 2
        print("The orc has done \u001b[31m 2 \u001b[0m points of damage ")
        print("I'll take you to our Chieftain to suffer punishment for this")

    else:
        print('Invalid input. Try again')
        orckingdom()

    print('''
\u001b[33;1mThe Chieftain Xenoria looks warily at you.

If you want Xenoria, The Supreme Warrior of the Orc Tribe to support you in the war,
Then you have to reduce your health by 2 points.

Press 'y' to agree with the proposal.
Press 'n' to continue with your travels.\u001b[0m
        ''')
    a = input('')
    if a.lower() == 'y':
        hp -= 2
        Kingdoms.remove('orc kingdom')
        alliance.append('orc kingdom')
        atkrange[0] *= 3
        atkrange[1] *= 3
        g1 = open("inventory.txt", "a")
        g1.write('\nIvan the Terrible')
        g1.close()
        print('''
Your updated attribute values are:
\u001b[31mAttack: {}\u001b[0m
\u001b[34mDefense: {}\u001b[0m
\u001b[32mHealth: {}\u001b[0m'''.format(atkrange, defrange, hp))
        print('''
\nYou have gained the support of the Orc Tribe.
Xenoria, The Supreme Warrior of the Orc Tribe also hands you the weapon:
          'Ivan the Terrible'

The weapon increases your attack levels by three times. 
          ''')
    else:
        print(
            "Aren't you a silly traveller ? Coming upto to our Queen Vecna and still refusing her help ?"
        )
    return


def wizardingabode():
    os.system('clear')
    global Kingdoms
    global level
    print('''A fog of gloom welcomes you. \n\n\n
You hear someone whisper the words 'Non-magical' as a gust of ominous wind knocks you down.\n'''
          )
    sleep(1)
    print(
        '''\n\n You open your eyes to see the Head of the Wizarding abode, Voldemort staring at you

I know why you are here. If you wish to receive our help,

\u001b[31m Prove your worth by fighting against this monster\u001b[0m\n\n''')
    level += 2
    fight()
    level -= 2
    Kingdoms.remove('wizarding abode')
    alliance.append('wizarding abode')
    print('''\u001b[33m
\nYou have gained the support of the Wizarding Abode.
Voldemort, The Head Mage hands you the 3 Greater Health Potions.\u001b[0m
          ''')
    inv.append("Greater Health Potion")
    inv.append("Greater Health Potion")
    inv.append("Greater Health Potion")
    return


def humansettlement():
    os.system('clear')
    global Kingdoms
    global goldgained
    global ability
    global abilities
    print('''Two human guards greet you at the doors of the human settlement.
To enter, first answer the riddle\n''')

    cond = 'n'
    while cond == 'n':
        print(
            "\u001b[31mIt has a golden head. It has a golden tail. It has no body.\u001b[0m\n\nIf you want to give up, type 'n'"
        )
        answer = input()
        if answer.lower() == 'golden coin' or answer.lower(
        ) == 'coin' or answer.lower() == 'gold coin':
            cond = 'y'
        elif answer.lower() == 'n':
            return

    print('''
\u001b[33;1mThe Human King, Kaz Brekker looks warily at you.

If you want Kaz, the Chief Warrior of the Human Settlement to support you in the war,
Then you have to pay up 20 gold bars.

Press 'y' to agree with the proposal.
Press 'n' to continue with your travels.\u001b[0m
        ''')
    a = input('')
    if a.lower() == 'y':
        if goldgained < 20:
            print(
                "You don't have enough money to buy my support, go back fool ")
            return ()

        print('\u001b[33;1mGold bars remaining=\u001b[0m', goldgained)
        Kingdoms.remove('human settlement')
        alliance.append('human settlement')
        ability = True
        abilities.append('Guns blazing')
        print('''
\nYou have gained the support of the Human kingdom.
Kaz, the Chief Warrior of the Human Settlement also grants you the ability to:
          'Guns blazing'

The ability will increase your attack by 10 levels for a moment. It is a cooldown ability.  
          ''')
    else:
        print(
            "Aren't you a silly traveller ? Coming upto to our Chief and still refusing his help ?"
        )
    return


def centaurforest():
    os.system('clear')
    global kvisit
    global Kingdom_visit
    global goldgained
    print(
        '''As you venture into the centaur forest, you start to hear loud party noises.\n
A grand party of the centaurs is happening. With loud rock music being played on the speakers, you can see endless fountains of wine and centaur-women draped on the centaurs.

In the middle of the crowd, you spot the Centaur Lord, Chiron. You approach him.\n'''
    )

    print(
        '''\n\u001b[33;1mChiron listens to your proposition but as a form of test, lays down three chalices in front of you . 
    What do you do ?
    
    1. Drink the chalice which has a dark and glittering liquid, resembling some sort of wine
    2. Drink the chalice containing a pale yellowish liquid
    3. Drink the chalice with a mysterious colour-changing yet mesmerising potion 
    4. Chug all three and grin sheepishly at Chiron\u001b[0m
    ''')
    choice = int(input())

    if choice == 1:
        print(
            'The potion instaneously makes you drunk. You cannot comprehend anything happening around you and need to be taken out of the forest '
        )
        return
    elif choice == 2:
        print(
            'You immediately start throwing up and have to be taken out of the forest'
        )
        return
    elif choice == 3:
        print(
            'You suddenly feel light-headed and feel yourself starting to float up, up and beyond. \nSee you next time bud <3'
        )
        return
    else:
        print('Chiron is very pleased with your decision.')
        Kingdoms.remove('centaur forest')
        alliance.append('centaur forest')
        g1 = open("inventory.txt", "a")
        for i in range(0, 3):
            g1.write('\nGreater Health Potion')
        g1.close()
        print('''
\nYou have gained the support of the Centaurs.
Chiron, the Centaur Leader hands you 3 Greater Health potions.

They have been added to your inventory.
          ''')
    return


def questpt1():
    part2 = "a"
    while part2:
        part2 = f1.readline()

        if "FIGHT" in part2:
            b = part2.partition("FIGHT")
            print(b[0])
            fight()
            print(b[2])
        else:
            print(part2)
    f1.close()
    return


def questpt2():
    global hp
    global kvisit
    global Kingdom_visit
    global visitedk
    global alliance
    Continue = input('\nPress enter to continue: ')
    while Continue != '':
        Continue = input('\nPress enter to continue: ')
    os.system('clear')
    f2 = open("story(quest1).txt", "r")
    part4 = f2.readline()
    print(part4)
    part4 = f2.readline()
    print(part4)
    sleep(1)
    part4 = f2.readline()
    print(part4, end=' ')
    print('Apart from your own kingdom,', ownkingdom, 'and Dragon Spine')
    nvariable = 1
    for i in Kingdoms:
        Kingdom_visit[nvariable] = i
        nvariable += 1
    mvariable = 1
    for i in Kingdoms:
        print(mvariable, i.title(), end="\n")
        mvariable += 1

    print('\nKingdoms aligned with:')
    if len(alliance) == 0:
        print('No kingdoms till now')
    else:
        for i in alliance:
            print(i.title())

    print(
        "\n\u001b[33;1mPress the number of the kingdom which you would like to visit: \u001b[0m"
    )
    while True:
        try:
            kvisit = int(input())
        except ValueError:
            print("Invalid input. Try again")
            continue
        else:
            break
    print("It will take you 7 rolls of dice to reach", Kingdom_visit[kvisit])
    dicecount = 0
    while dicecount <= 6:
        if hp <= 0:
            hp = 30
            questpt2()
            break
        else:
            q = "d"
            while q != 's':
                print('''\nType "s" to visit shop
Type "i" to open inventory
Type "SPIN" to continue on your journey''')
                p = str(input(""))
                if p.lower() == "s":
                    shop()
                elif p.lower() == "i":
                    inventory()
                elif p.lower() == 'spin':
                    q = "s"

                    dice()
                    dicecount += 1
                else:
                    print("invalid input")
    return


def append():
    global name
    f1 = open('username.csv', 'a')
    global atkrange
    global defrange
    global goldgained
    global monencountered
    atklevel = atkrange[0]
    deflevel = defrange[0]
    gold = goldgained
    w_obj = csv.writer(f1)
    w_obj.writerow([name, atklevel, deflevel, gold, monencountered])
    f1.close()


def update():
    list = []
    global name
    global atkrange
    global defrange
    global goldgained
    global monencountered
    f1 = open('username.csv', 'r')
    r_obj = csv.reader(f1, delimiter=',')
    for row in r_obj:
        if row[0] != name:
            list.append(row)
        elif row[0] == name:
            print('Previous attempt\n', row)
            row[0] = name.capitalize()
            row[1] = atkrange[0]
            row[2] = defrange[0]
            row[3] = goldgained
            row[4] = monencountered
            print('Updated to:\n', row)
            list.append(row)
    f1.close()
    file = open('username.csv', 'w', newline='')
    w_obj = csv.writer(file)
    w_obj.writerows(list)


def leaderboard():
    list = ['NAME', 'ATTACK', 'DEFENCE', 'GOLD', 'NUMBER OF MOSTERS']
    lb = []
    lb.append(list)
    file = open('username.csv', 'r')
    robj = csv.reader(file, delimiter=',')
    for row in robj:
        lb.append(row)
    for i in lb:
        print(i[0], i[1], i[2], i[3], i[4], sep='  :  ')


def check(name):
    exist = 0
    namelist = []
    file = open('username.csv', 'r')
    r_obj = csv.reader(file, delimiter=',')
    for row in r_obj:
        namelist.append(row[0])
    file.close()
    for i in namelist:
        if i == name.capitalize():
            exist = 1
    if exist == 0:
        append()
    else:
        update()


def mainbossfight():
    global monsterhp
    global pts
    global atk
    global defense
    global hp
    global baseatk1
    global powerup1
    global cooldown
    global mname
    global mdamage
    mname = "dragon"
    print(
        "\u001b[1m\u001b[33mIt is time to begin the final battle. Good luck\u001b[0m\n"
    )
    monsterhp = 500
    mdamage = [10, 15]

    def phase1():
        while monsterhp > 260 and hp > 0:
            gf()
            if monsterhp > 0 and hp > 0:
                print("\n\u001b[36mthe", mname, "has", monsterhp,
                      "health points remaining\u001b[0m")
                print()
                monster()

    def phase2():
        atkrange[0] *= 0.5
        atkrange[1] *= 0.5
        while monsterhp > 200 and hp > 0:
            gf()
            if monsterhp > 0 and hp > 0:
                print("\n\u001b[36mthe", mname, "has", monsterhp,
                      "health points remaining\u001b[0m")
                print()
                monster()
        atkrange[0] *= 2
        atkrange[1] *= 2

    def phase3():
        while monsterhp >= 0 and hp > 0:

            def choose():
                try:
                    print('''What do you choose to do?
        press 1 to''', baseatk1, '''
        press 2 to check inventory ''')
                    a = int(input())
                    if a == 1:
                        baseatk()
                    elif a == 2:
                        inventory()
                    else:
                        print("invalid input")
                        choose()
                except:
                    print("Invalid Input. Try again...")

            def baseatk():
                global monsterhp
                global cooldown
                damage = random.randint(atkrange[0], atkrange[1])
                print("you have done \u001b[31m", damage,
                      "\u001b[0m points of damage with your base attack")
                monsterhp -= damage
                cooldown = 'F'

            choose()
            if monsterhp > 0 and hp > 0:
                print("the", mname, "has", monsterhp,
                      "health points remaining")
                print("you have", hp, "health points remaining")
                print()
                monster()
            elif hp <= 0:
                print("you have been defeated by the", mname)
                print("Game over. You have lost.")
                print()
                break

    while monsterhp > 0 and hp > 0:
        if monsterhp > 260 and monsterhp <= 500:
            phase1()
        elif monsterhp <= 260 and monsterhp > 200:
            print(
                "\n\u001b[31mThe dragon realizes that he is weakened, so he puts up his shield\u001b[0m"
            )
            phase2()
            print("\n\u001b[31mThe shield has finally been broken!\u001b[0m")
        elif monsterhp <= 200 and monsterhp > 0:
            print()
            print(
                "\n\u001b[31mThe dragon roars in anger, and gathers all its magic and releases it upon you."
            )
            print("\nYou cannot use your powerup anymore!\u001b[0m\n")
            phase3()

    if monsterhp <= 0:
        print("\n\n\n\u001b[31;1mYou have defeated the Dragon !!\u001b[0m")
    elif hp <= 0:
        print("\n\nYou have been defeated by the", mname)
        print("Game over. Try again later...")

    print()
    print()


###########
##Start of actual code
###########
cp1 = 'False'
cp2 = 'False'
cp3 = 'False'

f1 = open("story(intro).txt", "r")

print('\u001b[35m \u001b[47;1mWelcome to Incursion Realms!!! \u001b[0m \n')
part1 = f1.readline()
print(part1)
charbuild()
print("\u001b[33;1mYour chosen class is: ", class1, '\u001b[0m')
print(
    '\n\u001b[33;1mYour base attack is', baseatk1, '\nand special attack is',
    powerup1,
    '.It does more damage than your base attack.The special attack goes on cooldown for 1 turn after using it.\u001b[0m'
)
print("\nAs a beginner, you have been gifted 5 points to level up your stats")
pts += 5
statslevelup()

Continue = input('\nPress enter to continue: ')
while Continue != '':
    Continue = input('\nPress enter to continue: ')
os.system('clear')

questpt1()

##Check point 1 code
if hp <= 0:
    cp1 = 'True'
while cp1 == 'True':
    hp = 30
    print("You have lost the battle. Starting from latest saved progress...")
    questpt1()

while len(alliance) < 3:
    questpt2()
    ##Check point 2 code
    if hp <= 0:
        cp2 = 'True'
    while cp2 == 'True':
        hp = 30
        print(
            "You have lost the battle. Starting from latest saved progress...")
        questpt2()

    print()

    if Kingdom_visit[kvisit] == 'elf kingdom':
        elfkingdom()
    elif Kingdom_visit[kvisit] == 'orc kingdom':
        orckingdom()
    elif Kingdom_visit[kvisit] == 'wizarding abode':
        wizardingabode()
    elif Kingdom_visit[kvisit] == 'human settlement':
        humansettlement()
    elif Kingdom_visit[kvisit] == 'centaur forest':
        centaurforest()

Continue = input(
    '\n\u001b[31;1mYou can now face the Evil Dragon. Press enter to continue: '
)
while Continue != '':
    Continue = input('\nPress enter to continue: \u001b[0m')
os.system('clear')

mainbossfight()
if hp <= 0:
    cp3 = 'True'

Continue = input('\nPress enter to continue: ')
while Continue != '':
    Continue = input('\nPress enter to continue: ')
os.system('clear')

print(
    "Game has ended. Thank you for playing. These are your achievements throughout the game.\n\n"
)
name = input('Enter your name to save your progress:')
check(name)
leaderboard()
