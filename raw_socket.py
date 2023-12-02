from math import ceil
import sys


def b64_encode(string_in, is_padded: int):
    upper = [chr(x) for x in range(65, 91)]
    lower = [chr(x) for x in range(97, 123)]
    index_upper = [x for x in range(0, 26)]
    index_lower = [x for x in range(26, 52)]
    digits = [str(x) for x in range(0, 10)]
    index_digits = [x for x in range(52, 63)]

    b64_alpha = {**dict(zip(index_upper, upper)),
                 **dict(zip(index_lower, lower)),
                 **dict(zip(index_digits, digits)),
                 **{62: '+', 63: '/'}
                 }

    binary = "".join([f'{ord(x):08b}' for x in string_in])
    sextets = []

    # partition the binary into sextets
    for x in range(0, len(binary), 6):
        sextets.append(binary[x:x + 6])
    # padding the last sextet
    sextets[-1] = f"{sextets[-1]:0<6}"
    padding = ceil(len(sextets) / 4) * 4 - len(sextets)

    # return padding * ['=']
    b64_alpha_index = [int(x, 2) for x in sextets]
    encoded = [b64_alpha[x] for x in b64_alpha_index]

    if is_padded == 1:
        encoded = ''.join(encoded + padding * ['='])

    return ''.join(encoded)


while True:
    string = ""
    while True:
        line = input("Enter a line (press Enter twice to finish):\n")
        if not line:
            break  # Exit the loop if an empty line is entered
        string += line + "\n"

    encoded_text = b64_encode(string, 1)

    print(encoded_text)