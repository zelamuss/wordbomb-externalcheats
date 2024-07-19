import pyautogui
import keyboard

def load_wordlist(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
        print(f"Wordlist loaded. Total words: {len(words)}")
        return words
    except FileNotFoundError:
        print("Wordlist file not found.")
        return []

def find_longest_matching_word(wordlist, combination):
    matching_words = [word for word in wordlist if combination.lower() in word.lower()] 
    if matching_words:
        longest_word = max(matching_words, key=len)
        return longest_word
    return None

def type_word(word, typing_speed=0.05):
    pyautogui.typewrite(word, interval=typing_speed)

def on_f4_pressed(combination, wordlist):
    longest_word = find_longest_matching_word(wordlist, combination)
    if longest_word:
        print(f"Typing word: {longest_word}")
        type_word(longest_word)

def main():
    hotkey_function = None
    hotkey_added = False
    
    while True:
        combination = input("Please enter the letters thats given to you (Example:NU)").lower() 
        if combination == 'q':
            break
        
        wordlist = load_wordlist('wordlist.txt')
        
        if wordlist:
            print("Word found.You can press F4 whenever you like to type it")
            
            # If didnt add hotkey
            if not hotkey_added:
                hotkey_function = lambda: on_f4_pressed(combination, wordlist)
                keyboard.add_hotkey('f4', hotkey_function)
                hotkey_added = True
            
            
            # Wait while hotkey
            keyboard.wait('f4')
        
        else:
            print("Wordlist failed to load.Exiting")

    # Remove the hotkey when exit
    if hotkey_added:
        keyboard.remove_hotkey('f4', hotkey_function)

if __name__ == "__main__":
    main()
