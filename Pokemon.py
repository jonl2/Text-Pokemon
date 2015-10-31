#TO DO LIST
# Pokemon capture mech, item buying system, new moves (super effective/not if time permits)
'''Replace this following code with the triple #s and follow instructions there:
    pkmn1.exp = pkmn1.exp + expgain(lvl)
    '''
timetick = False
times = 7
endg = 0
condi= 0
room = "Clearing"
drc = "Clearing"
cside = True
import time
import random




#Room move Functions -------------------------------------------------------------------------------------------------------
    
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

#Time functions -----------------------------------------------------------------------------------------------------------       
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


 #Pokemon Stat Creation ----------------------------------------------------------------------------------------------------       

def pnaming(pkm1): #For nicknames
    import time
    pt('Congratulations on choosing ',pkm1,' as your new partner! \nWill you give your partner a name?')
    pkm1 = input('\nEnter name here: ')
    pt('Congratulations on obtaining ', pkm1,'!\n')
    return pkm1

def pstatgen(pkmn_name,lvl,ID): #This generates the stats necessary for the game.
    import random
    global pokebelt
    a = lvl * 2
    b = a + 2
    c = lvl * 10
    d = c + 2
    atk = random.randint(a,b)
    Def = random.randint(a,b)
    spd = random.randint(a,b)
    hp = random.randint(c,d)
    exp = 0
    string = (pkmn_name,atk,Def,spd,hp,exp,lvl,ID)
    return string

#Pokemon Class
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
        self.orHP = HP
    def Fire_type(self):
        self.Type = 'fire'
    def Water_type(self):
        self.Type = 'water'
    def Grass_type(self):
        self.Type = 'grass'
    def levelup(self):
        self.attack = self.attack + 3
        self.defense = self.defense + 3
        self.speed = self.speed + 2
        self.HP = self.HP + 3
        self.orHP = self.orHP + 3
    def evolup(self,ID):
        self.attack = self.attack + 15
        self.defense = self.defense + 15
        self.speed = self.speed + 10
        self.orHP = self.orHP + 50
        self.HP = self.HP + 3
        self.ID = ID
    def Oneup(self,pkmn):
        global evol
        if pkmn.level == 16:
            pkmn.ID = pkmn.ID + 1
            newpkmn = pkmnID.pop(pkmn.ID)
            pkmnID.insert(pkmn.ID,newpkmn)
            ps('What? \n%s is evolving!\n'%(pkmn.name))
            timesleep()
            ps('Congratulations! Your %s has evolved into %s'%(pkmn.name,newpkmn))
            self.evolup(pkmn.ID)
        if pkmn.level == 36:
            pkmn.ID = pkmn.ID + 1
            newpkmn = pkmnID.pop(pkmn.ID)
            pkmnID.insert(pkmn.ID,newpkmn)
            ps('What? \n%s is evolving!\n'%(pkmn.name))
            timesleep()
            ps('Congratulations! Your %s has evolved into %s'%(pkmn.name,newpkmn))
            self.evolup(pkmn.ID)
               
#Items Gen/Class/Sorting---------------------------------------------------------------------------------------------------------
class Item(object):
    Type = 'normal'
    def __init__(self,name,description,amount,number):
        self.name = name
        self.description = description
        self.amount = amount
        self.number = number
    

def pokemart(room):
    itemlist = ('Potion','Pokeball','Escape rope')
    if room == 'v_mart': # +++++++++++++++++++++++++++++++++++++++++++++++++
        ps('Welcome to the Veridian City Pokémon Mart branch!\n How can we serve you?')
        a = 1
        while a == 1:
            print(itemlist)
            cmd = input(': ')
            cmd = cmd[0].upper() + cmd[1,len(cmd)].lower()
            cmdlo = cmd.lower()
            if cmd in itemlist:
                ps('How many would you like?')
                amount = int(input(': '))
                cmdlo.amount = cmdlo.amount + amount
                ps('You now have %s many %s.'%(cmdlo.amount,cmd))
                break
            else:
                ps('That is not a buyable item!')
#Generates wild pokemon----------------------------------------------------------------------------------------------------
        
def wildpkmn(action,room,lvl):
    if room == 'tall_grass1' or room == 'tall_grass2' or room == 'tall_grass3' or room == 'tall_grass4' or room == 'tall_grass5' or room == 'tall_grass6' or room == 'tall_grass7':
        action = 'search'
        if room == 'tall_grass1':
            lvl = 2
        if room == 'tall_grass2':
            lvl = 3
        if room == 'tall_grass3':
            lvl = 5
        if room == 'tall_grass4':
            lvl = 7
        if room == 'tall_grass5':
            lvl = 10
        if room == 'tall_grass6':
            lvl = 13
        if room == 'tall_grass7':
            lvl = 15
        a = search(action)
        pkmn2 = genwildpkmn(a[0],lvl,a[1])
        battle(pkmn2)

def search(action): #Wild pokemon search
    import random
    global room
    chance = random.randint(1,100)
    if action == 'search':
        if room == 'tall_grass1' or room == 'tall_grass2':
            if chance in range(1,50):
                ps('A wild Pidgey appears!')
                wldpkmn = 'Pidgey'
            if chance in range(51,100):
                ps('A wild Rattata appears!')
                wldpkmn = 'Rattata'
        elif room == 'tall_grass3' or room == 'tall_grass4':
            if chance in range(1,50):
                ps('A wild Pikachu appears!')
                wldpkmn = 'Pikachu'
            if chance in range(51,100):
                ps('A wild Caterpie appeared!')
                wldpkmn = 'Caterpie'
        elif room == 'tall_grass5' or room == 'tall_grass6':
            if chance in range(1,50):
                ps('A wild Bagon appeared!')
                wldpkmn = 'Bagon'
            if chance in range(51,100):
                ps('A wild Larvitar appeared!')
                wldpkmn = 'Larvitar'
        elif room =='tall_grass7':
            if chance in range(1,50):
                ps('A wild Dratini appeared!')
                wldpkmn = 'Dratini'
            if chance in range(51,100):
                ps('A wild Gible appeared!')
                wldpkmn = 'Gible'
        if wldpkmn == 'Pidgey':
            ID = 10
        if wldpkmn == 'Pikachu':
            ID = 13
        if wldpkmn == 'Caterpie':
            ID = 16
        if wldpkmn == 'Bagon':
            ID = 19
        if wldpkmn == 'Larvitar':
            ID = 22
        if wldpkmn == 'Dratini':
            ID = 25
        if wldpkmn == 'Gible':
            ID = 28
        if wldpkmn == 'Rattata':
            ID = 31
        return (wldpkmn,ID)
    else:
        ps('You cannont search for pokémon here!')

def genwildpkmn(name,lvl,ID):
    stats = pstatgen(name,lvl,ID)
    pkmn = Create_Pokemon(stats[0],stats[1],stats[2],stats[3],stats[4],stats[5],stats[6],stats[7])
    return pkmn


#Battle functions------------------------------------------------------------------------------------------------------------

def battle(pkmn2):
    import random
    import time
    global pokebelt
    global movesindex
    global movesdmg
    global wildmoves
    global pkmn1moves
    global meds
    global pokeballs
    global name
    b = pkmn1moves
    pkmn1 = pokebelt.pop(0)
    pokebelt.insert(0,pkmn1)
    pt('\nCome out, ',pkmn1.name,'! ')
    time.sleep(2)
    ps('\nWhat will you do?\n')
    List = listcreate(meds)
    List1 = listcreate(pokeballs)
    list2 = listcreate(pokebelt)
    while pkmn1.HP > 0 or pkmn2.HP > 0:
        if pkmn1.HP <= 0 or pkmn2.HP <= 0:
            break
        ps('ATTACK, BAG, RUN, SWITCH')
        action = input(': ')
        action = action.lower()
        if action == 'check exp':
            print(pkmn1.exp)
            print(pkmn1.level * 25)
        if action == 'attack':  #pkmn_name,atk,Def,spd,hp,exp,lvl,ID
            print(b)
            move1 = input(': ')
            move1 = move1[0].upper()+ move1[1:len(move1)].lower()
            if move1 in b:
                print('Use ',move1,' ',pkmn1.name,'!')
                cmd = movesindex.index(move1)
                atkdmg = movesdmg.pop(cmd)
                movesdmg.insert(cmd,pkmn1.attack)
                dmg = int((pkmn1.attack/pkmn2.defense)*atkdmg)
                pkmn2.HP = pkmn2.HP - dmg
                if pkmn2.HP <= 0:
                    pkmn2.HP = 0
                    pkmn1.exp = pkmn1.exp + pkmn1.level*25### REPLACE THE CODE: 'pkmn1.exp + pkmn1.level*25' with the new code in line 3.
                    ps('%s has fainted! %s has gained %s EXP.\n' %(pkmn2.name,pkmn1.name,expgain(pkmn2.level)))
                    if checkexp(pkmn1.exp,pkmn1.level) == 'ready':
                        print('LEVEL: %s \nATK: %s\nDEF: %s\nSPD: %s\nHP: %s'%(pkmn1.level,pkmn1.attack,pkmn1.defense,pkmn1.speed,pkmn1.orHP))
                        pkmn1.level = pkmn1.level + 1
                        pkmn1.levelup()
                        pkmn1.Oneup(pkmn1)
                        print('LEVEL: %s \nATK: %s\nDEF: %s\nSPD: %s\nHP: %s'%(pkmn1.level,pkmn1.attack,pkmn1.defense,pkmn1.speed,pkmn1.orHP))
                    break
                print(pkmn2.name,' has taken ',dmg,' amount of damage.', pkmn2.name ,'is now at: ',pkmn2.HP,'.')
                move = random.randint(1,100)
                if pkmn2.name == 'Pidgey' or 'Rattata':
                    if move in range(1,50):
                        cmd = 0
                    if move in range(51,100):
                        cmd = 1
                move = wildmoves.pop(cmd)
                wildmoves.insert(cmd,move)
                atkdmg = movesdmg.pop(cmd)
                movesdmg.insert(cmd,atkdmg)
                print(pkmn2.name,' used ',move,'!')
                dmg = int((pkmn2.attack/pkmn1.defense)*atkdmg)
                pkmn1.HP = pkmn1.HP - dmg
                if pkmn1.HP < 0:
                    pkmn1.HP = 0
                print(pkmn1.name,' has taken ',dmg,' amount of damage.',pkmn1.name,' is now at: ',pkmn1.HP,'.')
                if pkmn1.HP == 0:
                    run = input(ps('%s has fainted! Use next pokemon? Y/N'%(pkmn1.name)))
                    run = run.lower()
                    if run == 'y':
                        ps('Got away safely!')
                        break
                    elif run == 'n':
                        pkmn1 = pokebelt.pop(1)
                        ps('Come on out, %s!'%(pkmn1.name))
        if action == 'bag':
            ps("Which pocket would you like to open?\nMEDICINE,POKEBALLS")
            cmd = input(': ')
            cmd = cmd.lower()
            if cmd == 'medicine':
                print(List)
                use = input(': ')
                use = use[0].upper()+ use[1:len(use)].lower()
                if use in List:
                    if use == 'Potion':
                        item = meds.pop(0)
                        print(item.description)
                        if item.number != 0:
                            meds.insert(0,item)
                            if pkmn1.HP < pkmn1.orHP:
                                pkmn1.HP = item.amount + pkmn1.HP
                                if pkmn1.HP > pkmn1.orHP:
                                    pkmn1.HP = orHP1
                                ps('%s is now at %s HP.' %(pkmn1.name,pkmn1.HP))
                            else:
                                ps("It won't have any effect.")
                        else:
                            ps('You do not have any left!')    
                        
            if cmd == 'pokeballs':
                print(List1)
                use = input(': ')
                use = use[0].upper()+ use[1:len(use)].lower()
                if use in List1:
                    if use == 'Pokeball':
                        item = pokeballs.pop(0)
                        print(item.description)
                        ps('%s threw a pokeball!\n'%(name))
                        pokeballs.insert(0,item)
                        a = pkmn2.orHP/pkmn2.HP
                        if a >= 4:
                            chance = 'a'
                        elif a >= 2:
                            chance = 'aa'
                        elif a >= 1:
                            chance = 'aaa'
                    capture = random.randint(1,len(chance))
                    timesleep()
                    if capture == 1:
                        if len(pokebelt) >= 6:
                            transfer(pkmn2)
                            break
                        else:
                            pokebelt.append(pkmn2)
                            ps('%s was added to your party!'%(pkmn2.name))
                            
                            break
                    else:
                        ps('You almost had it!')
                        
                else:
                    ps('That is not here!')
        if action == 'switch':
            if len(pokebelt) == 1:
                ps('You cannot switch pokemon. You only have one.\n')
            else:
                print(list2)
                ps('Use the number 1-6 to choose the next pokemon.\n')
                cmd = int(input(": \n"))
                cmd = cmd - 1
                if cmd in range (0,5):
                    pkmn1 = pokebelt.pop(cmd)
                    pokebelt.insert(cmd,pkmn1)
                    ps('Come out, %s!' %(pkmn1.name))
        if action == 'run':
            ps('Got away safely!')
            break

def expgain(lvl):
    expgain = lvl * (10)
    return expgain

def checkexp(exp,lvl):
    lvlreq = lvl * 25
    if exp >= lvlreq:
        return 'ready'
    else:
        return 'not ready'

def listcreate(meds):
    List = []
    if len(meds) == 1:
        pot1 = meds.pop(0)
        meds.insert(0,pot1)
        List.insert(0,pot1.name)
    if len(meds) == 2:
        pot1 = meds.pop(0)
        meds.insert(0,pot1)
        List.insert(0,pot1.name)
        pot2 = meds.pop(1)
        meds.insert(1,pot2)
        List.insert(1,pot2.name)
    if len(meds) == 3:
        pot1 = meds.pop(0)
        meds.insert(0,pot1)
        List.insert(0,pot1.name)
        pot2 = meds.pop(1)
        meds.insert(1,pot2)
        List.insert(1,pot2.name)
        pot3 = meds.pop(2)
        meds.insert(2,pot3)
        List.insert(2,pot3.name)
    if len(meds) == 4:
        pot1 = meds.pop(0)
        meds.insert(0,pot1)
        List.insert(0,pot1.name)
        pot2 = meds.pop(1)
        meds.insert(1,pot2)
        List.insert(1,pot2.name)
        pot3 = meds.pop(2)
        meds.insert(2,pot3)
        List.insert(2,pot3.name)
        pot4 = meds.pop(3)
        meds.insert(3,pop4)
        List.insert(3,pot4.name)
    if len(meds) == 5:
        pot1 = meds.pop(0)
        meds.insert(0,pot1)
        List.insert(0,pot1.name)
        pot2 = meds.pop(1)
        meds.insert(1,pot2)
        List.insert(1,pot2.name)
        pot3 = meds.pop(2)
        meds.insert(2,pot3)
        List.insert(2,pot3.name)
        pot4 = meds.pop(3)
        meds.insert(3,pop4)
        List.insert(3,pot4.name)
        pot5 = meds.pop(4)
        meds.insert(4,pot5)
        List.insert(4,pot5.name)
    if len(meds) == 6:
        pot1 = meds.pop(0)
        meds.insert(0,pot1)
        List.insert(0,pot1.name)
        pot2 = meds.pop(1)
        meds.insert(1,pot2)
        List.insert(1,pot2.name)
        pot3 = meds.pop(2)
        meds.insert(2,pot3)
        List.insert(2,pot3.name)
        pot4 = meds.pop(3)
        meds.insert(3,pop4)
        List.insert(3,pot4.name)
        pot5 = meds.pop(4)
        meds.insert(4,pot5)
        List.insert(4,pot5.name)
        pot6 = meds.pop(5)
        meds.insert(5,pot6)
        List.insert(5,pot6.name)
    return List

def transfer(pkmn):
    global billpc
    billpc.append(pkmn)
    ps('%s was put in Bills PC!'%(pkmn.name))
    
    
    
#Misc Functions------------------------------------------------------------------------------------------------------------

def Help(): #Generates possible commands to input for user.
        print('To move around, use commands "north" "west" "east" "south" to move around rooms.')
        print('To do actions in specific buildings/areas, use "buy","search","help"\nrespective to where you are.')

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

def timesleep():
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)    

def heal(room):
    global pokebelt
    line = len(pokebelt)
    if room == 'v_pcenter':
        if line >= 1:
            pkm1 = pokebelt.pop(0)
            pkm1.HP = pkm1.orHP
            pokebelt.insert(0,pkm1)
            if line >= 2:
                pkm2 = pokebelt.pop(1)
                pkm2.HP = pkm2.orHP
                pokebelt.insert(1,pkm2)
                if line >= 3:
                    pkm3 = pokebelt.pop(2)
                    pkm3.HP = pkm3.orHP
                    pokebelt.insert(2,pkm3)
                    if line >= 4:
                        pkm4 = pokebelt.pop(3)
                        pkm3.HP = pkm3.orHP
                        pokebelt.insert(3,pkm4)
                        if line >= 5:
                            pkm5 = pokebelt.pop(4)
                            pkm5.HP = pkm5.orHP
                            pokebelt.insert(4,pkm5)
                            if line == 6:
                                pkm6 = pokebelt.pop(5)
                                pkm6.HP = pkm6.orHP
                                pokebelt.insert(5,pkm6)
        timesleep()
        ps('All pokemon have been fully healed.')
            
#Events

def event_1(room,pokebelt,ec): #Prof Oak Event.---------------------------------------------------------------------------
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
        ps("\nYou are now in Professor Oak's Lab.\n")
        ps('OK, ')
        ps(name)
        ps('. Choose the pokemon of your choice!\n')
        ps('There are three pokemon to choose from:\n')
        ps('CHARMANDER - the blaze pokemon. A strong fire pokemon.\n')
        ps('SQUIRTLE - the turtle pokemon. A strong water pokemon.\n')
        ps('BULBASAUR - the vine pokemon. A strong grass pokemon.\n')
        ps('Choose one: C for Charmander, S for Squirtle, and B for Bulbasaur.\n')
        choice = input(': ') #Choose starter pkmn.
        choice = choice.upper()
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
        ps('To complete the game, navigate the route, and battle many wild pokemon!\n')
        ec = ec + 1
        return(room,pokebelt,ec)
    else:
        ec = ec
        return(room,pokebelt,ec)

def event_2(room,ec): #Intro to battling.------------------------------------------------------------------------------------
    import time
    if room == 'pallet_clearing':
        ps('You notice an old man!\n')
        time.sleep(1)
        ps('Who comes here? \nIf you are trying to go to the route, it is crawling with pokémon! \nI will teach you how to battle.')
        battle_intro()
        ec = ec + 1
        return ec
    else:
        return ec

def battle_intro(): 
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
    pkmn2 = genwildpkmn('Pidgey',5,'none')
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
    print("Pidgey has taken %s damage, Pidgey's HP is now at: %s."%(dmg,hp))
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

def event_3(room,ec): #Potions
    if room == 'route1_ent':
        ps('You see a person up ahead.\n')
        ps('Hi! Im a guy from the PokeMart store chain! \nCome check out our center in the next town!\n')
        ps('Here are unlimited Potions to help you on your journey!\nYou recieved 5 POTIONS!')
        time.sleep(1)
        ps(' You put the POTIONS in the MEDICINE pocket.\n')
        potion = Item('Potion','A healing spray that heals 20HP.',20,5)
        meds.insert(0,potion)
        ps('Here are unlimited POKEBALLS as well!')
        ps('\nYou put the pokeballs in the POKEBALLS pocket.\n')
        pokeball = Item('Pokeball','A basic capture ball',10,5)
        pokeballs.insert(0,pokeball)

        ec = ec + 1
        return ec
    else:
        return ec
    
#Global Variables
        
ec = 0
delay = 0
choice = 0
b = 0
#Lists

pokebelt = [] #This is party pokemon
billpc = []
pkmn1moves = ['Scratch','Tackle']
wildmoves = ['Scratch','Tackle']
movesindex = ['Scratch','Tackle']
movesdmg = [15,15]
meds = []
pokeballs = []
evol = [1,4,7,10,18,21,24,27]

pkmnID = ['none','Bulbasaur','Ivysaur','Venasaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Pidgey','Pidgetto','Pidgeot','Pikachu','Raichu','Riacha','Caterpie','Metapod','Butterfree','Bagon','Shellgon','Salamance','Larvitar','Pupitar','Tyranitar','Dratini','Dragonair','Dragonite','Gible','Gabite','Garchomp','Rattata','Raticate','Raticata',]
#Script

endg = 1
ps('NOTE: for testing purposes, the game speed/exp gain is seriously increased \n(you always level up after each battle).\n to play on normal speed, copy the code in triple quotes in line 3\n to the marked location with three #s.)\n')
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
    while times > 24 or times < 0:
        ps('Not a vaild time.')
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
    heal(room)
    if action == 'help' or action == 'Help':
        Help()
    if ec == 0:
        a = event_1(room,pokebelt,ec)
        room = a[0]
        pokebelt = a[1]
        ec = a[2]
    if ec == 1:
        ec = event_2(room,ec)
    if ec == 2:
        ec = event_3(room,ec)
