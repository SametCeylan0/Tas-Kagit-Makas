import random
import time

print("*" * 10, "TAŞ, KAĞIT, MAKAS", "*"*10)
print("\n        ## 5 OLAN KAZANIR ##")

player_name = input("\nİsminizi giriniz: ")

comp_point = 0
player_point = 0

while True:
    players_action = input("Hamlenizi yapın(taş, kağıt, makas): ")

    p_choices = ["taş", "kağıt", "makas"]

    computer_action = random.choice(p_choices)

    print("oyuncu seçimi: " ,players_action,"--/--", "PC seçimi: ", computer_action)
    second = time.sleep(2)

    if players_action == computer_action:
        print(f"İki oyuncu da aynısını seçti: {players_action}. BERABERE! \n {player_name.upper()} = {player_point}\n Bilgisayar = {comp_point}")

    elif players_action == "taş":
        if computer_action == "kağıt":
            comp_point += 1
            print(f"Kağıt taşı sarar. BİLGİSAYAR KAZANDI! \n {player_name.upper()} = {player_point}\n Bilgisayar = {comp_point}")
        elif computer_action == "makas":
            player_point += 1
            print(f"Taş makası kırar. {player_name.upper()}  KAZANDI! \n {player_name.upper()} = {player_point}\n Bilgisayar = {comp_point} ")

    elif players_action == "kağıt":
        if computer_action == "makas":
            comp_point += 1
            print(f"Makas kağıdı keser BİLGİSAYAR KAZANDI! \n {player_name.upper()} = {player_point}\n Bilgisayar = {comp_point}")
        elif computer_action == "taş":
            player_point += 1
            print(f"Kağıt taşı sarar. {player_name.upper()} KAZANDI! \n {player_name.upper()} = {player_point}\n Bilgisayar = {comp_point} ")

    elif players_action == "makas":
        if computer_action == "taş":
            comp_point += 1
            print(f"Taş makası kırar. BİLGİSAYAR KAZANDI! \n {player_name.upper()} = {player_point}\n Bilgisayar = {comp_point}")
        elif computer_action == "kağıt":
            player_point += 1
            print(f"Kağıt taşı sarar. {player_name.upper()}  KAZANDI! \n {player_name.upper()} =  {player_point}\n Bilgisayar = {comp_point}")
    else:
        print("----HATALI KELİME GİRİŞİ----")

    if player_point == 5:
        print(player_name.upper(), "OYUNU KAZANDI !!!")
    elif comp_point == 5:
        print("BİLGİSAYAR KAZANDI !!!")

    if player_point == 5:
        breaking = input("Devam? (evet/hayır): ")
        if breaking.lower() == "hayır":
            break
        elif breaking.lower() == "evet":
            comp_point = 0
            player_point = 0
            continue
        else:
            print("HATALI GİRİŞ")

    elif comp_point == 5:
        breaking = input("Devam? (evet/hayır): ")
        if breaking.lower() == "hayır":
            break
        elif breaking.lower() == "evet":
            comp_point = 0
            player_point = 0
            continue
        else:
            print("HATALI GİRİŞ")

print(f"--OYUN BİTMİŞTİR--\nBilgisayar Puanı = {comp_point}\n{player_name.upper()} = {player_point}")