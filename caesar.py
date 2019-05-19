from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
#encrypts full strings of text by returning each character "rot" places
#to the right of each character in the text in alphabetical order 
    result = ""
    for char in text:
        result += rotate_character(char, rot)
    return result
    
def main():
    text = input("Type a message: ")
    rot = int(input("Rotate by: "))
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()
