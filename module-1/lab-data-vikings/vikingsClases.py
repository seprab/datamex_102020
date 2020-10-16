import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        Soldier.__init__(self, health, strength)

    def receiveDamage(self, damage):
        Soldier.receiveDamage(self, damage)
        return f"{self.name} has received {damage} points of damage" if self.health > 0 else f"{self.name} has died " \
                                                                                             f"in act of combat "

    def battleCry(self):
        return "Odin Owns You All!"


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        Soldier.receiveDamage(self, damage)
        return f"A Saxon has received {damage} points of damage" if self.health > 0 else "A Saxon has died in combat"


# War


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, _viking):
        self.vikingArmy.append(_viking)

    def addSaxon(self, _saxon):
        self.saxonArmy.append(_saxon)

    def vikingAttack(self):
        rand_viking = self.vikingArmy[random.randrange(0, len(self.vikingArmy))]
        rand_saxon = self.saxonArmy[random.randrange(0, len(self.saxonArmy))]
        print_msg = rand_saxon.receiveDamage(rand_viking.attack())
        self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health > 0]
        return print_msg

    def saxonAttack(self):
        rand_viking = self.vikingArmy[random.randrange(0, len(self.vikingArmy))]
        rand_saxon = self.saxonArmy[random.randrange(0, len(self.saxonArmy))]
        print_msg = rand_viking.receiveDamage(rand_saxon.attack())
        self.vikingArmy = [viking for viking in self.vikingArmy if viking.health > 0]
        return print_msg

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
