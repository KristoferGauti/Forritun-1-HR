import os

def cls():
    os.system('cls')



def print_options():
    cls()
    print("Veldu eitt af eftirfarandi")
    print("-"*len("Veldu eitt af eftirfarandi"))
    print("1.  Viðskiptavinir")
    print("2.  Bílafloti")
    print("3.  Afgreiðsla")
    print("4.  Pantanir")
    print("5.  Hætta")
    print("-"*len("Veldu eitt af eftirfarandi"))
    input_num = input("Val: ")
    print()
    if input_num == "1":
        vidskiptavinir_options()
    elif input_num == "2":
        bilafloti_options()
    elif input_num == "3":
        afgreidsla_options()
    elif input_num == "4":
        pantanir_options()
    elif input_num == "5":
        exit()
    else:
        print_options()

def vidskiptavinir_options():
    cls()
    print("Viðskiptavinir")
    print("-"*len("1.  Skrá nýjan viðskiptavin"))
    print("1.  Skrá nýjan viðskiptavin")
    print("2.  Fletta upp viðskiptavin")
    print("3.  Afskrá viðskiptavin")
    print("4.  Uppfæra viðskiptavin")
    print("5.  Setja á bannlista")
    print("6.  Taka af bannlista")
    print("7.  Sekta viðskiptavin")
    print("8.  Til baka")
    print("-"*len("1.  Skrá nýjan viðskiptavin"))
    input_num = input("Val: ")
    print()
    if input_num == "1":
        skra_vidskiptavin()
    elif input_num == "2":
        fletta_vidskiptavin()
    elif input_num == "3":
        afskra_vidskiptavin()
    elif input_num == "4":
        breyta_vidskiptavin()
    elif input_num == "5":
        setja_a_bannlista()
    elif input_num == "6":
        taka_af_bannlista()
    elif input_num == "7":
        sekta_vidskiptavini()
    else:
        print_options()

def skra_vidskiptavin():
    cls()
    nafn = input("Nafn: ")
    print("-"*len("Viðskiptavinur {} hefur verið skráður".format(nafn)) + "\n")
    símanr = input("Símanúmer: ")
    print("-"*len("Viðskiptavinur {} hefur verið skráður".format(nafn)) + "\n")
    netfang = input("Netfang: ")
    print("-"*len("Viðskiptavinur {} hefur verið skráður".format(nafn)) + "\n")
    kreditkortanumer = input("Kreditkortanr. (xxxx-xxxx-xxxx-xxxx): ")
    print("-"*len("Viðskiptavinur {} hefur verið skráður".format(nafn)) + "\n")
    kennitolu_check = input("Er viðskiptavinur með kennitölu? (j/n): ")
    print("-"*len("Viðskiptavinur {} hefur verið skráður".format(nafn)) + "\n")
    if kennitolu_check.lower() == "j":
        kennitala = input("Kennitala: ")
    print("-"*len("Viðskiptavinur {} hefur verið skráður".format(nafn)) + "\n")
    print("Viðskiptavinur {} hefur verið skráður".format(nafn))
    print("-"*len("Viðskiptavinur {} hefur verið skráður".format(nafn)) + "\n")
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass
    print_options()

def afskra_vidskiptavin():
    cls()
    kt = input("Hvern a að afskrá? (kennitala/netfang): ")
    print("-"*len("Afskrá: Jóhanna Einarsdóttir, 1506992669? (y/n):") + "\n")
    svar = input("Afskrá: Jóhanna Einarsdóttir, {}? (j/n): ".format(kt))
    print("-"*len("Afskrá: Jóhanna Einarsdóttir, 1506992669? (y/n):") + "\n")
    if svar.lower() == "j":
        print("Jóhanna Einarsdóttir afskráð")
    else:
        print("Hætt við")
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def fletta_vidskiptavin():
    cls()
    print("Fletta upp viðskiptavini eftir:")
    print("-"*len("Fletta upp viðskiptavini eftir:"))
    print("1. Kennitölu")
    print("2. Nafni")   
    print("3. Símanúmeri")
    print("4. Netfangi")
    print("5. Til baka")
    print("-"*len("Fletta upp viðskiptavini eftir:"))
    val = input("Val: ")
    if val == "1":
        fletta_vidskiptavin_kt()
    elif val == "2":
        fletta_vidskiptavin_nafn()
    elif val == "3":
        fletta_vidskiptavin_simanr()
    elif val == "4":
        fletta_vidskiptavin_netfang()
    else:
        vidskiptavinir_options()

def fletta_vidskiptavin_netfang():
    cls()
    netfang = input("Netfang: ")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234"))
    print("Nafn: Jón Ólafsson")
    print("Kennitala: 2903983209")
    print("Símanr: 8886785")
    print("Netfang: " + netfang)
    print("Kreditkortanúmer: 1234-1234-1234-1234")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234"))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def fletta_vidskiptavin_kt():
    cls()
    kennitala = input("Kennitala: ")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234"))
    print("Nafn: Jón Ólafsson")
    print("Kennitala: " + kennitala)
    print("Símanr: 8886785")
    print("Netfang: JohnnyBoy23@internet.is")
    print("Kreditkortanúmer: 1234-1234-1234-1234")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234"))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def fletta_vidskiptavin_nafn():
    cls()
    nafn = input("Nafn: ")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234"))
    print("Nafn: " + nafn)
    print("Kennitala: 0303782289")
    print("Símanúmer: 8886785")
    print("Netfang: JohnnyBoy23@internet.is")
    print("Kreditkortanúmer: 1234-1234-1234-1234")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234"))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def fletta_vidskiptavin_simanr():
    cls()
    simanr = input("Símanúmer: ")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234"))
    print("Nafn: Jón Ólafsson")
    print("Kennitala: 0303782289")
    print("Símanr: " + simanr)
    print("Netfang: JohnnyBoy23@internet.is")
    print("Kreditkortanúmer: 1234-1234-1234-1234")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234"))

    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def breyta_vidskiptavin():
    cls()
    netfang = input("Netfang: ")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234"))
    print("Viðskiptavinur fundinn.")
    print("Nafn: Jón Ólafsson")
    print("Kennitala: 2903983209")
    print("Símanr: 8886785")
    print("Netfang: " + netfang)
    print("Kreditkortanúmer: 1234-1234-1234-1234")
    print("-"*len("Kreditkortanúmer: 1234-1234-1234-1234") + "\n")

    print("Breyta: ")
    print("-"*len("4. Kreditkortanúmeri"))
    print("1. Nafni")
    print("2. Símanúmeri")
    print("3. Netfangi")
    print("4. Kreditkortanúmeri")
    print("5. Til baka")
    print("-"*len("4. Kreditkortanúmeri"))
    val = input("Val:")
    print("-"*len("4. Kreditkortanúmeri"))
    if val == "1":
        nafn = input("Nýtt nafn: ")
        print("Nafni hefur verið breytt.")
    elif val == "2":
        simanr = input("Nýtt Símanúmer: ")
        print("Símanúmeri hefur verið breytt.")
    elif val == "3":
        netfang = input("Nýtt netfang: ")
        print("Netfangi hefur verið breytt.")
    elif val == "4":
        kortanumer = input("Nýtt kreditkortanr. (xxxx-xxxx-xxxx-xxxx): ")
        print("Kortanúmeri hefur verið breytt.")
    elif val == "5":
        vidskiptavinir_options()

    print("-"*len("4. Kreditkortanúmeri"))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass
    

def setja_a_bannlista():
    cls()
    netfang = input("Netfang: ")
    print("-"*len("Setja á bannlista: Jón Ólafsson, {}? (j/n): ".format(netfang)))
    stadfesta = input("Setja á bannlista: Jón Ólafsson, {}? (j/n): ".format(netfang))
    print("-"*len("Setja á bannlista: Jón Ólafsson, {}? (j/n): ".format(netfang)))
    if stadfesta == "j":
        print("Jón Ólafsson hefur verið færður á bannlista.")
    else:
        print("Hætt við.")
    print("-"*len("Setja á bannlista: Jón Ólafsson, {}? (j/n): ".format(netfang)))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass
    
def taka_af_bannlista():
    cls()
    kennitala = input("Kennitala/netfang: ")
    print("-"*len("Taka af bannlista: Jón Ólafsson, {}? (j/n): ".format(kennitala)))
    stadfesta = input("Taka af bannlista: Jón Ólafsson, {}? (j/n): ".format(kennitala))
    print("-"*len("Taka af bannlista: Jón Ólafsson, {}? (j/n): ".format(kennitala)))
    if stadfesta == "j":
        print("Jón Ólafsson hefur verið tekinn af bannlista.")
    else:
        print("Hætt við.")
    print("-"*len("Taka af bannlista: Jón Ólafsson, {}? (j/n): ".format(kennitala)))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass
    
def sekta_vidskiptavini():
    cls()
    kennitala = input("Kennitala/netfang: ")
    print("-"*len("Sekta: Jón Ólafsson, {}? (y/n)  ".format(kennitala)))
    stadfesta = input("Sekta: Jón Ólafsson, {}? (j/n): ".format(kennitala))
    print("-"*len("Sekta: Jón Ólafsson, {}? (y/n)  ".format(kennitala)))
    if(stadfesta == "j"):
        upphaed_sektar = input("Upphæð sektar: ")
        print("-"*len("Sekta: Jón Ólafsson, {}? (y/n)  ".format(kennitala)))
        print("Jón Ólafsson hefur verið sektaður um {} kr.".format(upphaed_sektar))
    else:
        print("Hætt við.") 
    print("-"*len("Sekta: Jón Ólafsson, {}? (y/n)  ".format(kennitala)))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def bilafloti_options():
    cls()
    print("Bílafloti")
    print("-"*len("2.  Birta útleigða bíla"))
    print("1.  Birta lausa bíla")
    print("2.  Birta útleigða bíla")
    print("3.  Skila bíl")
    print("4.  Skrá bíl")
    print("5.  Afskrá bíl")
    print("6.  Leita að bíl")
    print("7.  Bilaðir bílar")
    print("8.  Til baka")
    print("-"*len("2.  Birta útleigða bíla"))
    input_num = input("Val: ")
    if input_num == "1":
        birta_lausa_bila()
    elif input_num == "2":
        birta_utleigda_bila()
    elif input_num == "3":
        skila_bil()
    elif input_num == "4":
        skra_bil()
    elif input_num == "5":
        afskra_bil()
    elif input_num == "6":
        leita_ad_bil()
    elif input_num == "7":
        biladir_bilar()
    else:
        print_options()

def birta_lausa_bila():
    cls()
    dags_fyrri_string = input("Dagsetning leigu: ")
    print("-"*len("Dagsetning leigu: "))
    dags_seinni_string = input("Dagsetning skila: ")
    cls()
    print("Eftirfarandi bílar eru lausir frá {} til {}:".format(dags_fyrri_string, dags_seinni_string))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "2500 kr/dag"))
    print(60*"-")

    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass
    

def birta_utleigda_bila():
    cls()
    dags_fyrri_string = input("Dagsetning leigu: ")
    print("-"*len("Dagsetning leigu: "))
    dags_seinni_string = input("Dagsetning skila: ")
    cls()
    print("Eftirfarandi bílar eru í útleigu á tímabilinu frá {} til {}:".format(dags_fyrri_string, dags_seinni_string))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SX-452", "Jeppi", "2003", "Grænn", "3000 kr/dag"))
    print(60*"-")

    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def skila_bil():
    cls()
    bilnumer = input("Bílnúmer: ")
    print("-"*len("Bílnum {} hefur verið skilað!".format(bilnumer)))
    print("Bílnum {} hefur verið skilað!".format(bilnumer))
    print("-"*len("Bílnum {} hefur verið skilað!".format(bilnumer)))

    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def skra_bil():
    cls()
    bilnumer = input("Bílnúmer: ")
    print("-"*len("Bílnum {} hefur verið skráður!".format(bilnumer)))
    print("Bíllinn {} hefur verið skráður!".format(bilnumer))
    print("-"*len("Bílnum {} hefur verið skráður!".format(bilnumer)))

    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass
    #Hér eigum við eftir að bæta við virkni til þess að geyma lit, gerð, verð
    # og fleiri upplýsingar um bílinn sem myndu vera attributes í klasa

def afskra_bil():
    cls()
    bilnumer = input("Bílnúmer: ")
    print("-"*len("Bílnum {} hefur verið afskráður!".format(bilnumer)))
    print("Bíllinn {} hefur verið afskráður!".format(bilnumer))
    print("-"*len("Bílnum {} hefur verið afskráður!".format(bilnumer)))

    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def leita_ad_bil():
    cls()
    bilnumer = input("Bílnúmer: ")
    cls()
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format(bilnumer, "2003", "Jeppi", "Grænn", "3000 kr/dag"))
    print(60*"-")

    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def biladir_bilar():
    cls()
    print("Bilaðir bílar")
    print("-"*len("3.  Birta bilaða bíla"))
    print("1.  Skrá bíl")
    print("2.  Afskrá bíl")
    print("3.  Birta bilaða bíla")
    print("4.  Til baka")
    print("-"*len("3.  Birta bilaða bíla"))
    input_num = input("Val: ")

    if input_num == "1":
        skra_bilada_bil()
    elif input_num == "2":
        afskra_bilada_bil()
    elif input_num == "3":
        skoda_bil()
    else:
        print_options()

def skra_bilada_bil():
    cls()
    bilnumer = input("Bílnúmer: ")
    reason = input("Af hverju er hann bilaður? ")
    cls()
    print("Bíllinn {} hefur verið skráður sem bilaður.".format(bilnumer))
    print("-"*len("Bíllinn {} hefur verið skráður sem bilaður.".format(bilnumer)))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def afskra_bilada_bil():
    cls()
    bilnumer = input("Bílnúmer: ")
    cls()
    print("Bíllinn {} hefur verið skráður á ný.".format(bilnumer))
    print("-"*len("Bíllinn {} hefur verið skráður á ný.".format(bilnumer)))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def skoda_bil():
    cls()
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("GHY-234", "Fólksbíll", "2009", "Blár", "Vélarbilun"))
    print(60*"-")

    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def afgreidsla_options():
    cls()
    print("Afgreiðsla")
    print("-"*len("2.  Skrá nýjan viðskiptavin"))
    print("1.  Birta lausa bíla")
    print("2.  Skrá nýjan viðskiptavin")
    print("3.  Skrá pöntun")
    print("4.  Kostnaðarmat")
    print("5.  Skila bíl")
    print("6.  Afskrá viðskiptavin")
    print("7.  Bakfæra pöntun")
    print("8.  Uppfæra viðskiptavin") 
    print("9.  Breyta pöntun")
    print("10. Til baka")
    print("-"*len("2.  Skrá nýjan viðskiptavin"))
    input_num = input("Val: ")
    print()
    if input_num == "1":
        birta_lausa_bila()
    elif input_num == "2":
        skra_vidskiptavin()
    elif input_num == "3":
        skra_pontun()
    elif input_num == "4":
        kostnadarmat()
    elif input_num == "5":
        skila_bil()
    elif input_num == "6":
        afskra_vidskiptavin()
    elif input_num == "7":
        bakfaera_pontun()
    elif input_num == "8":
        breyta_vidskiptavin()
    elif input_num == "9":
        breyta_pontun()
    else:
        print_options()

def skra_pontun():
    cls()
    kt = input("Kennitala/netfang: ")
    print("-"*len("Kennitala/netfang: 1506992669"))
    print("Leigutímabil?")
    print("-"*len("Kennitala/netfang: 1506992669"))
    fra = input("Frá (YYYY, MM, DD): ")
    til = input("Til (YYYY, MM, DD): ")
    cls()
    print("Lausir bílar á leigutímabili ({}) - ({})".format(fra, til))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "2500 kr/dag"))
    print(60*"-")
    bilnumer = input("Veldu bíl (AA-X99) eða n til að hætta við: ")
    print(60*"-")
    
    if bilnumer.lower() == "n":
        print("Þú hefur hætt við að leigja út bíl.")
        print("-"*len("Þú hefur hætt við að leigja út bíl."))

        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass
    else:
        print("Áætlaður kostnaður án tryggingar: 45.000 kr.")
        print(60*"-")
        val = input("Samþykkja? (j/n): ")
        print(60*"-")

        if val.lower() == "j":
            trygging_check = input("Má bjóða þér aukatryggingu fyrir 500 kr. aukalega pr. dag? (j/n): ")
            print(60*"-")
            if trygging_check.lower() == "j":
                print("Lokaverð 50.000 kr.")
                val = input("Samþykkja? (j/n): ")
                print(60*"-")
                if val.lower() == "j":
                    print("Bíllinn",bilnumer,"hefur verið leigður út ({}) - ({})".format(fra, til))
                    print("-"*len("Bíllinn " + bilnumer + " hefur verið leigður út ({}) - ({})".format(fra, til)))
                    svar = input("Fara aftur á valmynd? (j/n): ")
                    if svar.lower() == "j":
                        print_options()
                    else:
                        pass
                else:
                    print("Þú hefur hætt við að leigja út bíl")
                    print(60*"-")

                    svar = input("Fara aftur á valmynd? (j/n): ")
                    if svar.lower() == "j":
                        print_options()
                    else:
                        pass
            else:
                print("Bíllinn",bilnumer,"hefur verið leigður út ({}) - ({})".format(fra, til))
                print(60*"-")

                svar = input("Fara aftur á valmynd? (j/n): ")
                if svar.lower() == "j":
                    print_options()
                else:
                    pass
        else:
            print("Þú hefur hætt við að leigja út bíl")
            print(60*"-")
            svar = input("Fara aftur á valmynd? (j/n): ")
            if svar.lower() == "j":
                print_options()
            else:
                pass

def kostnadarmat():
    cls()
    fra = input("Frá (YYYY, MM, DD): ")
    til = input("Til (YYYY, MM, DD): ")
    cls()
    # Hér er sett inn copy úr fallinu birta_lausa_bila()
    print("Eftirfarandi bílar eru lausir frá {} til {}:".format(fra, til))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
    print(60*"-")
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
    print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "4500 kr/dag"))
    print(60*"-")
    dummy_input = input("Bílnúmer: ")
    bill_verd = 4500
    dagur_a = fra.split(",")[2]
    dagur_a = int(dagur_a.strip())
    dagur_b = til.split(",")[2]
    dagur_b = int(dagur_b.strip())
    # vantar með mán en erum ekki með date svo læt þetta duga
    # birta_lausa_bila(fra, til) # fá hvaða bílar eru lausir
    # val = input("Veldu bíl (AA-X99): ")
    # við fáum tímabil frá fletta_pontun og mínusum fyrra tímabilið frá því seinna
    # þá fáum við hve marga daga viðkomandi hefur bílinn og margföldum dagana við dagskostnaðinn
    dagar = dagur_b - dagur_a + 1
    verd_samtals = dagar*bill_verd
    cls()
    print("Kostnaðarmat:", verd_samtals, "Kr.")
    print("-"*len("Kostnaðarmat: "+ str(verd_samtals) + " Kr."))

    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def pantanir_options():
    cls()
    print("Pantanir")
    print("-"*len("3.  Fletta upp pöntun"))
    print("1.  Skrá pöntun")
    print("2.  Breyta pöntun")
    print("3.  Fletta upp pöntun")
    print("4.  Bakfæra pöntun")
    print("5.  Til baka")
    print("-"*len("3.  Fletta upp pöntun"))
    input_num = input("Val: ")
    print()
    if input_num == "1":
        skra_pontun()
    elif input_num == "2":
        breyta_pontun()
    elif input_num == "3":
        fletta_pontun()
    elif input_num == "4":
        bakfaera_pontun()
    else:
        print_options()

def breyta_pontun():
    cls()
    kennitala = input("Hver er kennitalan/netfangið? ")
    cls()
    print("Hverju viltu breyta?")
    print("-"*len("Hverju viltu breyta?"))
    print("1. Dagsetningu")
    print("2. Bíl")
    print("3. Til baka")
    print("-"*len("Hverju viltu breyta?"))
    input_num = input("Val: ")

    cls()
    if input_num == "1":
        fra = input("Frá (YYYY, MM, DD): ")
        til = input("Til (YYYY, MM, DD): ")
        print("-"*len("Dagsetningu hefur verið breytt."))
        print("Dagsetningu hefur verið breytt.")
        print("-"*len("Dagsetningu hefur verið breytt."))
    
    elif input_num == "2":
        print("Eftirfarandi bílar eru lausir á tímabili þessarar pöntunar:")
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("Bílnúmer", "Tegund", "Árgerð", "Litur", "Verð"))
        print(60*"-")
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("SB-463", "Fólksbíll", "1998", "Rauður", "4500 kr/dag"))
        print("{:<12}{:<14}{:<8}{:<14}{:<12}".format("EU-N45", "Smábíll", "2014", "Grár", "2500 kr/dag"))
        print(60*"-")
        print("Núverandi bíll: SG-X69")
        bil = input("Nýr bíll: ")
        print(60*"-")
        print("Nýr bíll hefur verið valinn.")

    else:
        svar = input("Fara aftur á valmynd? (j/n): ")
        if svar.lower() == "j":
            print_options()
        else:
            pass
    
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass
    

def fletta_pontun():
    cls()
    kt = input("Kennitala/netfang pöntunar: ")
    cls()
    print("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt))
    print("SB-463 á tímabilinu 10/12/18 til 14/12/18")
    print("-"*len("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt)))
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def bakfaera_pontun():
    # fletta_pontun()
    cls()
    kt = input("Kennitala/netfang pöntunar: ")
    cls()
    print("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt))
    print("SB-463 á tímabilinu 10/12/18 til 14/12/18")
    print("-"*len("Viðskiptavinurinn Ásgeir Jónasson, {} hefur pantað bílinn".format(kt)))
    choice = input("Viltu eyða þessari pöntun? (j/n): ")
    cls()
    if(choice == "j"):
        print("Pöntuninni hefur verið eytt")
        print("---------------------------")
    else:
        print("Hætt við")
        print("--------")
    
    svar = input("Fara aftur á valmynd? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass

def main():
    print()
    print("Velkomin í Bílaleiguna IceCarRentals.")
    print("-"*37)
    n = 7
    print("{}        _______".format(" "*n))
    print("{}       //  ||\ \ ".format(" "*n))
    print("{}  ____//___||_\ \__".format(" "*n))
    print("{} )  _          _    \ ".format(" "*n))
    print("{} |_/ \________/ \___|".format(" "*n))
    print("{}___\_/________\_/_____".format(" "*n))
    print("{}Drive cheap, not safe!".format(" "*n))
    print("-"*37)
    svar = input("Keyra forrit? (j/n): ")
    if svar.lower() == "j":
        print_options()
    else:
        pass


main()