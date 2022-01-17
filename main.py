import random as r
import quest_tr as tr

name = input("Please enter you'r name: ")

num = r.randint(1, 265)

goko = 0
kerim = 0
ege = 0
berke = 0
ecrin = 0
simge = 0
almina = 0
doruk = 0
türker = 0


if name == "goko" or name == "Goko":
    print("! Hala sevgilin yok dimi. Tamda tahmin ettiğim gibi, hadi geç")
    print("! and you'r number is :")
    print(num)
    print("! have a good time")
    goko += 1

elif name == "ali" or name == "Ali":
    print("! Hello Mr.ASSHole")
    print("! and you'r number is :")
    print(num)
    print("! have a good time")
    #bu testi yaparken pek arkadaşımın olmadığını fark ettim

elif name == "kerim" or name == "Kerim":
    print("! Ohh naber aşko")
    print("! and you'r number is :")
    print(num)
    print("! have a good time")
    kerim += 1

elif name == "ecrin" or name == "Ecrin":
    print("! Vay seni küçük boylu cüce, hoşgeldin")
    ecrin += 1

elif name == "Almina" or name == "almina" or name == "naz" or name == "Naz" or name == "Almina naz" or name == "Almina Naz":
    print("! Merhaba seni enayi")
    almina += 1

elif name == "Simge" or name == "simge":
    print("! oooo hoşgeldin geri zekalı")
    simge += 1

else:
    print("! Hello player, " + name)
    print("! and you'r number is :")
    print(num)
    print("! have a good time")



print("""

    1. English
    2. Turkish

    """)
game_len = input("> Please enter you'r game language: ")

def eng_game():
    print("! Game language is done")

def tr_game():
    if goko == 1:
        tr.quest_goko()
    elif kerim == 1:
        tr.quest_kerim()
    elif berke == 1:
        tr.quest_berke()
    elif simge == 1:
        tr.quest_simge()
    elif ecrin == 1:
        tr.quest_ecrin()
    elif almina == 1:
        tr.quest_almina()
    elif doruk == 1:
        tr.quest_doruk()


if game_len == "tr" or game_len == "turkish" or game_len == "Turkish" or game_len == "2":
    tr_game()

elif game_len == "en" or game_len == "english" or game_len == "English" or game_len == "1":
    eng_game()


