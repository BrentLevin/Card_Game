class Land():
    def __init__(self, name):
        self.name = name

Plains = Land("Plains")

a = {"Plains": Plains} #have a dictionary mapping objects to their string name

deck = ["Plains"] #have a list of strings from the imported deck so as to create the decklist of objects
newdeck = [] #decklist of objects

for i in deck: #for every string in the imported deck list (can we do this straight from the import? no its better to have it in a standardised converted format) find the equivalent object
    newdeck.append(a[i])

for i in newdeck:
    print(i.name)

print(newdeck)