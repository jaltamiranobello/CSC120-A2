""" 
  - storing the inventory for the store 
  - updating a computer's price 
  - updating a computer's OS
  - buying a computer (add to inventory)
  - selling a computer (remove from inventory)
  - refurbishing a computer
    """
from computer import * 
#imports everything from computer

class ResaleShop:
    # What attributes will it need?
    inventory: list = []

    # How will you set up your constructor?
    #   I will need an inventory in resaleshop but it is not something that needs to be initialized so I will not put the attribute of 
    #   an inventory as an argument. To do so I will use a list

    # Remember: in python, all constructors have the same name (__init__)
    #   Ititializes the shop with an empty inventory
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    """ I need to be able to buy() a computer then anotehr method to storeInventory() of the store. I also need one to refurbish()
    the computers I buy and finally one to sell() the computers
    """
    # takes in an object from computer class and adds it into the invenotry in resaleshop, returns nothing
    def buy(self, computer: Computer) -> None:
        self.inventory.append(computer)

    # takes in an object from computer class and a new_system from main then it will check if the computer exists in the store inventory and
    # if it does it will update the price depending on the year it was made and update the system if a new_system is given. If the computer
    # given is not in the inventory then it will print a statement saying it doesn't exist.
    def refurbish(self, computer: Computer, new_system)-> None:
        if computer in self.inventory:
            if computer.year < 2000:
                computer.price = 0
            elif computer.year < 2012:
                computer.price = 250
            elif computer.year < 2018:
                computer.price = 550
            else:
                computer.price = 1000
            if new_system != None:
                computer.system = new_system
        else: 
            print(f"{computer.comp_name}, not found in inventory. Please select another item to refurbish.")

    # for every computer in self.inventory it will assign it an ID and remove it from the inventory if it already existed in the inventory
    # otherwise it will print out a statment saying the item is not held in the store.
    def sell(self, computer: Computer)-> None:
        if computer in self.inventory:
            ID = 0
            for computer in self.inventory:
                ID +=1
                print(f"Selling item {ID}...")
                self.inventory.remove(computer)
                print("Item sold!")
                print("Updating inventory..\n")

        else:
            print("Sorry we don't have that item...\n")

    # for every computer it will be given an ID which will be printed alongside all the information of a computer in the inventory but
    # if there is no computers in the inventory then it will print no items
    def storeInventory (self, computer: Computer )-> None:
        print("Checking inventory...")
        if self.inventory != []:
            ID = 0
            for computer in self.inventory:
                ID += 1
                self.inventory[ID-1] = computer
                print(f"Item ID: {ID}, Description: {computer.comp_name}, Processor Type: {computer.processor}, Hard Drive Capacity: {computer.hard_drive}, Memory: {computer.memory}, OS: {computer.system}, Year: {computer.year}, Price: {computer.price}")
    
        else: 
            print("No items in inventory.\n")

#creates object in reslaeshop and computer then calls on methods in resaleshop
def main():
    comp1 = Computer("Mac Pro", "3.5 GHc" , 1024, 64, "mac OS Big Sur", 2013, 1500)
    comp2 = Computer("HP Laptop", "3.5 Ghc", 2300, 256, "Windows 11", 2011, 1000)
    store = ResaleShop()
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    print(f"Buying {comp1.comp_name}")
    print(f"Buying {comp2.comp_name}")
    print("Adding to inventory...")
    print("Done.\n")
    store.buy(comp1)
    store.buy(comp2)
    store.storeInventory(comp2)
    print("")
    print("Refurbishing Item ID: 1, updating OS to MacOS Monterey")
    print("Refurbishing Item ID: 2, not updating sysytem")
    print("")
    print("Updating inventory...")
    store.refurbish(comp1, "MacOS Monterey")
    store.refurbish(comp2, None)
    print("Done.\n")
    store.storeInventory(comp2)
    print("Done.\n")
    store.sell(comp1)
    store.storeInventory(comp2)
    print("Done.\n")    
main()


