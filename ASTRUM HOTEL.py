
xonalar = {
    1: {"holat": "bo'sh", "tur": "Lyuks"},
    2: {"holat": "bo'sh", "tur": "Standart"},
    3: {"holat": "bo'sh", "tur": "Standart"},
    4: {"holat": "bo'sh", "tur": "Ekonom"},
    5: {"holat": "bo'sh", "tur": "Ekonom"},
}
print("📣📣📣📣📣📣📣  ASTRUM MEHMONXONAMIZGA XUSH KELIBSIZ")

def xona_band_qil(xona_raqami, mehmon_ismi):
    xonalar[xona_raqami]["holat"] = mehmon_ismi
    print(f"{xona_raqami}-xona {mehmon_ismi} uchun band qilindi ({xonalar[xona_raqami]['tur']}).")

def xonalar_korsat():
    print("\nXonalar holati:")
    for xona, malumot in xonalar.items():
        print(f"{xona}-xona ({malumot['tur']}): {malumot['holat']}")

while True:
    print("\n1. Mehmon qo'shish🆕")
    print("2. Mehmonni chiqarish🆓")
    print("3. Xonalar holatini ko'rish🧐")
    print("4. Dasturdan chiqish➡️")

    tanlov = input("Tanlovingizni kiriting (1-4): ")

    if tanlov == "1":
        xona_tur = input("Xona turini tanlang (Lyuks, Standart, Ekonom): ").capitalize()
        mavjud_xonalar = [xona for xona, malumot in xonalar.items() if malumot["tur"] == xona_tur]

        if mavjud_xonalar:
            while True:
                print(f"Mavjud xonalar: {[xona for xona in mavjud_xonalar]}")
                xona_raqami = input("Xona raqamini kiriting: ")
                if xona_raqami.isdigit():
                    xona_raqami = int(xona_raqami)
                    if xona_raqami in mavjud_xonalar:
                        if xonalar[xona_raqami]["holat"] == "bo'sh":
                            mehmon_ismi = input("Mehmonning ismini kiriting: ")
                            xona_band_qil(xona_raqami, mehmon_ismi)
                            break
                        else:
                            print(f"{xona_raqami}-xona band. Iltimos, boshqa xona tanlang.")
                    else:
                        print("Tanlangan xona noto'g'ri!")
                else:
                    print("Iltimos, to'g'ri xona raqamini kiriting!")
        else:
            print(f"{xona_tur} turidagi xonalar mavjud emas yoki band.")

    elif tanlov == "2":
        xona_raqami = input("Xona raqamini kiriting (1-5): ")
        if xona_raqami.isdigit():
            xona_raqami = int(xona_raqami)
            if xona_raqami in xonalar:
                if xonalar[xona_raqami]["holat"] != "bo'sh":
                    oldingi_mehmon = xonalar[xona_raqami]["holat"]
                    xonalar[xona_raqami]["holat"] = "bo'sh"
                    print(f"{xona_raqami}-xona bo'shatildi. Oldingi mehmon: {oldingi_mehmon}.")
                else:
                    print(f"{xona_raqami}-xona allaqachon bo'sh.")
            else:
                print("Noto'g'ri xona raqami!")
        else:
            print("Iltimos, to'g'ri xona raqamini kiriting!")

    elif tanlov == "3":
        xonalar_korsat()

    elif tanlov == "4":
        print("Dastur to'xtatildi. Xayr!")
        break

    else:
        print("Noto'g'ri tanlov, qaytadan urinib ko'ring!")
