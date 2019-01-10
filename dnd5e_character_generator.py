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

def main():
    print("Welcome to the basic Dungeons and Dragons 5e character generator!")
    new_player = Player()
    new_player.name = input("What is your new character's name: ")
    print(new_player.name)

if __name__ == "__main__":
    main()