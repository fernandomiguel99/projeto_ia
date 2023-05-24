#Projeto de Inteligência Artificial entrega: 25/05/2023
#Professor: Fagner , Aluno: Fernando Miguel D'Andrea Lima
#Robocup@Home Go and Get It
#Git: https://github.com/fernandomiguel99/projeto_ia

class robot:
    def __init__(self,type,location,hand):
        self.type=type
        self.location=location
        self.hand=hand

class object:
    def __init__(self, type, location):
        self.type = type
        self.location = location

class person:
    def __init__(self, type, location, hand):
        self.type = type
        self.location = location
        self.hand = hand

Hera = robot("Robot","office","empty")

Fanta = object("Fanta","kitchen_table")
Beer_can = object("Beer_can","trash_bin")
Coke = object("Coke","trash_bin")
Milk = object("Milk","kitchen_table")
Apple_juice = object("Apple_juice","office")

Michael = person("Michael","kitchen","empty")
Daniel = person("Daniel","trash_bin","empty")
Christopher = person("Christopher","bookshelf","empty")
Matthew = person("Matthew","office","empty")
Joshua = person("Joshua","exit","empty")
David = person("David","apartment","empty")


#print(fanta.type)

def goto(target):
    if target in ('apartment','kitchen','office','trash_bin','exit','kitchen_table','bookshelf'):
        print("Current location:",Hera.location)
        print("Target detected: location",target)
        print("moving to",target)
        Hera.location = target
        print("Final location:",Hera.location)
        print("-----------------")
    else:
        if target.type in ('Fanta','Beer_can','Coke','Milk','Apple_juice'):
            print("Current location:",Hera.location)
            print("Target detected: object",target.type)
            print("moving to",target.location)
            Hera.location = target.location
            print("Final location:",Hera.location)
            print("-----------------")
        elif target.type in ('Michael','Christopher','Matthew','Joshua','Daniel','David'):
            print("Current location:",Hera.location)
            print("Target detected: person",target.type)
            print("moving to",target.location)
            Hera.location = target.location
            print("Final location:",Hera.location)
            print("-----------------")
        else:
            print("Sorry, couldn't get it right.")
            print("-----------------")

def pick(target):
    if target in ('apartment','kitchen','office','trash_bin','exit','kitchen_table','bookshelf'):
        print("ERROR, cannot pick up a location!")
        print("-----------------")
    else:
        if target.type in ('Fanta','Beer_can','Coke','Milk','Apple_juice'):
            if Hera.hand == "empty":
                print("Current location:",Hera.location)
                print("Target detected: object",target.type)
                print("Target location:",target.location)
                if Hera.location == target.location:
                    Hera.hand = target.type
                    target.location = "Hera"
                    print("Successfully picked",target.type+"!")
                    print("-----------------")
                else:
                    print("ERROR, cannot pick up "+target.type+". "+Hera.type+" and "+target.type+" are on different locations.")
                    print("-----------------")
            else:
                print("ERROR, cannot pick up "+target.type+" while "+Hera.type+" is holding "+Hera.hand)
                print("-----------------")
        elif target.type in ('Michael','Christopher','Matthew','Joshua','Daniel','David'):
            print("ERROR, cannot pick up a person!")
            print("-----------------")

        else:
            print("Sorry, couldn't get it right.")
            print("-----------------")

def place(target):    
    if target.type in ('Hera'):
            print("Current location:",Hera.location)
            held_obj = find_target(Hera.hand)
            held_obj.location = Hera.location         
            
            Hera.hand = "empty"
            print("Successfully placed "+held_obj.type+"!")
            print("-----------------")

    elif target.type in ('Michael','Christopher','Matthew','Joshua','Daniel','David'):
        print("Current location:",Hera.location)
        held_obj = find_target(Hera.hand)
        held_obj.location = target.type
        target.hand = held_obj.type

            
        Hera.hand = "empty"
        print("Successfully placed "+held_obj.type+"!")
        print("-----------------")

    else:
        print("Sorry, couldn't get it right.")
        print("-----------------")


def talk(target):
    if target in ('apartment','kitchen','office','trash_bin','exit','kitchen_table','bookshelf'):
        print("ERROR, cannot talk to a location dummy!")
        print("-----------------")

    else:    
        if target.type in ('Fanta','Beer_can','Coke','Milk','Apple_juice'):
            print("ERROR, cannot talk to an object dummy!")
            print("-----------------")

        elif target.type in ('Michael','Christopher','Matthew','Joshua','Daniel','David'):
            print("Current location:",Hera.location)
            if Hera.location == target.location:
                print("Target detected: person")
                print("Name:,", target.type)
                print("Hello ",target.type)
                print("-----------------")
            elif Hera.location != target.location:
                print("ERROR, cannot find"+target.type+" at this location:"+Hera.location)
                print("-----------------")       
        else:
            print("Sorry, couldn't get it right.")
            print("-----------------")

#goto(fanta)

#pick(fanta)

#talk(daniel)

#place(fanta)

#pick(fanta)

#goto(daniel)

#give(fanta,daniel)

def locals(target,local):
    if target.location == local:
        print(target.type+", ", end = '')    

def print_locals():
    locations=['apartment','kitchen','office','trash_bin','exit','kitchen_table','bookshelf']
    objects=[Hera,Michael,Christopher,Matthew,Joshua,Daniel,David,Fanta,Beer_can,Coke,Milk,Apple_juice]
    print("Locations:")
    for i in range(len(locations)):
        print("")
        print(" "+locations[i]+": ", end = '')
        #print( end = '')
        for j in range(len(objects)):
            locals(objects[j],locations[i])
    print("")
    print("")
    print("In Hands:")
    print("")
    print(" Hera: "+Hera.hand)
    print(" Michael: "+Michael.hand)
    print(" Christopher: "+Christopher.hand)
    print(" Matthew: "+Matthew.hand)
    print(" Joshua: "+Joshua.hand)
    print(" Daniel: "+Daniel.hand)
    print(" David: "+David.hand)

def find_target(target):
    #objects=[Michael,Christopher,Matthew,Joshua,Daniel,David,Fanta,Beer_can,Coke,Milk,Apple_juice]
    if target == 'apartment':
        obj = 'apartment'
    elif target =='kitchen':
        obj = 'kitchen'
    elif target =='office':
        obj = 'office'
    elif target == 'trash_bin':
        obj = 'trash_bin'
    elif target == 'exit':
        obj = 'exit'
    elif target =='kitchen_table':
        obj = 'kitchen_table'
    elif target =='bookshelf':
        obj = 'bookshelf'
    elif target == "Michael":
        obj = Michael
    elif target == "Christopher":
        obj = Christopher
    elif target == "Matthew":
        obj = Matthew
    elif target == "Joshua":
        obj = Joshua
    elif target == "Daniel":
        obj = Daniel
    elif target == "David":
        obj = David
    elif target == "Fanta": 
        obj=Fanta
    elif target == "Beer_can":
        obj= Beer_can
    elif target == "Coke":
        obj = Coke
    elif target == "Milk":
        obj = Milk
    elif target == "Apple_juice":
        obj =Apple_juice      
    elif target == "Hera":
        obj = Hera
    else:
        obj = ""
    return obj


print_locals()
print("--------------------------------------------")
print("Hello I'm Hera, your Robot Assistant.")
print("Ready to help! Please give an order to me!")
print(" goto : Go to a place or a Person")
print(" pick : Pick an object")
print(" place : Place held Object ")
print(" talk : Talk to a Person")
print(" give : Give held Object to a Person")
print(" help")


while True:
    print("")
    print("Current location:",Hera.location)
    order = input("-> ")
    print(order)
    if order == "goto":
        print("Go where?")
        arg = input("->")
        _obj = find_target(arg)
        print(_obj)
        goto(_obj)
        print_locals()
        del(_obj)
    elif order == "pick":
        print("Pick what?")
        arg = input("->")
        _obj = find_target(arg)
        print(_obj)
        pick(_obj)
        print_locals()
        del(_obj)
    elif order == "place":
        print("Place where?")
        arg = input("->")
        _obj = find_target(arg)
        print(_obj)
        place(_obj)
        print_locals() 
        del(_obj)
    elif order == "talk":
        print("Talk to who?")
        arg = input("->")
        _obj = find_target(arg)
        print(_obj)
        talk(_obj)
        print_locals()
        del(_obj)

    elif order == "help":
        print(" goto : Go to a place or a Person")
        print(" pick : Pick an object")
        print(" place : Place held Object")
        print(" talk : Talk to a Person")
        print(" help")
        print_locals()
    elif order == "quit":
        break
    else: 
        print("Sorry, could't get it right.")      
print("-End-")