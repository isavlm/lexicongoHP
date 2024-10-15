import random

# List of vowels and consonants
vowels = list("AEIOU" * 4)  # 4 of each vowel
consonants = list("BCDFGHJKLMNPQRSTVWXYZ" * 4)  # 4 of each consonant

# Special tiles
special_tiles = ['Bludger', 'Knight Bus', 'Wit Potion']

# Combine all tiles together
tiles = vowels + consonants + special_tiles
random.shuffle(tiles)

STARTING_TILES = 10  # Number of tiles to deal to each player
MAX_TILES = 15  # Max number of tiles per player

# Function to deal tiles ensuring at least 2 vowels per player
def deal_tiles(tiles, num_players):
    players = {f'Player {i+1}': [] for i in range(num_players)}
    
    # Deal 2 vowels to each player first
    for player in players:
        for _ in range(2):
            vowel = random.choice(vowels)
            players[player].append(vowel)
            vowels.remove(vowel)

    # Deal remaining tiles
    for _ in range(STARTING_TILES - 2):
        for player in players:
            tile = tiles.pop()
            players[player].append(tile)
    
    return players

# Check if tiles can form a valid word
def can_form_word(tiles):
    for word in valid_words:
        if all(tiles.count(letter) >= word.count(letter) for letter in word):
            return True  # Can form at least one valid word
    return False

# Display instructions
def display_instructions():
    print("""
    Welcome to Lexicon Go! Harry Potter Edition

    - You will be dealt 10 tiles.
    - The computer will try to form words using its tiles.
    - You can form words or skip your turn.
    - You can type 'Tile' to draw a new tile during your turn.
    - Type 'END' to end the game.

    Press ENTER to return to the menu.
    """)

# Menu
def menu():
    while True:
        print("===== LEXICON GO! HARRY POTTER =====")
        print("1. Start Game")
        print("2. Instructions")
        print("3. Quit")
        
        choice = input("Select an option: ")

        if choice == '1':
            # Start the game with the player and computer
            players_tiles = deal_tiles(tiles, 2)  # 2 players: human and computer
            game_loop(players_tiles, tiles)
        elif choice == '2':
            display_instructions()
            input()
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid option, please try again.")

# Valid words
valid_words = {
    "HOGWARTS", "POTTER", "SNAPE", "DRACO", "DOBBY", "WANDS", "BROOM", "WEASEL", "RIDDLE", 
    "HORCRUX", "MUGGLE", "NIMBUS", "LUPIN", "HEDWIG", "MOODY", "GOBLET", "PHOENIX", "TONKS", 
    "ALBUS", "PERCY", "FAWKES", "DURSLEY", "NEVILLE", "DUDLEY", "DEMENTOR", "AZKABAN", "GRANGER", 
    "QUIDDITCH", "SLYTHERIN", "GRYFFINDOR", "HAGRID", "OLLIVANDER", "BELLATRIX", "MALFOY", 
    "ERISED", "CROOKSHANKS", "REMUS", "MCGONAGALL", "SIRIUS", "PATRONUS", "DIAGON", "GRINGOTTS", 
    "HOGSMEADE", "FLITWICK", "SLUGHORN", "MANDRAKE", "FELIX", "AMORTENTIA", "POLYJUICE", 
    "VERITASERUM", "IMPERIUS", "CRUCIATUS", "AVADA", "SECTUMSEMPRA", "LUMOS", "NOX", "ACCIO", 
    "ALOHOMORA", "EXPELLIARMUS", "EXPECTO", "PROTEGO", "LEGILIMENS", "APPARATE", "OBLIVIATE", 
    "ANIMAGUS", "PENSIEVE", "BEZOAR", "THESTRAL", "ACROMANTULA", "HIPPOGRIFF", "CENTAUR", 
    "MERPEOPLE", "VEELA", "RAVENCLAW", "HUFFLEPUFF", "BASILISK", "SEEKER", "KEEPER", "BEATER", 
    "CHASER", "GALLEON", "PORTKEY", "WEREWOLF", "FLOO", "GRINDELWALD", "DARK","LORD", "CUP", "DIADEM", 
    "DIARY" "STONE","RING", "LOCKET", "CLOAK", "SCAR", "PHILOSOPHER", "SORCERER", "HALLOWS", "ELDER",
    "FIREBOLT", "QUIRRELL", "KRUM", "BUCKBEAK", "WORMTAIL", "VOLDEMORT", "HORNTAIL", "BASILISK", 
    "GRIPHOOK", "PEVERELL", "FIREWHISKY", "SWORD", "SORTING", "HAT", "MIRROR", "ELF", "GOBLIN",
    "WAND", "NEWT", "FIGG", "SNITCH", "BUTTERBEER", "PUMPKIN"
}


# Function to check if words are valid
def is_valid_word(word):
    return word in valid_words

# Function with the logic to play a turn for a player human or computer.

# Unified turn logic for both human and computer
# Unified turn logic for both human and computer, with special tile handling and SNITCH rule
def play_turn(player, player_tiles, game_tiles, is_computer=False):
    print(f"{player}'s tiles: {' '.join(player_tiles)}")
    
    if is_computer:
        # Check for special tiles and use them
        if 'Bludger' in player_tiles:
            print("Computer used Bludger! Skips the player's next turn.")
            player_tiles.remove('Bludger')
            return 'BLUDGER'
        elif 'Knight Bus' in player_tiles:
            print("Computer used Knight Bus! Shuffles its tiles.")
            random.shuffle(player_tiles)
            player_tiles.remove('Knight Bus')
            return 'KNIGHT BUS'
        elif 'Wit Potion' in player_tiles:
            print("Computer used Wit Potion! Swaps tiles with the player.")
            player_tiles, game_tiles = game_tiles, player_tiles
            player_tiles.remove('Wit Potion')
            return 'WIT POTION'

        # Automatically form the first valid word if possible
        if can_form_word(player_tiles):
            for word in valid_words:
                if all(player_tiles.count(letter) >= word.count(letter) for letter in word):
                    if word == 'SNITCH':  # Check if the computer forms "SNITCH"
                        print("Computer formed SNITCH and wins the game!")
                        return 'SNITCH'
                    print(f"Computer forms the word: {word}")
                    for letter in word:
                        player_tiles.remove(letter)
                    return True
        else:
            # If no valid word, draw a new tile if possible
            if len(player_tiles) < MAX_TILES:
                new_tile = game_tiles.pop()
                player_tiles.append(new_tile)
                print(f"Computer draws a new tile: {new_tile}")
            else:
                print("Computer skips the turn.")
            return False
    
    # Human player's turn
    while True:
        action = input("Form a word, type 'Tile' to draw a new tile, 'SKIP' to skip, 'BLUDGER' for Bludger, 'KNIGHT BUS' for Knight Bus, 'WIT POTION' for Wit Potion, or 'END' to end the game: ").upper()
        
        # Handle special tiles for the human player
        if action == 'BLUDGER' and 'Bludger' in player_tiles:
            print(f"{player} used Bludger! Skips the opponent's next turn.")
            player_tiles.remove('Bludger')
            return 'BLUDGER'
        elif action == 'KNIGHT BUS' and 'Knight Bus' in player_tiles:
            print(f"{player} used Knight Bus! Shuffles your tiles.")
            random.shuffle(player_tiles)
            player_tiles.remove('Knight Bus')
            return 'KNIGHT BUS'
        elif action == 'WIT POTION' and 'Wit Potion' in player_tiles:
            print(f"{player} used Wit Potion! Swaps your tiles with the game pool.")
            player_tiles, game_tiles = game_tiles, player_tiles
            player_tiles.remove('Wit Potion')
            return 'WIT POTION'
        elif action == 'TILE':
            if len(player_tiles) < MAX_TILES:
                new_tile = game_tiles.pop()  # Draw a new tile from the game pool
                player_tiles.append(new_tile)  # Add it to the player's tile list
                print(f"{player} drew a new tile: {new_tile}")
                print(f"Your updated tiles: {' '.join(player_tiles)}")
            else:
                print(f"Cannot draw more tiles. {player} already has {MAX_TLES} tiles.")
        elif action == 'SKIP':
            print(f"{player} skips the turn.")
            return False
        elif action == 'END':
            print(f"{player} ended the game.")
            return 'END'
        elif is_valid_word(action):
            if action == 'SNITCH':  # Check if the player forms "SNITCH"
                print(f"{player} formed SNITCH and wins the game!")
                return 'SNITCH'
            print(f"{action} is valid!")
            for letter in action:
                if letter in player_tiles:
                    player_tiles.remove(letter)
            return True
        else:
            print(f"{action} is not valid! Try again or type 'Tile' to draw a new tile.")


# Game Loop
def game_loop(players, game_tiles):
    computer_player = 'Player 2'
    
    while True:
        for player, player_tiles in players.items():
            if not player_tiles:
                print(f"{player} wins!")
                return

            if player == computer_player:
                print(f"\nIt's the computer's turn!")
                turn_result = play_turn(player, player_tiles, game_tiles, is_computer=True)
            else:
                print(f"\nIt's {player}'s turn!")
                turn_result = play_turn(player, player_tiles, game_tiles)
                
            if turn_result == 'SNITCH':
                print(f"{player} wins by forming SNITCH!")
                return
            elif turn_result == 'END':
                print(f"{player} ended the game.")
                return
                
            if turn_result and game_tiles:
                player_tiles.append(game_tiles.pop())
            
            print(f"{player}'s tiles: {' '.join(player_tiles)}")
            print()  # Add space between turns


# Run the menu
menu()