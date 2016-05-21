#!/usr/bin/python2.7 -tt

class Hero:   #
    def __init__(self,name):
        self.name = name
        self.health = 100
        
    def eat(self, food):  #Ph(self, var, var)
        if (food == 'apple'):
            self.health -= 100
        if (food == 'ham'):
            self.health += 20   
            
Bob = Hero("bob")
print Bob.name
print Bob.health

Bob.eat('ham')
print Bob.health

Bob.eat('apple')
print Bob.health