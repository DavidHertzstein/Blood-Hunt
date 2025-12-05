class Hero:
    def __init__(self, name, klasse):  
        self.name = name
        self.klasse = klasse
        self.hitpoints = 100
        self.maxhp = 100
        self.magicpoints  = 50
        self.maxmp = 50
        self.strength = 20
        self.dexterity = 10
        self.armor = 5
        self.dodgechance = 5
 
        # Klassenspezifische (Boni) Werte
        if self.klasse.lower() == "krieger":
            self.hitpoints = 250
            self.maxhp = 250
            self.magicpoints = 40
            self.maxmp = 40
            self.strength = 50
            self.dexterity = 8
            self.armor = 15
            self.dodgechance = 3

        elif self.klasse.lower() == "magier":
            self.hitpoints = 100
            self.maxhp = 100
            self.magicpoints = 40
            self.maxmp = 40
            self.strength = 25
            self.dexterity = 12
            self.armor = 2
            self.dodgechance = 3

        elif self.klasse.lower() == "assasine":
            self.hitpoints = 90
            self.maxhp = 90
            self.magicpoints = 60
            self.maxmp = 60
            self.strength = 28
            self.dexterity = 20
            self.armor = 8
            self.dodgechance = 15

class Weapon:
    def __init__(self):
        self.name = ""
        self.classic_atk= 0
        self.special_atk = 0
        self.attack_special_manacost = 0
        self.ultimate_atk = 0
        self.attack_ultimate_manacost = 0



    def krieger_waffe(self):
        self.name = "Kriegsschwert"
        self.classic_atk= 25
        self.special_atk = 40
        self.attack_special_manacost = 15
        self.ultimate_atk = 70
        self.attack_ultimate_manacost = 30


    def magier_waffe(self):
        self.name = "Arkaner-Stab"
        self.classic_atk = 15
        self.special_atk = 55
        self.attack_special_manacost = 20
        self.ultimate_atk = 100
        self.attack_ultimate_manacost = 40

    def assasine_waffe(self):
        self.name = "Schattendolch"
        self.classic_atk= 22
        self.special_atk = 45
        self.attack_special_manacost = 10
        self.ultimate_atk = 80
        self.attack_ultimate_manacost = 25
        
        

class Items:
    def __init__(self):
        self.health_potion_healing = 50
        self.manapotion = 30

    
    
        



        