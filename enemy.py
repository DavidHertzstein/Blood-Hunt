class Enemies:
   def __init__(self):
       self.name = ""
       self.hitpoints = 100 #Aktuelle Anzahl der Lebenspunkte
       self.maxhp = 100 #Maximale Anzahl der Lebenspunkte
       self.strength = 10 #Stärke zeigt wie viel Schaden der Gegner macht
       self.dodgechance = 1 #Zeigt eine mögliche Ausweich-Chance 1 = 10% um auszuweichen, 4 = 40% etc
       self.critchance = 1 #Zeigt Chancen auf kritische Treffer 1 = 10% um auszuweichen, 4 = 40% etc
#<<<Enemy Dracula>>>
   def enemy_dracula(self):
       self.hitpoints = 70 #Aktuelle Anzahl der Lebenspunkte
       self.maxhp = 70 #Maximale Anzahl der Lebenspunkte
       self.name = "Dracula"
       self.strength = 30 #Stärke zeigt wie viel Schaden der Gegner macht
       self.dodgechance = 7 #Zeigt eine mögliche Ausweich-Chance 1 = 10% um auszuweichen, 4 = 40% etc
       self.critchance = 5 #Zeigt Chancen auf kritische Treffer 1 = 10% um auszuweichen, 4 = 40% etc
#<<<Enemy Rosenkreuzritter>>>
   def enemy_rosen_kreuz_ritter(self):
       self.hitpoints = 200 #Aktuelle Anzahl der Lebenspunkte
       self.maxhp = 200 #Maximale Anzahl der Lebenspunkte
       self.name = "Rosenkreuzritter"
       self.strength = 35 #Stärke zeigt wie viel Schaden der Gegner macht
       self.dodgechance = 10 #Zeigt eine mögliche Ausweich-Chance 1 = 10% um auszuweichen, 4 = 40% etc
       self.critchance = 5 #Zeigt Chancen auf kritische Treffer 1 = 10% um auszuweichen, 4 = 40% etc
#<<<Enemy Stone Golem>>>
   def enemy_minotaurus(self):
       self.hitpoints = 120 #Aktuelle Anzahl der Lebenspunkte
       self.maxhp = 120 #Maximale Anzahl der Lebenspunkte
       self.name = "Minotaurus"
       self.strength = 40 #Stärke zeigt wie viel Schaden der Gegner macht
       self.dodgechance = 0 #Zeigt eine mögliche Ausweich-Chance 1 = 10% um auszuweichen, 4 = 40% etc
       self.critchance = 3 #Zeigt Chancen auf kritische Treffer 1 = 10% um auszuweichen, 4 = 40% etc
 
class Boss():
    def __init__(self):
        self.name = ""
        self.hitpoints = 0
        self.maxhp = 0
        self.strength = 0
        self.dodgechance = 0
        self.critchance = 0
 
 
    def mini_boss_schwarzer_ritter(self):
        self.name = "Schwarzer Rosenritter"
        self.hitpoints = 250
        self.maxhp = 250
        self.strength = 55
        self.dodgechance = 2
        self.critchance = 4

    def final_boss_rosenkoenigen_rosamira(self):
        self.name = "Rosenkönigin Rosamira"
        self.hitpoints = 350
        self.maxhp = 350
        self.strength = 60
        self.dodgechance = 10
        self.critchance = 20