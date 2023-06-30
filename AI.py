import os 
import random
import time 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

facts = [
    "The shortest war in history was between Britain and Zanzibar in 1896. It lasted only 38 minutes.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "A group of flamingos is called a 'flamboyance'.",
    "The average person walks the equivalent of three times around the world in their lifetime.",
    "The world's oldest known recipe is for beer. It was found on a Sumerian clay tablet and dates back to around 1800 BCE.",
    "Koalas have unique fingerprints, just like humans.",
    "The electric chair was invented by a dentist.",
    "The word 'nerd' was first coined by Dr. Seuss in his book 'If I Ran the Zoo'.",
    "Bananas are berries, while strawberries are not.",
    "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    "The fingerprints of koalas are so similar to humans that they have been confused at crime scenes.",
    "The Hawaiian alphabet only has 12 letters: A, E, I, O, U, H, K, L, M, N, P, and W.",
    "The average person spends six months of their lifetime waiting for red traffic lights to turn green.",
    "The world's oldest known joke is from ancient Sumeria and is a fart joke.",
    "In Japan, it is common for people to take a nap during their lunch break. This is called 'inemuri'.",
    "A bolt of lightning is six times hotter than the surface of the sun.",
    "Cows have best friends and can become stressed when separated from them.",
    "The first webcam was used at the University of Cambridge to monitor a coffee pot.",
    "The unicorn is the national animal of Scotland.",
    "The world's largest pyramid is not in Egypt but in Cholula, Mexico.",
    "Octopuses have three hearts.",
    "The average person blinks around 15-20 times per minute.",
    "The oldest known customer complaint is from ancient Mesopotamia, written on a clay tablet around 1750 BCE.",
    "The longest recorded flight of a chicken is 13 seconds.",
    "Wombat feces are cube-shaped.",
    "Penguins have an organ above their eyes that converts seawater into freshwater.",
    "The average person swallows around 295 times while eating a meal.",
    "The shortest war in history was between Britain and Zanzibar in 1896. It lasted only 38 minutes.",
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
    "A group of flamingos is called a 'flamboyance'.",
    "The average person walks the equivalent of three times around the world in their lifetime.",
    "The world's oldest known recipe is for beer. It was found on a Sumerian clay tablet and dates back to around 1800 BCE.",
    "Koalas have unique fingerprints, just like humans.",
    "The electric chair was invented by a dentist.",
    "The word 'nerd' was first coined by Dr. Seuss in his book 'If I Ran the Zoo'.",
    "Bananas are berries, while strawberries are not.",
    "There are more possible iterations of a game of chess than there are atoms in the observable universe.",
    "The fingerprints of koalas are so similar to humans that they have been confused at crime scenes.",
    "The Hawaiian alphabet only has 12 letters: A, E, I, O, U, H, K, L, M, N, P, and W.",
    "The average person spends six months of their lifetime waiting for red traffic lights to turn green.",
    "The world's oldest known joke is from ancient Sumeria and is a fart joke."
]

random.shuffle(facts)

print("=======")
print("By Ibnu")
print("=======")
time.sleep(1.0)
print("masukan nama kamu")
nama = input("type: ")
time.sleep(1.0)
print("halo", nama, "selamat datang")
time.sleep(2.0)
clear()

def bot():
    print("============")
    print("halo saya adalah AI yang di ciptakan ######")
    print("============")
    print("perintah: ")
    print("#1 halo")
    print("#2 berikan saya fakta unik")
    print("#3 coming soon")
    print("=============")
    print("jika anda ingin bot ini bekerja masukan angka sesuai perintah diatas")
    print("contoh: #1, #2, #3")
    print("============")

bot()

while True:
    perintah = input("type: ")
    if perintah == "#1":
        print("halo saya adalah AI yang di ciptakan oleh ####, saya masih dalam tahap pengembangan jadi jika ada sesuatu yang error mohon dimaklumi")
        time.sleep(1.0)
        print("ulang y/n")
        ulang = input("type: ")
        while True:
            if ulang == "y":
                print("okay")
                time.sleep(1.0)
                clear()
                bot()
                break 
            elif ulang == "n":
                print("bye bye")
                print("terima kasih telah menggunakan saya")
                time.sleep(1.0)
                exit()
            else:
                print("mohon ketik y/n")
                time.sleep(1.0)
                clear()
                print("ulang y/n")
                ulang = input("type: ")
    elif perintah == "#2":
        print(facts[0])  
        facts.append(facts.pop(0)) 
        time.sleep(1.0)
        print("ulang y/n")
        ulang2 = input("type: ")
        while True:
            if ulang2 == "y":
                print("okay")
                time.sleep(1.0)
                clear()
                bot()
                break 
            elif ulang2 == "n":
                print("bye bye")
                print("terima kasih telah menggunakan saya")
                time.sleep(1.0)
                exit()
            else:
                print("mohon ketik y/n")
                time.sleep(1.0)
                clear()
                print("ulang y/n")
                ulang2 = input("type: ")
    elif perintah == "#3":
        print("coming soon")
        time.sleep(1.0)
        print("ke menu awal y/n")
        menu_awal = input("type: ")
        while True:
            if menu_awal == "y":
                time.sleep(1.0)
                print("okay")
                time.sleep(1.0)
                clear()
                bot()
                break
            elif menu_awal == "n":
                print("bye bye")
                print("terima kasih telah menggunakan saya")
                time.sleep(1.0)
                exit()
            
            else:
                print("mohon ketik y/n")
                time.sleep(1.0)
                clear()
                print("ke menu awal y/n")
                menu_awal = input("type: ")
    
    else:
        print("mohon ketik sesuai perintah yang ada di atas")