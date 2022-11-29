"""
Exercise "Morris The Miner".

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Initial situation:
Morris has the attributes sleepiness, thirst, hunger, whisky, gold.
All attributes have the starting value 0.

Rules:
If sleepiness, thirst or hunger goes above 100, Morris the miner dies.
Morris can’t store more than 10 bottles of whisky.
No attribute may go below 0.

At each turn, Morris can perform exactly one of these activities:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Your task:
Write a program that gets Morris as much gold as possible in 1000 turns.

if you have no idea how to begin, open S0031_morris_help.py and start from there
if you get stuck, ask google, the other pupils or the teacher (in this order).

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


class morris:
    """Morris the miner."""

    sleepiness: int = 0
    thirst: int = 0
    hunger: int = 0
    whisky: int = 0
    gold: int = 0

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1
        self._ensure_zero()
        self._check_health("morris would never wake again")

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5
        self._check_health("while mining morris suddenly fell over")

    def eat(self):
        if self.gold > 1:
            self.sleepiness += 5
            self.thirst -= 5
            self.hunger -= 20
            self.gold -= 2
            self._ensure_zero()
            self._check_health(
                "while morris was eating he suddenly fell over.")
        else:
            print("too poor")

    def buy_whisky(self):
        if self.whisky == 10:
            print("morris already has 10 whisky, he cant carry more")
        elif self.gold < 1:
            print("too poor")
        else:
            self.sleepiness += 5
            self.thirst += 1
            self.hunger += 1
            self.whisky += 1
            self.gold -= 1
            self._check_health(
                "While going to the store to buy whisky morris fell over")

    def drink(self):
        if self.whisky > 0:
            self.sleepiness += 5
            self.thirst -= 15
            self.hunger -= 1
            self.whisky -= 1
            self._ensure_zero()
            self._check_health("While taking a pause to drink morris felt bad")
        else:
            print("must have wisky")

    def _ensure_zero(self):
        if self.thirst < 0:
            self.thirst = 0
        if self.hunger < 0:
            self.hunger = 0
        if self.sleepiness < 0:
            self.sleepiness = 0

    def _check_health(self, extra: str):
        if self.sleepiness > 100:
            print(extra)
            print("he had died of sleep deprivation")
            self._die()
        elif self.thirst > 100:
            print(extra)
            print("he had died of thirst")
            self._die()
        elif self.hunger > 100:
            print(extra)
            print("he had died of hunger")
            self._die()

    def _die(self):
        self.thirst = 0
        self.sleepiness = 0
        self.hunger = 0
        self.whisky = 0
        self.gold = 0

    def __repr__(self):
        return f"Morris status:\nHunger: {self.hunger}\nThirst: {self.thirst}\nSleepiness: {self.sleepiness}\nGold: {self.gold}\nWhisky stored: {self.whisky}"


me = morris()
for i in range(1000):
    if me.thirst > 50:
        me.drink()
    elif me.sleepiness > 50:
        me.sleep()
    elif me.hunger > 50:
        me.eat()
    elif me.whisky == 0 and me.gold > 1:
        me.buy_whisky()
    else:
        me.mine()
print(me)
