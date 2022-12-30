class People:
    def __init__(self,name,lastName):
        self.name = name
        self.lastName = lastName

    def __str__(self):
        print("Hello my name is "+ self.name + " " + self.lastName)
    
    def upperName(self):
        print("MY NAME IS "+ self.name.upper() + " " +self.lastName.upper())

me = People("Alan","Akra")
me.__str__()
me.upperName()