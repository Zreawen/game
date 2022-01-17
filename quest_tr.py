import random as rm
from  playsound import playsound

def quest_goko():
    qf = 0
    qp1 = 0
    qp2 = 0
    qp3 = 0
    qp4 = 0
    qp5 = 0

    while qf != 1:
        quest = rm.randint(1, 5)


        if qp1 == 1 and qp2 == 1 and qp3 == 1 and qp4 == 1 and qp5 == 1:
            qf += 1

        elif quest == 1 and  qp1 == 0:
            print("""
                ? Ali'nin ilk sevgilisi kimdir? ?
                """)
            cevap = input("> ")

            if cevap == "Sıla" or cevap == "sıla" or cevap == "Sila" or cevap == "sila":
                qp1 += 1
                print("! Tebrikler doğru bildin")
                print("@ olduğuma çok pişmanım")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

        elif quest == 2 and qp2 == 0:
            print("""
            ? Ali 2020 yılındaki doğum gününde aldığı para ile ne almıştır? ?
            """)
            cevap = input("> ")
            if cevap == "dl" or cevap == "Dl" or cevap == "DL" or cevap == "diamond lock" or cevap == "Diamond Lock":
                qp2 += 1
                print("! Tebrikler doğru bildin")
                print("@ Tam enayi değilmiyim?")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

        elif quest == 3 and qp3 == 0:
            print("""
            ? Ali'nin köpeğinin adı nedir? ?
            """)
            cevap = input("> ")
            if cevap == "sarah" or cevap == "Sarah" or cevap == "sara" or cevap == "Sara":
                qp3 += 1
                print("! Tebrikler doğru bildin")
                print("@ keşke almasaydım")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

        elif quest == 4 and qp4 == 0:
            print("""
            ? Gökhan'ın gerçekten sevdiği ve açıldığı ilk kız veya erkek(lol)? ?
            """)
            cevap = input("> ")
            if cevap == "deniz" or cevap == "Deniz":
                qp4 += 1
                print("! Tebrikler doğru bildin")
                print("""
                @ dinle o gün red yediğinde seni teselli edememiş veya arkanda durmadığım için özür dilerim.
                  biliyor musun o kız seni hak etmiyor gitsin bok yesin.
                  fuck you deniz.
                """)
                playsound('complate.mp3')
            elif cevap == "ali" or cevap == "Ali":
                print("WTF")
                #ali yazabileceğini düşündüğüm için ekledim yoksa yanlış anlama seni homofobik orospu çocu
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

        elif quest == 5 and qp5 == 0:
            print("""
            ? budsiki mi airpods pro mu? ?
            """)
            cevap = input("> ")
            if cevap == "budsiki" or cevap == "Budsiki" or cevap == "buds 2" or cevap == "Buds 2" or cevap == "buds iki" or cevap == "Buds iki":
                qp5 += 1
                print("! Tebrikler doğru bildin")
                print("@ e yani")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

def quest_kerim():
    qf = 0
    qp1 = 0
    qp2 = 0
    qp3 = 0
    qp4 = 0
    qp5 = 0

    while qf != 1:
        quest = rm.randint(1, 5)


        if qp1 == 1 and qp2 == 1 and qp3 == 1 and qp4 == 1 and qp5 == 1:
            qf += 1

        elif quest == 1 and qp1 == 0:
            print("""
            ? Hamza'nın cinsiyeti nedir? ?
            """)
            cevap = input("> ")
            if cevap == "gay" or cevap == "Gay":
                qp1 += 1
                print("! Tebrikler doğru bildin")
                print("@ yalnız ne sikişiyodunuz arka sıralarda")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

        elif quest == 2 and qp2 == 0:
            print("""
            ? Bir tane daha küçük kerim vardı. O küçük kerim benim hangi farm seedlerimi çalmıştı? ?
            """)
            cevap = input("> ")
            if cevap == "pepper" or cevap == "Pepper":
                qp2 += 1
                print("! Tebrikler doğru bildin")
                print("@ yalnız ne piçti o çocuk")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

        elif quest == 3 and qp3 == 0:
            print("""
            ? Benim yanımda oturan çocuk kimdi? ?
            """)
            cevap = input("> ")
            if cevap == "yıldırım" or cevap == "Yıldırım" or cevap == "yildirim" or cevap == "Yildirim":
                qp3 += 1
                print("! Tebrikler doğru bildin")
                print("@ çok iyi çocuktu")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

        elif quest == 4 and qp4 == 0:
            print("""
            ? Senle hep dalga geçtikleri özelliğin? ?
            """)
            cevap = input("> ")
            if cevap == "kekeleme" or cevap == "Kekeleme" or cevap == "kekelemek" or cevap == "Kekelemek":
                qp4 += 1
                print("! Tebrikler doğru bildin")
                print("@ takma kafana, dalga geçenleri direkt sik")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

        elif quest == 5 and qp5 == 0:
            print("""
            ? Beni seviyor musun aşko? ?
            """)
            cevap = input("> ")
            if cevap == "Evet" or cevap == "evet":
                qp5 += 1
                print("@ Bende seni aşko")
                playsound('complate.mp3')
            else:
                print("! nE")
                playsound('wrong.mp3')



def quest_berke():
    qf = 0
    qp1 = 0
    qp2 = 0
    qp3 = 0
    qp4 = 0
    qp5 = 0

    while qf != 1:
        quest = rm.randint(1, 5)

        if qp1 == 1 and qp2 == 1 and qp3 == 1 and qp4 == 1 and qp5 == 1:
            qf += 1

def quest_ecrin():
    qf = 0
    qp1 = 0
    qp2 = 0
    qp3 = 0
    qp4 = 0
    qp5 = 0

    while qf != 1:
        quest = rm.randint(1, 5)

        if qp1 == 1 and qp2 == 1 and qp3 == 1 and qp4 == 1 and qp5 == 1:
            qf += 1

def quest_simge():
    qf = 0
    qp1 = 0
    qp2 = 0
    qp3 = 0
    qp4 = 0
    qp5 = 0

    while qf != 1:
        quest = rm.randint(1, 5)

        if qp1 == 1 and qp2 == 1 and qp3 == 1 and qp4 == 1 and qp5 == 1:
            qf += 1

        elif quest == 1 and qp1 == 0:
            print("""
            ? Bu okuldaki ilk sevgilin? ?
            """)
            cevap = input("> ")
            if cevap == "Mert" or cevap == "mert" or cevap == "Amed" or cevap == "amed" or cevap == "mert amed" or cevap == "Mert Amed" or cevap == "Mert amed":
                qp1 += 1
                print("! Tebrikler doğru bildin")
                print("@ kardeşim ne diyim yani? keşke sevgili olmadan bize sorsaydın.")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

        elif quest == 2 and qp2 == 0:
            print("""
            ? p
            """)
            cevap = input("> ")
            if cevap == "" or cevap == "":
                qp2 += 1
                print("! Tebrikler doğru bildin")
                print("@ ")
                playsound('complate.mp3')
            else:
                print("! Verdiğin cevap doğru değil")
                playsound('wrong.mp3')

def quest_almina():
    qf = 0
    qp1 = 0
    qp2 = 0
    qp3 = 0
    qp4 = 0
    qp5 = 0

    while qf != 1:
        quest = rm.randint(1, 5)

        if qp1 == 1 and qp2 == 1 and qp3 == 1 and qp4 == 1 and qp5 == 1:
            qf += 1



def quest_doruk():
    qf = 0
    qp1 = 0
    qp2 = 0
    qp3 = 0
    qp4 = 0
    qp5 = 0

    while qf != 1:
        quest = rm.randint(1, 5)

        if qp1 == 1 and qp2 == 1 and qp3 == 1 and qp4 == 1 and qp5 == 1:
            qf += 1



