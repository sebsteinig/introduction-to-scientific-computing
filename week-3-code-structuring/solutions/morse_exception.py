letter_to_morse = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
    'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
}


def encode(message):
    if "!" in message:                                            # ← new code
        raise ValueError(f"'!' is not valid in English strings")  # ←
    
    morse = []

    for letter in message:
        letter = letter.lower()
        morse_letter = letter_to_morse[letter]
        morse.append(morse_letter)

    morse_message = " ".join(morse)
    
    return morse_message


# We need to invert the dictionary. This will create a dictionary
# that can go from the morse back to the letter
morse_to_letter = {}
for letter in letter_to_morse:
    morse = letter_to_morse[letter]
    morse_to_letter[morse] = letter


def decode(message):
    english = []

    morse_letters = message.split(" ")

    for letter in morse_letters:
        english_letter = morse_to_letter[letter]
        english.append(english_letter)

    english_message = "".join(english)
    
    return english_message