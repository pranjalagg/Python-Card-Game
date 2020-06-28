
class Knight:

    def __init__(self, skill):
        self.health = 100
        self.armour = 100
        self.skill = skill
        #self.score = 0

    def in_health(self):
        if self.health < 100:
            self.health += 10

    def dec_health(self):
        if self.health >= 50:
            self.health -= 50

    def dec_health_sp(self):
        if self.health >= 50 and self.health < 100:
            self.health = 0
        else:
            self.health -=100

    def get_health(self):
        return self.health

    def in_armour(self):
        if self.armour < 100:
            self.armour += 5

    def dec_armour(self):
        self.armour -= 5

    def get_armour(self):
        return self.armour

    def get_skill(self):
        return self.skill