import random
from ascii import HANGMANPICS


def game_level_function():
    """Funkcija aprasanti vartotojo lygio pasirinkima.
    Vartotojas negali ivesti radies."""
    while True:
        try:
            user_game_level = int(input('Pasirinkite žaidimo sunkumą: '))
            while user_game_level <= 2:
                user_game_level = int(input('Pasirinkite žaidimo sunkumą: '))
        except ValueError:
            print('Įvesčiai reikalingas skaičius! Bandykite dar kartą.')
        else:
            return user_game_level


def mistake_num_func():
    """Funkcija aprasanti vartotojo klaidu skaiciaus pssirenkamuma.
    Vartotojas negali ivesti raides."""
    while True:
        try:
            mistake_number_1 = int(input('Pasirinkite suklydimų skaičių (nuo 3 iki 6): '))
        except ValueError:
            print('Įvesčiai reikalingas skaičius! Bandykite dar kartą.')
        else:
            return mistake_number_1


def game_repeat_func():
    """Funkcija skirta vartotojo nora zaisti toliau ar uzbaigti ji."""
    while True:
        game_repeat = input('Ar norite bandyti dar kartą (taip/ne)? ')
        if game_repeat == 'ne':
            print('Ačiū, kad žaidėte.')
            return False
        elif game_repeat == 'taip':
            print('Sėkmeė kitame žaidime!')
            return True
        elif game_repeat != 'taip':
            print('Įvesties klaida. Bandykite dar kartą.')


zaidimas = True

while zaidimas:
    # Iskvieciama funkcija ir gaunamas zaidimo sunku lygis..
    game_level = game_level_function()

    # Nuskaitome turimu zodziu sarasa ir atrenkame reikiamo ilgio zodzius.
    words_list = []
    file_object = open('words.txt', 'r')
    for word in file_object:
        word_len = len(word)
        if game_level < word_len:
            words_list.append(word.replace('\n', '').lower())

    # Is atrinktu zodziu saraso atrenkame viena ir ji isskaidome i raides.
    random_word = random.choice(words_list)
    random_split = list(enumerate(random_word))
    hidden_list = '-' * len(random_word)
    print("Reikalingas žodis atspėti: " + hidden_list)

    # Iskvieciama funkcija klaidu skaiciui nustatyti.
    mistake_number = mistake_num_func()
    mistake = 0

    # Pasikartojanciu raidziu sarasas.
    same_random_letters = []
    same_mistake = 0

    # Spejimu kilpa
    while mistake_number != mistake:
        random_letter = str(input('Įveskite spėjamą raidę: '))
        if random_letter.isalpha():
            if random_letter in same_random_letters:
                if same_mistake == 1:
                    mistake += 1
                    print('Raidė ' + random_letter + ' buvo jau spėta prieš tai. Suklydote dar kartą!')
                    print(HANGMANPICS[6 - mistake_number + mistake])
                else:
                    print('Ši raidė jau buvo spėta!')
                    same_mistake += 1
            elif random_letter not in random_word:
                print('Šios raidės žodyje nėra. Spėkite kitą raidę.')
                mistake += 1
                same_random_letters.append(random_letter)
                if mistake == mistake_number:
                    print(HANGMANPICS[6 - mistake_number + mistake])
                    print('Pralaimėjote! Reikalingas žodis atspėti buvo: '
                          + random_word + '.')
                else:
                    print(HANGMANPICS[6 - mistake_number + mistake])
            elif random_word not in hidden_list:
                same_random_letters.append(random_letter)
                for k, v in random_split:
                    if v == random_letter:
                        loop_word = list(hidden_list)
                        loop_word[k] = random_letter
                        hidden_list = "".join(loop_word)
                if random_word == hidden_list:
                    print("Šaunu! Žodis atspėtas!")
                    break
                else:
                    print('Pasirinkta raidė teisinga! Tęskite spėjant kitą raidę.')
                    print(hidden_list)
        else:
            print('Įvesčiai reikalinga raidė. Bandykite dar kartą.')
            continue

    zaidimas = game_repeat_func()
