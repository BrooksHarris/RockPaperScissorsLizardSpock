class ElementError(Exception):
    pass

#betterthan and worsethan are lists of string names, and name is a string
class Element:
    def __init__(self, name, betterthan=[], worsethan=[]):
        self.name = name
        self.betterthan = betterthan
        self.worsethan = worsethan
        if len(self.betterthan) != len(self.worsethan):
            raise ElementError("Different amount of betterthans and worsethans.")
        if len(self.betterthan)%2 != 0:
            raise ElementError("Odd number of betterthans and worsethans.")
    def getBetterThan(self):
        return self.betterthan
    def getWorseThan(self):
        return self.worsethan
    def setBetterThan(self, new_betterthan):
        self.betterthan = new_betterthan
    def setWorseThan(self, new_worsethan):
        self.worsethan = new_worsethan
    def getName(self):
        return self.name

class GameError(Exception):
    pass

#names is a list of strings, rankings is a dictionary, where the key is better than the value
class Game:
    def __init__(self, names, b, w):
        self.elements = []
        better = b
        worse = w
        for name in names:
            betterthan = []
            for i in range(len(better)):
                if better[i] == name:
                    betterthan.append(worse[i])
            worsethan = []
            for i in range(len(worse)):
                if worse[i] == name:
                    worsethan.append(better[i])
            self.elements.append(Element(name,betterthan=betterthan,worsethan=worsethan))
    def getNames(self):
        names = []
        for element in self.elements:
            names.append(element.getName())
        return names
    def whoWins(self, name1, name2):
        names = self.getNames()
        element1 = self.elements[names.index(name1)]
        if name1 == name2:
            return "tie"
        elif name2 in element1.getBetterThan():
            return name1
        elif name2 in element1.getWorseThan():
            return name2
        else:
            raise GameError("No relationship between the two elements.")

# "rock":"scissors"
# "scissors":"paper"
# "paper":"rock"
# "spock":"rock"
# "paper":"spock"
# "spock":"scissors"
# "lizard":"spock"
# "lizard":"paper"
# "rock":"lizard"
# "scissors":"lizard"

if __name__ == "__main__":
    import random
    g = Game(["rock","paper","scissors","lizard","spock"],["rock","scissors","paper","spock","paper","spock","lizard","lizard","rock","scissors"],["scissors","paper","rock","rock","spock","scissors","spock","paper","lizard","lizard"])
    names = g.getNames()
    while True:
        element_input = input("Enter Choice: ")
        element_random = random.choice(names)
        print("You chose: " + str(element_input) + " and Computer chose: " + str(element_random))
        print("Winner: " + str(g.whoWins(element_input,element_random)))