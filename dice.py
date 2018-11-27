from random import randint

class Die():

    def __init__(self, sides):
        self.sides = 6
        
    def roll_die(self):
        x = randint(1, self.sides)
        print(str(x))
        
        
dice1=Die(6)
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()
dice1.roll_die()

dice2=Die(10)
dice2.sides = 10
dice2.roll_die()
dice2.roll_die()
dice2.roll_die()
dice2.roll_die()
dice2.roll_die()
dice2.roll_die()
dice2.roll_die()
dice2.roll_die()
dice2.roll_die()
dice2.roll_die()

dice3=Die(20)
dice3.sides = 20
dice3.roll_die()
dice3.roll_die()
dice3.roll_die()
dice3.roll_die()
dice3.roll_die()
dice3.roll_die()
dice3.roll_die()
dice3.roll_die()
dice3.roll_die()
dice3.roll_die()