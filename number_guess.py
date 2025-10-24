import random

def sayi_tahmin_oyunu():
    print("Sayı Tahmin Oyununa Hoşgeldin!")
    print("1 ile 100 arasında bir sayı tuttum, bakalım tahmin edebilecek misin?")

    dogru_sayi = random.randint(1, 100)
    tahmin_hakki = 10

    while tahmin_hakki > 0:
        try:
            tahmin = int(input(f"{tahmin_hakki} tahmin hakkın kaldı. Tahminin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")
            continue

        if tahmin < dogru_sayi:
            print("Daha büyük bir sayı söyle.")
        elif tahmin > dogru_sayi:
            print("Daha küçük bir sayı söyle.")
        else:
            print(f"Tebrikler! Doğru sayı {dogru_sayi} idi.")
            break

        tahmin_hakki -= 1

    if tahmin_hakki == 0:
        print(f"Maalesef tahmin hakların bitti. Doğru sayı {dogru_sayi} idi.")

if __name__ == "__main__":
    sayi_tahmin_oyunu()
