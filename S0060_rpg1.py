"""
Exercise: Object oriented role playing game, part 1 :

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Define a class "Character" with attributes "name, max_health", "_current_health", "attackpower."
_current_health shall be a private attribute, it is not meant to be changed from outside the class.

Add a constructor (__init__) which accepts the classes' attributes as parameters.
Add a method for printing out class objects (__repr__).

Add a method "hit" which reduces _current_health of another character by attackpower.
Example: _current_health=80 and attackpower=10: a hit reduces _current_health to 70.

The method hit may not change the private attribute _current_health of a (potentially) foreign class.
For this reason we define another method get_hit which reduces _current_health of the object it belongs to by attackpower.

If you get stuck, ask google, the other pupils or the teacher (in this order).
If you have no idea how to begin, open S0061_rpg1_help.py and start from there.

When your program is complete, push it to your github repository
and compare it to the teacher's solution in S0065_rpg1_solution.py
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


class Character:

    def __init__(self, name: str, max_health: int, attackpower: int):
        self.name = name
        self.max_health = max_health
        self.attackpower = attackpower

    def __repr__(self):
        return f"{self.name} has {self._current_health}/{self.max_health} health, with {self.attackpower} attack power"

    def hit(self, person):
        person.get_hit(self.attackpower)

    def git_hit(self, attackpower: int):
        self._current_health -= attackpower
