#! /usr/bin/env python3
class Animal:
    def eat(self):   
        print (    "%s 吃"  %self.name)   
    def drink(self):   
        print (  "%s 喝"   %self.name)    
    def shit(self):   
        print ( "%s 拉"   %self.name)    
    def pee(self):   
        print ( "%s 撒"   %self.name)  

class Cat(Animal):    
    def __init__(self , name):   
        self.name = name    
    def cry(self):   
        print ('喵喵叫')  

class Dog(Animal):     
    def __init__(self , name):   
        self.name = name   
    def cry(self):   
        print ('啊啊啊')   
    def life(self):
        print('吃喝拉撒')
                
# c1 = Cat('小白家的小黑猫')   
# c1.eat()   
# c1.cry()   

    
d1 = Dog('张晓菲')   
d1.shit()
d1.cry()
d1.life()


