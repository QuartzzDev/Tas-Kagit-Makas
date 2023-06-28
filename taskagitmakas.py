import random  # print(Style.RESET_ALL)
import time
from colorama import Fore, Back, Style

oyundanCik = 0

Hamleler = ["Taş", "Kağıt", "Makas"]  # Bot Hüsnünün Yapabileceği Hamleler


# Çizgi Çizmek İçin Ayrı Ayrı Uğraşmak Yerine Fonksiyona Koydum
def YesilCizgi():
  print(Fore.GREEN, "______________________________________")
  print(Style.RESET_ALL)


def KirmiziCizgi():
  print(Fore.RED, "______________________________________")
  print(Style.RESET_ALL)


def MaviCizgi():
  print(Fore.BLUE, "______________________________________")
  print(Style.RESET_ALL)


# Başlık

KirmiziCizgi()
print(Fore.RED, "Quartzz ile", Fore.LIGHTCYAN_EX, "Taş", Fore.LIGHTMAGENTA_EX,
      "Kağıt", Fore.LIGHTYELLOW_EX, "Makas")
print(Style.RESET_ALL)
MaviCizgi()

print("Oyun Başlıyor . . .")
time.sleep(3)

KirmiziCizgi()
playerName = input("Hey Oyuncu ..\nKendine Havalı Bir İsim Koy . . ")
KirmiziCizgi()

while oyundanCik == 0:

  print(playerName, "-> İlk Hamleni Yap 'Taş - Kağıt - Makas' "
        )  # Kullancıdan Hamlesini Aldığımız Yer
  ilkHamle = input()

  botHamle = random.choice(Hamleler)  # Hüsnü'nün Hamlesini Belirledik

  # Verilen Cevaplara Göre Sonuçları Yazdırdık
  if (ilkHamle == "Taş" and botHamle == "Makas"):
    YesilCizgi()
    print("Bot Hüsnü ->", botHamle, "--------", playerName, "->", ilkHamle)
    time.sleep(2)
    print("Taş -> Makas'ı Kırar", playerName, "Oyunu Kazandı")  # Taş Makas
    YesilCizgi()
  elif (ilkHamle == "Makas" and botHamle == "Taş"):
    YesilCizgi()
    print("Bot Hüsnü ->", botHamle, "--------", playerName, "->", ilkHamle)
    time.sleep(2)
    print("Taş -> Makas'ı Kırar", "Bot Hüsnü", "Oyunu Kazandı")  # Taş Makas
    YesilCizgi()
  elif (ilkHamle == "Kağıt" and botHamle == "Taş"):
    YesilCizgi()
    print("Bot Hüsnü ->", botHamle, "--------", playerName, "->", ilkHamle)
    time.sleep(2)
    print("Kağıt -> Taş'ı Sarar", playerName, "Oyunu Kazandı")  # Taş Kağıt
    YesilCizgi()
  elif (ilkHamle == "Taş" and botHamle == "Kağıt"):
    YesilCizgi()
    print("Bot Hüsnü ->", botHamle, "--------", playerName, "->", ilkHamle)
    time.sleep(2)
    print("Kağıt -> Taş'ı Sarar", "Bot Hüsnü", "Oyunu Kazandı")  # Taş Kağıt
    YesilCizgi()
  elif (ilkHamle == "Makas" and botHamle == "Kağıt"):
    YesilCizgi()
    print("Bot Hüsnü ->", botHamle, "--------", playerName, "->", ilkHamle)
    time.sleep(2)
    print("Makas -> Kağıt'ı Keser", playerName, "Oyunu Kazandı")  # Makas Kağıt
    YesilCizgi()
  elif (ilkHamle == "Kağıt" and botHamle == "Makas"):
    YesilCizgi()
    print("Bot Hüsnü ->", botHamle, "--------", playerName, "->", ilkHamle)
    time.sleep(2)
    print("Kağıt -> Kağıt'ı Keser", "Bot Hüsnü",
          "Oyunu Kazandı")  # Makas Kağıt
    YesilCizgi()
  elif (ilkHamle == "Taş" and botHamle == "Taş"):
    time.sleep(2)
    YesilCizgi()
    print(
      "Taş ve Taş hmm Yoksa Birbirlerini Gösteren Spidermanlar mı Deseydim -> Oyun Berabere"
    )  # Taş Taş
    YesilCizgi()
  elif (ilkHamle == "Kağıt" and botHamle == "Kağıt"):
    time.sleep(2)
    YesilCizgi()
    print(
      "Kağıt ve Kağıt hmm Yoksa Birbirlerini Gösteren Spidermanlar mı Deseydim -> Oyun Berabere"
    )  # Kağıt Kağıt
    YesilCizgi()
  elif (ilkHamle == "Makas" and botHamle == "Makas"):
    time.sleep(2)
    YesilCizgi()
    print(
      "Makas ve Makas hmm Yoksa Birbirlerini Gösteren Spidermanlar mı Deseydim -> Oyun Berabere"
    )  # Makas Makas
    YesilCizgi()
  else:
    time.sleep(2)
    YesilCizgi()
    print("Hatalı Giriş Yaptın Gibi Gözükyor Canım :) Birdaha Dene")
    YesilCizgi()
