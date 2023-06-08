# shift list to right ( rotate the rotor )
def clock(given_list):

    given_list.append(given_list.pop(0))


# getting plain text
def get_plain_text():
    plain_text = input('put your plain text here: (no spaces allowed)')
    return plain_text


# Making internal keyboard ( a Whitelist of valid characters )
keyboard = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# first gear of the enigma machine
rotor1_1 = ['a', 'm', 'c', 'i', 'e', 'j', 'g', 'h', 'd', 'f', 'l', 'k', 'b',
            'n', 'y', 'z', 'o', 'x', 'w', 'u', 'v', 'p', 't', 'r', 's', 'q']
rotor1_2 = ['b', 'a', 'd', 'n', 'k', 'f', 'h', 'g', 'i', 'j', 'e', 'l', 'm',
            'c', 'x', 'v', 'p', 't', 'r', 'q', 'z', 'u', 'w', 'y', 'o', 's']

# second gear of the enigma machine
rotor2_1 = ['l', 'g', 'j', 'd', 'e', 'n', 'b', 'a', 'i', 'c', 'k', 'h', 'm',
            'f', 's', 't', 'q', 'w', 'o', 'x', 'v', 'r', 'p', 'z', 'y', 'u']
rotor2_2 = ['b', 'd', 'a', 'i', 'e', 'f', 'n', 'h', 'j', 'c', 'm', 'l', 'k',
            'g', 'r', 'z', 'u', 'x', 'p', 'q', 'o', 'v', 't', 's', 'w', 'y']

# third gear of the enigma machine
rotor3_1 = ['i', 'h', 'c', 'd', 'k', 'f', 'l', 'b', 'm', 'g', 'e', 'j', 'a',
            'n', 'w', 'o', 't', 's', 'y', 'v', 'r', 'p', 'x', 'q', 'u', 'z']
rotor3_2 = ['c', 'm', 'k', 'b', 'e', 'n', 'f', 'h', 'i', 'j', 'a', 'l', 'd',
            'g', 'v', 'p', 'o', 'y', 's', 'z', 'q', 'u', 'r', 't', 'w', 'x']

# reflect wall has only 13 alphabetic characters
reflection = ['a', 'm', 'f', 'k', 'j', 'r', 'h', 'o', 'g', 'c', 'd', 'e', 't',
              'f', 't', 'a', 'e', 'c', 'o', 'h', 'r', 'd', 'j', 'g', 'k', 'm']


def main():
    # enter your desired key
    key = input(' 3 letters for key : (no spaces allowed)')

    # conditions
    if len(key) > 3:
        breakpoint('too many characters')
    for i in key:
        if i not in keyboard:
            breakpoint('wrong type')

    key_elements = list(key)

    # setting the rotors to its right place due to the given key
    while key_elements[0] != rotor1_1[0]:
        clock(rotor1_1)
        clock(rotor1_2)

    while key_elements[1] != rotor2_1[0]:
        clock(rotor2_1)
        clock(rotor2_2)

    while key_elements[2] != rotor3_1[0]:
        clock(rotor3_1)
        clock(rotor3_2)

    clock_counter = 1
    plain_text = ''

    # starting enigma machine / when to stop the machine
    while plain_text != '!':
    
        cipher = []
        plain_text = get_plain_text()

        for i in list(plain_text):

            if i in keyboard:
                ref = rotor3_2.index(rotor3_1[rotor2_2.index(rotor2_1[rotor1_2.index(
                    rotor1_1[keyboard.index(i)])])])

                if ref in range(0, 14):

                    n_ref = reflection.index(reflection[ref], 13)

                else:
                    n_ref = reflection.index(reflection[ref])

                cipher.append(keyboard[rotor1_1.index(rotor1_2[rotor2_1.index(
                    rotor2_2[rotor3_1.index(rotor3_2[n_ref])])])])

                # let clock_counter rotate correctly
                for j in plain_text:
                    if j not in keyboard:
                        breakpoint('forbidden characters!')
                    else:
                        clock_counter += 1

                # first rotor will be rotated every clock_counter
                clock(rotor1_1)
                clock(rotor1_2)
            
                # third rotor will be rotated after every 676 ( 26 * 26 ) clock_counter.
                if clock_counter % 676 == 0:
                    clock(rotor3_1)
                    clock(rotor3_2)

                # second rotor will be rotated after every 26 ( length of alphabetical characters ) clock_counter.
                elif clock_counter % 26 == 0:
                    clock(rotor2_1)
                    clock(rotor2_2)

                else:
                    continue

        string = ''
        print(string.join(cipher))
