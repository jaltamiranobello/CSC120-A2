"""
    -storing information about a specific computer
"""
class Computer:
    #What attributes will it need?
    comp_name: str = ""
    processor: str = ""
    hard_drive: int = 0
    memory: int = 0
    system: str = ""
    year: int = ""
    price: int = 0

    # How will you set up your constructor?
    """ I will use the attributes as arguments in the constructor because I need to know all the info of the computer before hand as
    the information of the computer is something that will be given and not created.
    """

    # Remember: in python, all constructors have the same name (__init__)
    #an object has a description stored when it is initially given it
    def __init__(self, comp_name, processor, hard_drive, memory, system, year, price) -> None:
        self.comp_name = comp_name
        self.processor = processor
        self.hard_drive = hard_drive
        self.memory = memory
        self.system = system
        self.year = year
        self.price = price

    # What methods will you need?
    """ The computer will not be doing anything so the only method I need is to print the information of an object so I can do this
    with a details() function
    """
    #prints all the information of an object in computer
    def details(self) -> None:
        print(f"Description: {self.comp_name}, Processor Type: {self.processor}, Hard Drive Capacity: {self.hard_drive}, Memory: {self.memory}, OS: {self.system}, Year: {self.year}, Price: {self.price}")


def main():
    #comp_1 = Computer("Mac Pro", "3.5 GHC", 1024, 64, "MacOS Big Sur", 2013, 1500)
    #comp_1.details()
    pass
main()


    