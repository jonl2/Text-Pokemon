#TO DO LIST
# Pokemon capture mech, battle system(on this right now), item buying system, level system/exp gain system, Pokedex system.

timetick = False
times = 7
endg = 0
condi= 0
room = "Clearing"
drc = "Clearing"
cside = True
import time
import random


#Functions
    
def Move(action,condi,room): #Room function pt1 ( I was too lazy to do a matrix for the code... :D )
    if room == "Clearing": #Each room has individual name.
        if action == "north" or action == 'North': #Each if statement shows whether the route is availible or not.
            room = 3 #For this one it is yes.
        if action == "south" or action == "South":
            print("You cannot go that way") #This one is no.    
        if action == "east" or action == "East":
            print("You cannot go that way") #This on is no too.
        if action == "West" or action == "west":
            print("You cannot go that way") #So is this one. The pattern continues for all rooms.
    if room == "rival_house":
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            print("You cannot go that way")
        if action == "east" or action == "East":
            room = 3
        if action == "West" or action == "west":
            print("You cannot go that way")
    if room == "pallet_center":
        if action == "north" or action == "North":
            room = 5
        if action == "south" or action == "South":
            room = 1
        if action == "east" or action == "East":
            room = 4
        if action == "West" or action == "west":
            room = 2
    if room == "pallet_lab":
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            print("You cannot go that way")
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            room = 3
    if room == "pallet_clearing":
        if action == "north" or action == "North":
            room = 7
        if action == "south" or action == "South":
            room = 3
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            print("You cannot go that way")
    if room == "tall_grass1":
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            print("You cannot go that way")
        if action == "east" or action == "East":
            room = 7
        if action == "West" or action == "west":
            print('You cannot go that way')
    if room == "route1_ent":
        if action == "north" or action == "North":
            room = 9
        if action == "south" or action == "South":
            room = 5
        if action == "east" or action == "East":
            room = 8
        if action == "West" or action == "west":
            room = 6
    if room == "tall_grass2":
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            print("You cannot go that way")
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            room = 7
    if room == "tall_grass3":
        if action == "north" or action == "North":
            room = 11
        if action == "south" or action == "South":
            room = 7
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            print("You cannot go that way")
    if room == "tall_grass4":
        if action == "north" or action == "North":
            room = 12
        if action == "south" or action == "South":
            print("You cannot go that way")
        if action == "east" or action == "East":
            room = 11
        if action == "West" or action == "west":
            print("You cannot go that way")
    if room == "trainer1":
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            room = 9
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            room = 10
    if room == "tall_grass5":
        if action == "north" or action == "North":
            room = 14
        if action == "south" or action == "South":
            room = 10
        if action == "east" or action == "East":
            room = 13
        if action == "West" or action == "west":
            print("You cannot go that way")
    if room == "tall_grass6":
        if action == "north" or action == "North":
            room = 15
        if action == "south" or action == "South":
            print("You cannot go that way")
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            room = 12
    if room == "tall_grass7":
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            room = 12
        if action == "east" or action == "East":
            room = 15
        if action == "West" or action == "west":
            print('You cannot go that way')
    if room == "trainer2":
        if action == "north" or action == "North":
            room = 16
        if action == "south" or action == "South":
            room = 13
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            room = 14
    if room == "v_enter":
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            room = 15
        if action == "east" or action == "East":
            room = 17
        if action == "West" or action == "west":
            print("You cannot go that way")
    if room == "v_house":
        if action == "north" or action == "North":
            room = 20
        if action == "south" or action == "South":
            print("You cannot go that way")
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            room = 16
    if room == "v_mart":
        if action == "north" or action == "North":
            room = 21
        if action == "south" or action == "South":
            print("You cannot go that way")
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            print("You cannot go that way")
    if room == "v_gym":
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            print("You cannot go that way")
        if action == "east" or action == "East":
            room = 20
        if action == "West" or action == "west":
            print("You cannot go that way")
    if room == "v_center":
        if action == "north" or action == "North":
            room = 22
        if action == "south" or action == "South":
            room = 17
        if action == "east" or action == "East":
            room = 21
        if action == "West" or action == "west":
            room = 19
    if room == 'v_pcenter':
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            room = 18
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            room = 20
    if room == 'v_exit':
        if action == "north" or action == "North":
            print("You cannot go that way")
        if action == "south" or action == "South":
            room = 20
        if action == "east" or action == "East":
            print("You cannot go that way")
        if action == "West" or action == "west":
            print("You cannot go that way")
    return room
    

    
def Room(room,drc): #Room function pt2
    global cside 
    global timetick
    if drc != room:
        timetick = True
        
        if room == 1:
            room = "Clearing"
            print('Clearing')
            cside = False
        if room == 2:
            room = "rival_house"
            print("Rival's home")
            cside = False
        if room == 3:
            room = "pallet_center"
            print('Pallet Town Central Square')
            cside = True
        if room == 4 :
            room = "pallet_lab"
            print("Professor Oak's Lab")
            cside = False
        if room == 5 :
            room = "pallet_clearing"
            print('Pallet Town Clearing')
            cside = True
        if room == 6 :
            room = "tall_grass1"
            print('Tall Grass')
            cside = True
        if room == 7 :
            room = "route1_ent"
            print('Route 1 entrance/exit')
            cside = True
        if room == 8 :
            room = "tall_grass2"
            print('Tall Grass')
            cside = True
        if room == 9 :
            room = "tall_grass3"
            print('Tall Grass')
            cside = True
        if room == 10 :
            room = "tall_grass4"
            print('Tall Grass')
            cside = True
        if room == 11 :
            room = "trainer1"
            print('Route 1 open area')
            cside = True
        if room == 12 :
            room = "tall_grass5"
            print('Tall Grass')
            cside = True
        if room == 13 :
            room = "tall_grass6"
            print('Tall Grass')
            cside = True
        if room == 14 :
            room = "tall_grass7"
            print('Tall Grass')
            cside = True
        if room == 15 :
            room = "trainer2"
            print('Route 1 entance/exit')
            cside = True
        if room == 16 :
            room = "v_enter"
            print('Viridian Entrance/exit')
            cside = True
        if room == 17 :
            room = "v_house"
            print('Viridian Homes')
            cside = False
        if room == 18 :
            room = "v_mart"
            print('Viridian Pokémon Mart')
            cside = False
        if room == 19 :
            room = "v_gym"
            print('Viridian Gym')
            cside = False
        if room == 20 :
            room = "v_center"
            print('Viridian Central Square')
            cside = True
        if room == 21:
            room = 'v_pcenter'
            print('Viridian Pokémon Center')
            cside = False
        if room == 22:
            room = 'v_exit'
            print('Viridian entrance/exit')
            cside = True
    return room
        
def Time(time,cside): #Timekeeper function
    global timetick
    if timetick == True:
        time = time + 1
    
    if time == 24:
        time =0
    if time == 19 and cside == True:
        print("It's getting dark. You can see the sun setting.\n")
    if time == 6 and cside == True:
        print("It's getting brighter. You can see the sun rising.\n")
    return time

def CTime(time,action,cside): #Shows current time to user when requested.
    from random import randint
    if time == 0:
        time = 25
    Ttime = time
    Atime = "AM"
    inside="You can't see the sky, but you feel like it is around"
    outsideD ="You look at the sun, it appears to be around"
    outsideN = "You look at the night sky."
    if action == "check time" or action == "Check time":
        if time >= 12:
            Atime = "PM"
            if time == 13:
                Ttime = 1
            if time == 14:
                Ttime = 2
            if time == 15:
                Ttime = 3
            if time == 16:
                Ttime = 4
            if time == 17:
                Ttime = 5
            if time == 18:
                Ttime = 6
            if time == 19:
                Ttime = 7
            if time == 20:
                Ttime = 8
            if time == 21:
                Ttime = 9
            if time == 22:
                Ttime = 10
            if time == 23:
                Ttime = 11
            if time == 25:
                Ttime = 12
                Atime = "AM"
                time = 0
        LC=randint(1,5)
        lc="It feels like it is around "
       
            
        if cside == True and time >= 6 and time <= 19:
            print(outsideD,Ttime,Atime)
        if cside == True and time >= 20:
            
            if LC == 1:
                lc="You see a shooting star! It appears to be around "
            print(outsideN,lc,Ttime,Atime)
        if cside == True and time >= 0 and time <= 5:
            if LC == 1:
                lc="You see a shooting star! It appears to be around "
            print(outsideN,lc,Ttime,Atime)
        if cside == False:
            print(inside,Ttime,Atime)

def Help(): #Generates possible commands to input for user.
        print('To move around, use commands "north" "west" "east" "south" to move around rooms.')
        print('To do actions in specific buildings, use "talk" "buy" "challenge" "search" \nrespective to where you are.')

def ps(str): #slow typing for single strs.
    for letter in str:
        print (letter, end='')
        time.sleep(delay)

def pt(str1,str2,str3):
    for letter in str1:
        print(letter, end='')
        time.sleep(delay)
    for letter1 in str2:
        print(letter1, end='')
        time.sleep(delay)
    for letter2 in str3:
        print(letter2, end='')
        time.sleep(delay)
        
def pstatgen(pkmn_name,lvl,ID): #This generates the stats necessary for the game.
    import random
    global pokebelt
    atk = random.randint(10,15)
    Def = random.randint(10,15)
    spd = random.randint(10,15)
    hp = random.randint(50,60)
    exp = 0
    string = [pkmn_name,atk,Def,spd,hp,exp,lvl,ID]
    return string

def pnaming(pkm1): #For nicknames
    import time
    pt('Congratulations on choosing ',pkm1,' as your new partner! \nWill you give your partner a name?')
    pkm1 = input('\nEnter name here: ')
    pt('Congratulations on obtaining ', pkm1,'!\n')
    return pkm1

def pstatgen(pkmn_name,lvl,ID): #This generates the stats necessary for the game.
    import random
    global pokebelt
    atk = random.randint(10,15)
    Def = random.randint(10,15)
    spd = random.randint(10,15)
    hp = random.randint(50,60)
    exp = 0
    string = (pkmn_name,atk,Def,spd,hp,exp,lvl,ID)
    return string

#Classes
class Create_Pokemon(object):
    Type = 'none'
    def __init__(self,name,attack,defense,speed,HP,exp,level,ID):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.HP = HP
        self.exp = exp
        self.level = level
        self.ID = ID
    def Fire_type(self):
        self.Type = 'fire'
    def Water_type(self):
        self.Type = 'water'
    def Grass_type(self):
        self.Type = 'grass'

def var1(a,c): #This is to individually take the variables in tuples that were return generated
    b = a[c]
    return b

def genwildpkmn(name,lvl):
    stats = pstatgen(name,lvl,'none')
    pkmn = Create_Pokemon(stats[0],stats[1],stats[2],stats[3],stats[4],stats[5],stats[6],stats[7])
    return pkmn

def search(action,room): #Wild pokemon search
    import random
    chance = random.randint(1,100)
    if action == 'search':
        if room == 'tall_grass1' or 'tall_grass2' or 'tall_grass3' or 'tall_grass4' or 'tall_grass5' or 'tall_grass6' or 'tall_grass7':
            if chance == 1:
                ps('A wild Articuno(GET HER) appears!')
                wldpkmn = 'Articuno'
            if chance in range(2,50):
                ps('A wild Pidgey appears!')
                wldpkmn = 'Pidgey'
            if chance in range(51,100):
                ps('A wild Rattata appears!')
                wldpkmn = 'Rattata'
            return wldpkmn
        else:
            ps('You cannont search for pokémon here!')

#Battle function
def battle_intro(): #Battle help/intro function
    import time
    global pokebelt
    global pkmn1moves
    time.sleep(1)
    ps('\nA Wild Pidgey appears!')
    time.sleep(1)
    ps('\nWhen you start, the first pokemon in your party comes out.')
    time.sleep(1)
    pkmn1 = pokebelt.pop(0)
    pokebelt.insert(0,pkmn1)
    pt('\nCome out, ',pkmn1.name,'! ')
    pkmn2 = genwildpkmn('Pidgey',5)
    pkmn2moves = ['Scratch']
    time.sleep(1)
    ps('\nWhat will you do?')
    time.sleep(1)
    ps('\nNow you can choose to attack, use bag, run, or switch pokémon.')
    time.sleep(2)
    print('\n:Attack')
    time.sleep(1)
    ps('\nWhich move?\nNow you can choose which move to use.')
    print('Your moves:',pkmn1moves,'.')
    time.sleep(1)
    move1 = pkmn1moves.pop(0)
    pkmn1moves.insert(0,move1)
    print('Use ',move1,' ',pkmn1.name,'!')
    tup = damagepI(move1,pkmn2,pkmn1moves)
    hp = tup[0]
    dmg = tup[1]
    time.sleep(2)
    print('Pidgey has taken ',dmg,"damage, Pidgey's HP is now at:",' ',hp,'.')
    ps("\nThe battle will continue until the opponent's HP hits '0'.")
    time.sleep(1)
    ps('\nCongratulations on finishing the battle tutorial! Now go out and battle!\n')

def damagepI(move,pkmn2,pkmn1moves):
    global pokebelt
    global movesindex
    global movesdmg
    pkmn1 = pokebelt.pop(0)
    pokebelt.insert(0,pkmn1)
    p1name = pkmn1.name
    if move in pkmn1moves:
        cmd = movesindex.index(move)
        atkdmg = movesdmg.pop(cmd)
        movesdmg.insert(cmd,atkdmg)
    dmg = int((pkmn1.attack/pkmn1.defense)*atkdmg)
    hp = pkmn2.HP - dmg
    return (hp,dmg)

def battle(pkmn2):
    import random
    import time
    global pokebelt
    global movesindex
    global movesdmg
    global wildmoves
    global pkmn1moves
    global bag
    a = pkmn1moves
    pkmn2name = pkmn2.pop(0)
    pkmn2.insert(0,pkmn2name)
    pt('A wild ',pkmn2name,' appeared!')
    pkmn1 = pokebelt.pop(0)
    pokebelt.insert(0,pkmn1)
    p1name = pkmn1.pop(0)
    pkmn1.insert(0,p1name)
    pt('\nCome out, ',p1name,'! ')
    time.sleep(2)
    ps('\nWhat will you do?')
    HP1 = HP = 100
    while HP1 != 0 or HP != 0:  
        ps('ATTACK, BAG, RUN, SWITCH')
        action = input(': ')
        if action == 'attack' or 'Attack' or 'ATTACK':  #pkmn_name,atk,Def,spd,hp,exp,lvl,ID
            print(a)
            move1 = input(': ')
            atk1 = pkmn1.pop(1)
            pkmn1.insert(1,atk1)
            HP1 = pkmn1.pop(4)
            if move1 in a:
                print('Use ',move1,' ',p1name,'!')
                cmd = movesindex.index(move1)
                atkdmg = movesdmg.pop(cmd)
                movesdmg.insert(cmd,atk1)
                def1 = pkmn2.pop(2)
                pkmn2.insert(2,def1)
                dmg = int((atk1/def1)*atkdmg)
                hp = HP - dmg
                pkmn2.pop(4)
                pkmn2.insert(4,hp)
                print(pkmn2name,' has taken ',dmg,' amount of damage. Pidgey is now at: ',hp,'.')
                move = random.randint(1,100)
                if pkmn2name == 'Pidgey' or 'Rattata':
                    if move in range(1,50):
                        cmd = 0
                    if move in range(51,100):
                        cmd = 1
                move = wildmoves.pop(cmd)
                wildmoves.insert(cmd,move)
                atkdmg = movesdmg.pop(cmd)
                movesdmg.insert(cmd,atkdmg)
                print(pkmn2name,' used ',move,'!')
                def1 = pkmn1.pop(2)
                pkmn1.insert(2,def1)
                atk1 = pkmn2.pop(1)
                pkmn2.insert(1,atk1)
                dmg = int((atk1/def1)*atkdmg)
                hp = HP - dmg
                pkmn1.insert(4,hp)
                print(p1name,' has taken ',dmg,' amount of damage.',p1name,' is now at: ',hp,'.')
    print('Hi')
            
            
#Events
        

def wildpkmn(action,room,lvl):
    if room == 'tall_grass1' or room == 'tall_grass2' or room == 'tall_grass3' or room == 'tall_grass4' or room == 'tall_grass5' or room == 'tall_grass6' or room == 'tall_grass7':
        action = 'search'
        if room == 'tall_grass1':
            lvl = 5
        if room == 'tall_grass2':
            lvl = 7
        if room == 'tall_grass3':
            lvl = 8
        if room == 'tall_grass4':
            lvl = 10
        if room == 'tall_grass5':
            lvl = 12
        if room == 'tall_grass6':
            lvl = 14
        if room == 'tall_grass7':
            lvl = 15
        pkmn2name = search(action,room)
        pkmn2 = genwildpkmn(pkmn2name,lvl)
        battle(pkmn2)
    

def event_1(room,pokebelt): #Prof Oak Event.
    import time
    import random
    if room == 'pallet_center':
        ps('You notice Professor Oak!\n') #Lots of ingame text.
        time.sleep(1)
        ps('He comes up to you.\n')
        time.sleep(1)
        pt('How are you doing, ',name,'? I have the pokemon you were waiting for. \nCome with me!\n')
        time.sleep(1)
        ps('You eagerly comply and go with him to his lab.\n')
        room = 'pallet_lab'
        ps('OK, ')
        ps(name)
        ps('. Choose the pokemon of your choice!\n')
        ps('There are three pokemon to choose from:\n')
        ps('CHARMANDER - the blaze pokemon. A strong fire pokemon.\n')
        ps('SQUIRTLE - the turtle pokemon. A strong water pokemon.\n')
        ps('BULBASAUR - the vine pokemon. A strong grass pokemon.\n')
        ps('Choose one: C for Charmander, S for Squirtle, and B for Bulbasaur.\n')
        choice = input() #Choose starter pkmn.
        if choice == 'C':
            pkm1 = 'Charmander'
            ID = 4
        if choice == 'S':
            pkm1 = 'Squirtle'
            ID = 7
        if choice == 'B':
            pkm1 = 'Bulbasaur'
            ID = 1
        lvl = 5
        pkm1 = pnaming(pkm1)
        stats = pstatgen(pkm1,lvl,ID)
        pkm1 = Create_Pokemon(stats[0],stats[1],stats[2],stats[3],stats[4],stats[5],stats[6],stats[7])
        pokebelt.append(pkm1)
        print("\nYou are now in Professor Oak's Lab.\n")
        ps('To complete the game, navigate the route, find the next city,\n and defeat the gym leader that is way stronger than you! :D\n')
        return (room,pokebelt)

def event_2(room): #Intro to battling.
    import time
    global ec
    if room == 'pallet_clearing':
        ps('You notice an old man!\n')
        time.sleep(1)
        ps('Who comes here? \nIf you are trying to go to the route, it is crawling with pokémon! \nI will teach you how to battle.')
        battle_intro()
        ec = ec + 1
    return ec

#Global Variables
        
ec = 0
delay = 0
choice = 0
b = 0
#Lists

pokebelt = [] #This is party pokemon and stats for em.
pkmn1moves = ['Scratch','Tackle']
wildmoves = ['Scratch','Tackle']
movesindex = ['Scratch','Takle']
movesdmg = [15,15]
#Pokeball, Greatball, Ultraball, MasterBall
bag = [[5,0,0,0],[]]

#Script

endg = 1
ps('Pokemon RED! text version 1.0. type START to begin.\n')
start = input()
if start == 'START':
    ps('Welcome to the world of pokemon! \n')
    time.sleep(1)
    ps('Tell me a few things about yourself. What is your name?\n')
    name = input('Type your name here: ')# Enter name here
    time.sleep(1)
    ps('What is the time?\n') #Time set here
    times = int(input('Enter time here (round to nearest hour integer (24hr)): '))
    time.sleep(1)
    ps("Let the adventure begin!\n")
    Help()
    ps('Type "north" to begin.\n')
    endg = 0
while endg == 0: #Infinite while for game to run forever! XD
    drc = room
    timetick = False
    action=input(':') #All commands are from action
    room = Move(action,condi,room)
    room = Room(room,drc)
    times = Time(times,cside)
    CTime(times,action,cside)
    wildpkmn(action,room,b)
    if action == 'help' or action == 'Help':
        Help()
    if ec == 0:
        ec = ec + 1
        a = event_1(room,pokebelt)
        room = a[0]
        pokebelt = a[1]
    if ec == 1:
        ec = event_2(room)

    
