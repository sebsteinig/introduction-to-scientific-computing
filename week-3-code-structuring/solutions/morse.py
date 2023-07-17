# letters to morse code
letter_to_morse = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
    'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
    'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
    'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
    '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
    '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
}


def encode(message):
    morse = []

    for letter in message:
        letter = letter.lower()
        morse_letter = letter_to_morse[letter]
        morse.append(morse_letter)

    morse_message = " ".join(morse)
    
    return morse_message

# morse code to letters
morse_to_letter = {}
for letter in letter_to_morse:
    morse = letter_to_morse[letter]
    morse_to_letter[morse] = letter


def decode(message):
    english = []

    # Now we cannot read by letter. We know that morse letters are
    # separated by a space, so we split the morse string by spaces
    morse_letters = message.split(" ")

    for letter in morse_letters:
        english_letter = morse_to_letter[letter]
        english.append(english_letter)

    # Rejoin, but now we don't need to add any spaces
    english_message = "".join(english)
    
    return english_message