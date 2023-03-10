
morse_code = {
    'A': '.-', 'B': '-...',   'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..', ' ': '/',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.'
}

new_message = []
message = input('Enter your message here! \n')
for char in message.upper():
    code = morse_code[char]
    new_message.append(code)

coded_message = " ".join(new_message)
print(coded_message)


# Short route to the code!
# converted_message = "".join(morse_code[char] for char in message.upper())
# print(converted_message)

morse_reversed = {v: k for k, v in morse_code.items()}

decoded_message = " ".join(morse_reversed[char] for char in coded_message.split(" "))
print(decoded_message)































