class Land():
    def __init__(self, name):
        self.name = name

Plains = Land("Plains")

a = {"Plains": Plains}

deck = ["Plains"]
newdeck = []

for i in deck:
    newdeck.append(a[i])

for i in newdeck:
    print(i.name)

print(newdeck)