MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ', ': '--..--',
    '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-'
}

def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter.upper()] + " "
        else:
            cipher += " "
    return cipher

def decrypt(message):
    message += " "
    decipher = ""
    citext = ""
    space_count = 0

    for letter in message:
        if letter != " ":
            space_count = 0
            citext += letter
        else:
            space_count += 1
            if space_count == 2:  # Two spaces indicate a new word
                decipher += " "
            elif citext:  # Decode the current Morse code
                for key, value in MORSE_CODE_DICT.items():
                    if citext == value:
                        decipher += key
                        break
                citext = ""

    return decipher


if __name__ == "__main__":
    message = "INDER SHARMA"
    encrypted_message = encrypt(message)
    print(f"Encrypted: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message)
    print(f"Decrypted: {decrypted_message}")
