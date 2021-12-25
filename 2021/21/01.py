with open("input") as f:
    p1 = int(f.readline()[28:])
    p2 = int(f.readline()[28:])

class Die:
    def __init__(self):
        self.value = 1
        self.rolls = 0

    def roll(self):
        self.rolls += 1
        result = self.value
        self.value += 1
        if self.value == 101:
            self.value = 1
        return result

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.score = 0

    def move(self, die):
        roll = die.roll() + die.roll() + die.roll()
        self.pos += roll
        while self.pos > 10:
            self.pos -= 10
        self.score += self.pos
        return self.score >= 1000

p1, p2 = Player(p1), Player(p2)
die = Die()

while True:
    if p1.move(die):
        break
    if p2.move(die):
        break

print(die.rolls * (p1.score if p1.score < 1000 else p2.score))
