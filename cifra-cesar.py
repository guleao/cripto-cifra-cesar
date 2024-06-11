message = "Hello World"
shift = 7

LAST_CHAR_CODE = 90
CHAR_RANGE = 26

# Placeholder:
result = ""

#Looping que mostra as letras presentes dentro da message
for char in message.upper(): 
    if char.isalpha():
    # Converter caracteres para a ASCII.
        char_code = ord(char)
        # Nova numeração de acordo com o ASCII + quaantidade de caracteres (shift).
        new_char_code = char_code + shift

        if new_char_code > LAST_CHAR_CODE:
            new_char_code -= CHAR_RANGE

        new_char = chr(new_char_code)
        result += new_char
    else:
        result += char 

print(result)
