#Chrissie Test Harness for the Haunted House
#v2.00 14/09/2022

#Top Level Class with the main() method

from tkinter import E
from Classes import Room, Character, Enemy, Item,Friend

backpack = []

i1 = Item("Cheese", "a big smelly block of blue Stilton cheese", "zombies")
print (i1.toString())
i2 = Item("Catnip", "a bag of the smelliest catnip known to man", "black cats")
print (i2.toString())
i3 = Item("Garlick","A smelly string of french galich that repels things","Vampires")

c1 = Enemy("Dave", "a smelly zombie")
c1.set_conversation("Wooooooooo!!!!")
#print(c1.describe())
#print(c1.talk())
c1.set_weakness ("Cheese")

"""if (c1.fight("Cheese")):
    print ("You have vanquished the foe, brave warrior!")
else:
    print ("You have been crushed, puny human!")"""

c2 = Friend("Wendy", "the good little witch",i3)
c2.set_conversation("How may I help you?")
#print(c2.describe())
#print(c2.talk())

r1 = Room("Kitchen", "a large, dark, damp room buzzing with flies, ugh!")
print (r1.toString())
r1.setResident(c1)
r1.placeItem (i1)
#print (r1.anybodyHere())

r2 = Room ("Conservatory", "a huge wrought-iron Victorian conservatory full of flesh eating plants!")
print (r2.toString())
#print (r2.anybodyHere())

r3 = Room ("Ballroom", "A huge ballroom with big chandeliers, all decorated in gold")
print (r3.toString())
r3.setResident(c2)
#print (r3.anybodyHere())

r1.linkRooms(r2, "N")
r2.linkRooms(r1, "S")

r1.linkRooms (r3, "E")
r3.linkRooms (r1, "W")

#print (r1.toString())
#print (r2.toString())
#print (r3.toString())

#set up the current room
current = r1
#first set up a stopping mechanism
done = False

while not done:
#main game loop
    print("\nYou are currently here >> "+ current.toString())
    command = input("Where do you want to go now? N S E W or Q > ")
    #makes sure that the input is uppercase
    command = command.upper()
    #checks that it's a valid response
    while command not in ["N", "S", "E", "W", "Q"]:
        command = input("You did not type N S E W or Q, try again!")
        command = command.upper()
    if command == "Q":
        done = True
        print ("Farewell, brave warrior!")
    else:
        current = current.move(command)
        print (current.anybodyHere())
        #add code here to fight if it is an enemy
        if (isinstance (current.getResident(), Enemy)) :
            decide = input ("[F]ight or [R]un?")
            #code here to get input and then decide what to do
        if(isinstance(current.getResident(),Friend)):
            print(current.getResident().Talk())
        print(current.anythingHere())