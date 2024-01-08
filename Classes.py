#Room class by Chrissie
#v1.00 07/09/2022
#a class to emulate a room in a haunted house

class Room:

    #full constructor to make the room objects
    def __init__(self, n, d ):
        #attributes next
        #name of the room
        self.name = n
        #description
        self.description = d
        #rooms that are linked to this one
        #this is stored as a hashmap of key-value pairs
        self.linkedRooms = {}
        self.resident = None
        self.item = None

    def toString(self):
        info = ("This is the " + self.name + " and it is " + self.description + "\n")
        for dir in self.linkedRooms:
            #loops through the hashmap, and gets details of the next linked room
            lr = self.linkedRooms[dir]
            #and adds the details of the linked room to the display string
            info = info +  ("The " + lr.getName() + " is " + dir + "\n" )
        return info

    #getters, one for each attribute (accessor methods)
    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    #setters, one for each attribute (modifiers or transformers)
    def setName(self, n):
        self.name = n

    def setDescription(self, d):
        self.description = d

    def linkRooms (self, rtl, dir):
        #this is a modifier method
        #passes in a direction (N,S,E,W) and a room to link in that direction
        self.linkedRooms[dir] = rtl

    def move(self, direction):
    #this is a hybrid method as it is both an accessor and a transformer
        if direction in self.linkedRooms:
            return self.linkedRooms[direction]
        else:
            print("You can't go that way")
        return self

    def setResident(self, resident):
        self.resident = resident

    def getResident(self):
        return self.resident

    def anybodyHere(self):
    #query whether there is anyone in the room
        if not (self.resident == None):
            return (self.resident.describe())
        else:
            return ("There is nobody here.")

    def placeItem (self, i):
        self.item = i

    def anythingHere (self):
            #query whether there is anyone in the room
        if not (self.item == None):
            return (self.item.toString())
        else:
            return ("There is nothing here.")

class Character():
    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        info = self.name + " is here!"
        info = info + "\n" +self.description
        return info

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def Talk(self):
        if self.conversation is not None:
            return("[" + self.name + " says]: " + self.conversation + "\n")
        else:
            return(self.name + " doesn't want to talk to you")

class Enemy (Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, combat_item):
    #a polymorphic method
        if (combat_item == self.weakness):
            return True
        else:
            return False


class Friend(Character):
    def __init__(self,char_name,char_description,gift):
        super().__init__(char_name,char_description)
        self.gift = gift
        
    def Talk(self):
        if self.conversation is not None:
            info = "[" + self.name + " says ]: " + self.conversation
            info = info + self.name + " has a gift for you"
            info + info + "\n" + self.gift.toString()
            return info
        else:
            return(self.name + " doesnt want to talk to you")

    def acceptgift(gift):
        pass

class Item():
    def __init__(self, n, d, wu):
        self.name = n
        self.description = d
        self.where_used = wu

    #follow up with the usual gets and sets and toString()
    #you can either make the item part of a room, like the character
    #or you can make it part of a character - you will fight the enemy for it
    #and the friend will give it to you

    def toString(self):
        return ("This is " + self.name + " and it is " + self.description
        + "\nAnd it works especially well on " + self.where_used)

    def getName(self):
        return self.name

    def getDescription (self):
        return self.description

    def getWhereUsed(self):
        return self.where_used

    def setName(self, n):
        self.Name = n

    def setDescription (self, d):
        self.description = d

    def setWhereUsed(self, wu):
        self.where_used = wu