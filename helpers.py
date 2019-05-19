alphabet = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):
#returns the numerical index of a letter in the alphabet, 0-25
    for i in range(len(alphabet)):
        if alphabet[i] == letter.lower():
            return i

def rotate_character(char, rot):
#returns the letter "rot" places to the right of "char" in the alphabet
#if char is not an alphabetical character, just char is returned
    if not char.isalpha():
        return char
    char_index = alphabet_position(char)
    rot_index = (char_index + rot) % 26
    if char.isupper() == True:
        return alphabet[rot_index].upper()
    return alphabet[rot_index]
