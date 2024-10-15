def can_make_word(word, letters):
    letter_count = {}
    
    # Count the occurrence of each letter in the list
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    
    # Check if we can form the word with the available letters
    for char in word:
        if char not in letter_count or letter_count[char] == 0:
            return False
        letter_count[char] -= 1
    
    return True

def find_valid_words(letters):
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
        "CHASER", "GALLEON", "PORTKEY", "WEREWOLF", "FLOO", "GRINDELWALD", "DARK", "LORD", "CUP", 
        "DIADEM", "DIARY", "STONE", "RING", "LOCKET", "CLOAK", "SCAR", "PHILOSOPHER", "SORCERER", 
        "HALLOWS", "ELDER", "FIREBOLT", "QUIRRELL", "KRUM", "BUCKBEAK", "WORMTAIL", "VOLDEMORT", 
        "HORNTAIL", "BASILISK", "GRIPHOOK", "PEVERELL", "FIREWHISKY", "SWORD", "SORTING", "HAT", 
        "MIRROR", "ELF", "GOBLIN", "WAND", "NEWT", "FIGG", "SNITCH", "BUTTERBEER", "PUMPKIN"
    }
    
    possible_words = []
    
    # Check which valid words can be made with the input letters
    for word in valid_words:
        if can_make_word(word, letters):
            possible_words.append(word)
    
    return possible_words

def main():
    while True:
        # Input: list of letters from the user
        user_input = input("Enter letters separated by spaces: ").upper().split()
        
        # Find and display the valid words
        valid_words = find_valid_words(user_input)
        
        if valid_words:
            print("Words you can make:", valid_words)
        else:
            print(f"No words can be made with the letters {user_input}.")
        
        # Ask if the user wants to try again
        try_again = input("Would you like to try again? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Goodbye!")
            break

# Run the main function
main()
