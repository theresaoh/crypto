from helpers import alphabet_position, rotate_character

def encrypt(text, key):
###encrypts full strings of text by returning each character "rot" places
###to the right of each character in the text in alphabetical order 
    result = ""
    text_iterator = 0
    key_iterator = 0
    key_char_list = []
    for keychar in key:
        key_char_list.append(keychar)     
    while text_iterator <= len(text) - 1:
        letter_in_key = key_char_list[key_iterator]
        #print("current key letter: ", letter_in_key, "rotation: ", alphabet_position(letter_in_key), "result: ", result)
        result += rotate_character(text[text_iterator], alphabet_position(letter_in_key))
        if rotate_character(text[text_iterator], 1) == text[text_iterator]:
            text_iterator += 1
            continue
        text_iterator += 1
        key_iterator += 1
        if key_iterator == len(key_char_list):
            key_iterator = 0
            continue
    return result
    
def main():
    text = input("Type a message: ")
    key = input("Encryption key: ")
    print(encrypt(text, key))

if __name__ == "__main__":
    main()

