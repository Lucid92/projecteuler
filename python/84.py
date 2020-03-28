# I would usually split all these classes up into different files but trying to keep these solutions to a single file.

import random

#--------
# Classes
#--------
class Location:
    def __init__(self, label):
        self.label = label
        self.visits = 0

class Player:
    def __init__(self):
        self.location = 0
    
    def move(self, roll):
        self.location = (self.location + roll) % 40

class Card:
    def __init__(self, action):
        self.action = action

    def doAction(self, *args):
        self.action(self, *args)

    def _doNothing(self, player):
        pass

    def _advanceToGo(self, player: Player):
        player.location = 0

    def _goToJail(self, player: Player):
        player.location = 10

class Chest(Card):
    ''' All functionality covered by Card '''    

class Chance(Card):
    def _advanceToGo(self, player: Player):
        player.location = 0
    
    def _goToJail(self, player: Player):
        player.location = 10

    def _goToC1(self, player: Player):
        player.location = 11

    def _goToE3(self, player: Player):
        player.location = 24

    def _goToH2(self, player: Player):
        player.location = 39

    def _goToR1(self, player: Player):
        player.location = 5

    def _goToNextR(self, player: Player):
        r_locations = [5, 15, 25, 35]

        if player.location > 35:
            player.location = 5
            return

        for r in r_locations:
            if r > player.location:
                player.location = r
                return

    def _goToNextU(self, player: Player):
        if 12 > player.location > 28:
            player.location = 12
        else:
            player.location = 28

    def _goBack3(self, player: Player):
        player.move(-3)       

#-----
# Main code
#-----
def drawCard(deck):
    card = deck.pop(0)
    deck.append(card)

    return card


# Set up decks
chest = [
    Chest(Chest._advanceToGo),
    Chest(Chest._goToJail)
]

for _ in range(14):
    chest.append(Chest(Chest._doNothing))

chance = [
    Chance(Chance._advanceToGo),
    Chance(Chance._goToJail),
    Chance(Chance._goToC1),
    Chance(Chance._goToE3),
    Chance(Chance._goToH2),
    Chance(Chance._goToR1),
    Chance(Chance._goToNextR),
    Chance(Chance._goToNextR),
    Chance(Chance._goToNextU),
    Chance(Chance._goBack3)
]

for _ in range(6):
    chance.append(Chance(Chance._doNothing))

# Set up board
board = [
    Location("GO"), Location("A1"), Location("CC1"),
    Location("A2"), Location("T1"), Location("R1"),
    Location("B1"), Location("CH1"), Location("B2"),
    Location("B3"), Location("JAIL"), Location("C1"),
    Location("U1"), Location("C2"), Location("C3"),
    Location("R2"), Location("D1"), Location("CC2"),
    Location("D2"), Location("D3"), Location("FP"),
    Location("E1"), Location("CH2"), Location("E2"),
    Location("E3"), Location("R3"), Location("F1"),
    Location("F2"), Location("U2"), Location("F3"),
    Location("G2J"), Location("G1"), Location("G2"),
    Location("CC3"), Location("G3"), Location("R4"),
    Location("CH3"), Location("H1"), Location("T2"), Location("H2")
]								

player = Player()
consecutive_doubles = 0

for _ in range(5000000):
    r1 = random.randint(1, 4)
    r2 = random.randint(1, 4)    

    # Handle doubles
    if r1 == r2:
        consecutive_doubles += 1
        if consecutive_doubles == 3:
            player.location = 10
            consecutive_doubles = 0
            board[player.location].visits += 1
            continue
    else:
        consecutive_doubles = 0

    player.move(r1 + r2)

    # Special squares
    if board[player.location].label.startswith("CH"):
        drawCard(chance).doAction(player)
    if board[player.location].label.startswith("CC"):
        drawCard(chest).doAction(player)   
    if board[player.location].label == "G2J":
        player.location = 10

    board[player.location].visits += 1

places = sorted(board, key=lambda b: b.visits, reverse=True)[:5]

for p in places:
    print(p.label, p.visits)