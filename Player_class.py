class Player:
    gender = "male"
    rank = "sergeant"

    #Constructor
    def __init__(self, name, health = 100, ammo = 50):
        #Instance variables
        self.name = name
        self.health = health
        self.ammo = ammo

    #Accessors and Mutators
    @property
    def name(self):
        print("in name accessor")
        return self._name
        
    
    @name.setter
    def name(self, value):
        self._name = value
        print("in name mutator")
        
    @property
    def health(self):
        print("in health accessor")
        return self._health
        
    
    @health.setter
    def health(self, value):
        if (value >= 0 and value <= 100):
            self._health = value
        else:
            self._health = 100
        print("in health mutator")    

    @property
    def ammo(self):
        print("in ammo accessor")
        return self._ammo
        

    @ammo.setter
    def ammo(self, value):
        if (value >= 0 and value <= 50):
            self._ammo = value
        else:
            self._ammo = 50
        print("in ammo mutator")

    #Behaviors
    def damage(self):
        self.health -= 10

    def reload(self):
        self.ammo = 50

    def shoot_bullet(self):
        self.ammo -= 1

    def __str__(self):
        return("{}:\t Ammo: {}\tHealth: {}".format(self.name, self.ammo, self.health))

# Object
player1 = Player("Jimmy")

player1.shoot_bullet()
player1.shoot_bullet()
player1.shoot_bullet()
player1.shoot_bullet()
print(player1)
player1.damage()
player1.damage()
print(player1)
player1.reload()
print(player1)
# Execution: 64, 2, 3, 6, 8, 20, 21, 9, 31, 32, 33, 10, 45, 46, 47, 4*(68, 59, 60, 39, 41, 45, 46, 47)
# 72, 62, 63, 14, 16, 63, 39, 41, 63, 25, 27, 2*(73, 53, 54, 25, 27, 31, 32, 33), goes through print sequence
# 76, 56, 57, 39, 41, 45, 46, 47, 77, goes through print sequence; finish
