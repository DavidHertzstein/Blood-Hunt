#Programmiert von David zusammen mit Andre, Edward und Abdul
import pygame
import time
import sys
import random
import os
from enemy import Enemies, Boss #Boss Klasse erstellt von David
from hero import Hero, Weapon, Items


#Globale Variablen
held = None
waffe = None
items = Items()
shield = 0


#Text für langsame ausgabe

def langsamer_text(text, delay=0.03):
   
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def bildschirm_loeschen():
   
    os.system('cls' if os.name == 'nt' else 'clear')



#Menü 


def main_menu():
    """Hauptmenü des Spiels"""
    pygame.mixer.music.load("Projekt/mixkit-tapis-615.mp3")
    pygame.mixer.music.play(-1)
    
    while True:
        print("====================================================================")
        print("                         BLOOD HUNT")
        print("                  GARDENS OF BLOOD AND ROSES")
        print("====================================================================")
        print("1. Starten")
        print("2. Anleitung")
        print("3. Beenden")
        print("====================================================================")
 
        wahl = input("Wähle eine Option aus von (1-3): ")
        
        if wahl == "1":
            starte_spiel()
            break
        elif wahl == "2":
            anleitung()
        elif wahl == "3":
            langsamer_text("Spiel wird beendet!!")
            pygame.quit()
            sys.exit()
        else:
            print("Ungültige Angabe")


def anleitung():
    """Zeigt die Spielanleitung"""
    print("\n=== Anleitung ===\n")
    print("- Kämpfe gegen Gegner mit 3 verschiedenen Angriffen:")
    print("- Normal-Angriff: Kein Mana, mittlerer Schaden")
    print("- Special-Angriff: Kostet Mana, hoher Schaden")
    print("- Ultimate-Angriff: Kostet viel Mana, massiver Schaden")
    print("- Verteidigung: Blockt Schaden mit deiner Rüstung")
    print("- Items: Nutze Heiltränke um HP wiederherzustellen")
    print("- Besiege die Rosenkönigin!\n")
    input("Drücke ENTER-Taste für zurück.\n")



#Story und Charaktererstellung


def starte_spiel():
    
    pygame.mixer.music.stop()
    
    langsamer_text("Aria... einst eine friedliche Stadt voller Musik und Blumen.")
    langsamer_text("Doch diese Zeiten sind vorbei.")
    langsamer_text("Ein süßer, unheilvoller Rosenduft liegt über den Straßen.")
    langsamer_text("Menschen verschwinden und wer zurückkehrt, ist von Dornen umhüllt.")
    langsamer_text("Die Finstere Rosenkönigin Rosamira hat ihr Dornenschloss über das Land ausgebreitet.")
    langsamer_text("Lebende Ranken wuchern durch die Stadt, verwandeln Menschen in Kreaturen.")
    langsamer_text("\nDu bist der letzte Überlebende")
    langsamer_text("\nDeine Mission:")
    langsamer_text(" - Die Stadt Aria retten")
    langsamer_text(" - Die Dornen vernichten")
    langsamer_text(" - Die Rosenkönigin töten\n")
    langsamer_text("Das Schicksal der Menschheit liegt in deinen Händen... Bitte... \nrette uns...\n")
    
    charakterauswahl()


def charakterauswahl():
   
    global held, waffe
    
    pygame.mixer.music.load("Projekt/intense-rain-city-night-171461.mp3")
    pygame.mixer.music.play(-1)
    
    langsamer_text("Du bist da... Du siehst nichts...")
    langsamer_text("Das Einzige was du hörst, ist der Klang des Regens..")
    langsamer_text("Du weißt nicht mehr wer du bist..")
    langsamer_text("Doch du kannst dich erinnern was du bist..")
    
    #Charakterwahl
    while True:
        charakterwahl = input("\nAlso was bist du?? Gib ein (Krieger, Magier, Assasine): ").strip()
        
        if charakterwahl.lower() in ["krieger", "magier", "assasine"]:
            break
        
        print("Ungültige Klasse! Wähle: Krieger, Magier oder Assasine")
    
    #Held wird erstellt
    held = Hero(name="Held", klasse=charakterwahl)
    
    #Waffe wird erstellt
    waffe = Weapon()
    if charakterwahl.lower() == "krieger":
        waffe.krieger_waffe()
    elif charakterwahl.lower() == "magier":
        waffe.magier_waffe()
    elif charakterwahl.lower() == "assasine":
        waffe.assasine_waffe()
    
    #Werte anzeigen
    bildschirm_loeschen()
    langsamer_text(f"So mein {charakterwahl}, WACH AUF!!!!")
    langsamer_text(f"\n=== DEINE WERTE ===")
    langsamer_text(f"Klasse: {held.klasse}")
    langsamer_text(f"HP: {held.hitpoints}/{held.maxhp}")
    langsamer_text(f"MP: {held.magicpoints}/{held.maxmp}")
    langsamer_text(f"Stärke: {held.strength}")
    langsamer_text(f"Rüstung: {held.armor}")
    langsamer_text(f"Geschicklichkeit: {held.dexterity}")
    langsamer_text(f"Ausweichchance: {held.dodgechance}%")
    langsamer_text(f"\nWaffe: {waffe.name}")
    langsamer_text(f"Normal-Angriff: {waffe.classic_atk} Schaden")
    langsamer_text(f"Special-Angriff: {waffe.special_atk} Schaden ({waffe.attack_special_manacost} MP)")
    langsamer_text(f"Ultimate-Angriff: {waffe.ultimate_atk} Schaden ({waffe.attack_ultimate_manacost} MP)\n")
    
    input("Drücke ENTER um fortzufahren...")
    stage3(held)



#Kampflogik


def kampf(held, gegner, gegner_name):
    
    global shield, waffe, items
    
    bildschirm_loeschen()
    print("="*60)
    langsamer_text(f"Ein {gegner_name} erscheint!")
    print("="*60)
    time.sleep(1)
    
    #Schleife des Kampfsystems
    while held.hitpoints > 0 and gegner.hitpoints > 0:
        
        #Status anzeigen
        print(f"\n{'='*50}")
        print(f"|Du: {held.hitpoints}/{held.maxhp} HP | {held.magicpoints}/{held.maxmp} MP |")
        print(f"|Gegner {gegner_name}: {gegner.hitpoints} HP |")
        print(f"|Nächster Gegner-Schaden: {max(0, gegner.strength - held.armor)} |")
        print(f"{'='*50}")
        
        #Aktion wählen
        zug = input("\n(1) Angreifen, (2) Verteidigen, (3) Heiltrank: ").strip()
        
        #Angriff
        if zug == "1":
            bildschirm_loeschen()
            print(f"\n|Du: {held.hitpoints}/{held.maxhp} HP | {held.magicpoints}/{held.maxmp} MP |")
            print(f"|Gegner {gegner_name}: {gegner.hitpoints} HP |\n")
            
            attack_type = input(f"Wähle Angriff:\n| 1. Normal ({waffe.classic_atk} DMG) | 2. Special ({waffe.special_atk} DMG, {waffe.attack_special_manacost} MP) | 3. Ultimate ({waffe.ultimate_atk} DMG, {waffe.attack_ultimate_manacost} MP) |\nEingabe: ").strip()
            
            damage = 0
            ist_krit = False
            
            #Normal-Angriff
            if attack_type == "1":
                if random.randint(1, 100) <= held.dexterity * 2:
                    damage = waffe.classic_atk * 2
                    ist_krit = True
                else:
                    damage = waffe.classic_atk
                held.magicpoints += 10
                
            #Special-Angriff
            elif attack_type == "2":
                if held.magicpoints >= waffe.attack_special_manacost:
                    if random.randint(1, 100) <= held.dexterity * 2:
                        damage = waffe.special_atk * 2
                        ist_krit = True
                    else:
                        damage = waffe.special_atk
                    held.magicpoints -= waffe.attack_special_manacost
                else:
                    langsamer_text("Nicht genug MP! Normal-Angriff wird ausgeführt.")
                    damage = waffe.classic_atk
                    held.magicpoints += 10
                    
            #Ultimate-Angriff
            elif attack_type == "3":
                if held.magicpoints >= waffe.attack_ultimate_manacost:
                    if random.randint(1, 100) <= held.dexterity * 2:
                        damage = waffe.ultimate_atk * 2
                        ist_krit = True
                    else:
                        damage = waffe.ultimate_atk
                    held.magicpoints -= waffe.attack_ultimate_manacost
                else:
                    langsamer_text("Nicht genug MP! Normal-Angriff wird ausgeführt.")
                    damage = waffe.classic_atk
                    held.magicpoints += 10
            else:
                langsamer_text(f"Ungültige Eingabe! Der Gegner erhält einen freien Angriff")
                damage = waffe.a
                held.magicpoints += 10
            
            #MP begrenzen
            if held.magicpoints > held.maxmp:
                held.magicpoints = held.maxmp
            
            #Prüfe Gegner-Ausweichen
            if random.randint(1, 100) <= gegner.dodgechance * 10:
                bildschirm_loeschen()
                print("="*50)
                print("| GEGNER AUSGEWICHEN! |")
                print("="*50)
                print(f"Der {gegner_name} hat deinen Angriff ausgewichen!")
            else:
                gegner.hitpoints -= damage
                bildschirm_loeschen()
                
                if ist_krit:
                    print("="*50)
                    print("| KRITISCHER TREFFER! |")
                    print("="*50)
                    print(f"Du hast {damage} Schaden verursacht! (KRIT)")
                else:
                    print(f"Du hast {damage} Schaden verursacht!")
                
                print(f"Gegner HP: {gegner.hitpoints}")
            
            time.sleep(1.5)
        
        #Verteidigung 
        elif zug == "2":
            bildschirm_loeschen()
            shield = held.armor
            held.magicpoints += 10
            if held.magicpoints > held.maxmp:
                held.magicpoints = held.maxmp
            print(f"Du verteidigst dich! Shield: {shield} | +10 MP")
            time.sleep(1)
        
        #Heiltrank
        elif zug == "3":
            bildschirm_loeschen()
            alter_hp = held.hitpoints
            held.hitpoints += items.health_potion_healing
            if held.hitpoints > held.maxhp:
                held.hitpoints = held.maxhp
            geheilt = held.hitpoints - alter_hp
            held.magicpoints += 10
            if held.magicpoints > held.maxmp:
                held.magicpoints = held.maxmp
            print(f"Du benutzt einen Heiltrank und heilst {geheilt} HP!")
            print(f"Deine HP: {held.hitpoints}/{held.maxhp}")
            time.sleep(1)
        
        else:
            bildschirm_loeschen()
            print("Ungültige Eingabe! Der Gegner greift an!")
            time.sleep(1)
        
        #Gegner-Angriff
        if gegner.hitpoints > 0:
            #Prüfe Held-Ausweichen
            if random.randint(1, 100) <= held.dodgechance:
                print("="*50)
                print("| DU BIST AUSGEWICHEN! |")
                print("="*50)
                print(f"Du hast dem Angriff des {gegner_name} ausgewichen!")
            else:
                #Prüfe Gegner-Krit
                if random.randint(1, 100) <= gegner.critchance * 10:
                    enemy_damage = max(0, (gegner.strength * 2) - held.armor - shield)
                    held.hitpoints -= enemy_damage
                    print("="*50)
                    print(f"| DER {gegner_name.upper()} HAT KRITISCH GETROFFEN! |")
                    print("="*50)
                    print(f"Du erleidest {enemy_damage} Schaden! (KRIT)")
                else:
                    enemy_damage = max(0, gegner.strength - held.armor - shield)
                    held.hitpoints -= enemy_damage
                    print(f"Der {gegner_name} greift an und verursacht {enemy_damage} Schaden!")
                
                shield = 0
            
            time.sleep(1.5)
        
        #Prüfe Kampfende
        if gegner.hitpoints <= 0:
            bildschirm_loeschen()
            print("="*60)
            print(f"*** DU HAST {gegner_name.upper()} BESIEGT! ***")
            print("="*60)
            
            #Belohnung
            held.hitpoints += 15
            held.magicpoints += 10
            if held.hitpoints > held.maxhp:
                held.hitpoints = held.maxhp
            if held.magicpoints > held.maxmp:
                held.magicpoints = held.maxmp
            
            print(f"Du erhältst +15 HP und +10 MP!")
            print(f"Deine Stats: {held.hitpoints}/{held.maxhp} HP | {held.magicpoints}/{held.maxmp} MP")
            time.sleep(2)
            return True
        #Wenn verloren
        if held.hitpoints <= 0:
            bildschirm_loeschen()
            print("="*60)
            print("*** DU WURDEST BESIEGT! ***")
            print("="*60)
            return False
    
    return held.hitpoints > 0



#Stage 3 - Wellensystem


def stage3(held):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Projekt/Stage3 music.mp3")
    pygame.mixer.music.play(-1)
    langsamer_text("\nDu steigst die Treppen hinauf..")
    langsamer_text("Als du oben angekommen bist, bemerkst du, dass du")
    langsamer_text("in die Gemächer der Königin gelangt bist.")
    langsamer_text("Dein Ziel ist ganz nah, gib nicht auf!!!!\n")
    
    input("Drücke ENTER um fortzufahren...")
    
    aktuelleWelle = 1
    
    while aktuelleWelle <= 10:
        bildschirm_loeschen()
        print("*"*60)
        print(f"*** WELLE {aktuelleWelle} VON 10 ***")
        print("*"*60)
        time.sleep(1)
        
        #Welle 9: Miniboss
        if aktuelleWelle == 9:
            miniboss = Boss()
            miniboss.mini_boss_schwarzer_ritter()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Projekt/operational-focus-fast-thrash-metal-instrumental-391329.mp3")
            pygame.mixer.music.play(-1)
            print("\n" + "="*60)
            langsamer_text("Ein schwarzer Ritter erscheint vor dem Tor")
            langsamer_text("der Rosenkönigin!")
            print("="*60)
            langsamer_text('"Du bist weit gekommen, Held..."')
            langsamer_text('"Aber hier endet dein Weg!!"')
            langsamer_text('"Ich lasse nicht zu, dass du meine Rosenkönigin tötest!!"\n')
            time.sleep(1)
            
            erfolgreich = kampf(held, miniboss, miniboss.name)
        
        # Welle10: Final Boss
        elif aktuelleWelle == 10:
            finalBoss = Boss()
            finalBoss.final_boss_rosenkoenigen_rosamira()
            pygame.mixer.music.stop()
            pygame.mixer.music.load("Projekt/Aufzeichnung 2025-12-04 162218.mp3")
            pygame.mixer.music.play(-1)
            print("\n" + "="*60)
            langsamer_text("Du erreichst den Thronsaal der Rosenkönigin")
            print("="*60)
            langsamer_text("Eine majestätische Gestalt erhebt sich vom Thron...")
            langsamer_text('"So... ein Sterblicher wagt es?"')
            langsamer_text('"Deine Reise endet hier!"\n')
            time.sleep(1)
            
            erfolgreich = kampf(held, finalBoss, finalBoss.name)
            
            # Nach Final Boss: Ende
            if erfolgreich:
                bildschirm_loeschen()
                pygame.mixer.music.stop()
                pygame.mixer.music.load("ghost-moon-lullaby-304719.mp3")
                pygame.mixer.music.play(-1)
                print("="*70)
                print("         DU HAST DIE ROSENKÖNIGIN BESIEGT!")
                print("="*70)
                langsamer_text("\nDie Dornen verschwinden...")
                langsamer_text("Die Stadt Aria ist gerettet!")
                langsamer_text("\n*** DANKE FÜR'S SPIELEN! ***")
                return True
        
        #Normale Wellen (1-8)
        else:
            gegner = Enemies()
            zufallgegner = random.choice([1, 2, 3])
            
            if zufallgegner == 1:
                gegner.enemy_dracula()
                name = "Dracula"
            elif zufallgegner == 2:
                gegner.enemy_rosen_kreuz_ritter()
                name = "Rosenkreuzritter"
            else:
                gegner.enemy_minotaurus()
                name = "Minotaurus"
            
            erfolgreich = kampf(held, gegner, name)
        
        #Prüfe ob Held gestorben ist
        if not erfolgreich:
            langsamer_text("\nDu bist gefallen...")
            langsamer_text("GAME OVER")
            return False
        
        #Welle überlebt
        bildschirm_loeschen()
        langsamer_text(f"*** WELLE {aktuelleWelle} ÜBERLEBT! ***\n")
        time.sleep(1)
        
        aktuelleWelle += 1
    
    return True



#Programm-Start


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    main_menu()

