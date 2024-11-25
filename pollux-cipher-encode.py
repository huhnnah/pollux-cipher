import random

MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', 
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.'
}

DOTS   = ['0', '4', '7']
DASHES = ['1', '5', '8']
SPACES = ['2', '3', '6', '9']

def encode_to_morse(plaintext):
    morse_code = []
    
    for char in plaintext.upper():
        if char in MORSE_CODE:
            morse_code.append(MORSE_CODE[char])
        elif char == ' ':
            morse_code.append('')
    
    return ' '.join(morse_code)

def decode_morse(morse_code):
    decoded_text = []
    codes = morse_code.split(' ')
    
    for code in codes:
        if code in MORSE_CODE.values():
            decoded_text.append(next(key for key, value in MORSE_CODE.items() if value == code))
        else:
            decoded_text.append(' ')
    
    return ''.join(decoded_text)

def pollux_encode(morse_code):
    encoded_text = []
    
    for char in morse_code:
        if char == '.':
            encoded_text.append(random.choice(DOTS))
        elif char == '-':
            encoded_text.append(random.choice(DASHES))
        elif char == ' ':
            encoded_text.append(random.choice(SPACES))
    
    return ''.join(encoded_text)

def pollux_decode(encoded_text):
    decoded_morse = []
    
    for char in encoded_text:
        if char in DOTS:
            decoded_morse.append('.')
        elif char in DASHES:
            decoded_morse.append('-')
        elif char in SPACES:
            decoded_morse.append(' ')
    
    return ''.join(decoded_morse)

def pollux_cipher(plaintext):
    if not all(c.isalnum() or c.isspace() for c in plaintext) or plaintext.startswith(' '):
        raise ValueError("Input must contain only letters and numbers, and cannot start with a space.")
    
    morse_code = encode_to_morse(plaintext)
    encoded_text = pollux_encode(morse_code)
    
    return encoded_text

try:
    plaintext = "hannah ramos 09"
    encoded_text = pollux_cipher(plaintext)
    
    print("=" * 80)
    print(f"{'POLLUX CIPHER ENCODE':^80}") 
    print("=" * 80)
    print(f"{'Test String:':<20} {plaintext}")
    print(f"{'Encrypted Text:':<20} {encoded_text}")
    print("=" * 80)
except ValueError as e:
    print("Error:", e)