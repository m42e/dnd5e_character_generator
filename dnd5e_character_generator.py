from random import randint

class Player:
    def  __init__(self):
        self.name = None
        self.className = None
        self.str = None
        self.dex = None
        self.con = None
        self.int = None
        self.wis = None
        self.cha = None

def best_of_4d6():
    rolls = [randint(1,6), randint(1,6), randint(1,6), randint(1,6)]
    rolls.remove(min(rolls))
    return sum(rolls)

def random_abil():
    n1 = best_of_4d6()
    n2 = best_of_4d6()
    n3 = best_of_4d6()
    n4 = best_of_4d6()
    n5 = best_of_4d6()
    n6 = best_of_4d6()
    abil = [n1, n2, n3, n4, n5, n6]
    abil.sort(reverse = True)
    print("You rolled the following scores: " + str(abil))
    return abil

def predef_abil():
    abil = [15, 14, 13, 12, 10, 8]
    print("You have the following scores to place as you please: " + str(abil))
    return abil

def custom_abil():
    new_player.str = input("What is your strength: ")
    new_player.dex = input("What is your dexterity: ")
    new_player.con = input("What is your constitution: ")
    new_player.int = input("What is your intelligence: ")
    new_player.wis = input("What is your wisdom: ")
    new_player.cha = input("What is your charisma: ")

def abil_input(abil):
    picked = []
    while(len(picked) < 6):
        choice = input("Will " + str(abil[len(picked)]) + " be your (S)trength, (D)exterity, (C)onstitution, (I)ntelligence, (W)isdom, or (Ch)arisma: ").upper()
        if choice == 'S' and choice not in picked: 
            new_player.str = abil[len(picked)]
            picked.append('S')
        elif choice == 'D' and choice not in picked:     
            new_player.dex = abil[len(picked)]
            picked.append('D')
        elif choice == 'C' and choice not in picked: 
            new_player.con = abil[len(picked)]
            picked.append('C')
        elif choice == 'I' and choice not in picked: 
            new_player.int = abil[len(picked)]
            picked.append('I')
        elif choice == 'W' and choice not in picked: 
            new_player.wis = abil[len(picked)]
            picked.append('W')
        elif choice == 'CH' and choice not in picked: 
            new_player.cha = abil[len(picked)]
            picked.append('CH')
        else: print("Invalid option")

def abil_menu():
    while True:
        choice = input("How would you like to determine your ability scores? (R)andom, (P)redetermined, (C)ustom: ").upper()
        if choice == 'R':
            abil_input(random_abil())
            break;
        elif choice == 'P':
            abil_input(predef_abil())
            break;
        elif choice == 'C': 
            custom_abil()
            break;
        else: print("Invalid option")

def add_distinct(lst):
    for word in lst:
        if word not in new_player.prof:
            new_player.prof.append(word)

def main():
    print("Welcome to the basic Dungeons and Dragons 5e character generator!")
    new_player.name = input("What is your new character's name: ")
    print(new_player.name)
    abil_menu()

new_player = Player()

if __name__ == "__main__":
    main()