import sys


def calc(x, y, fn):
    """
    Performs a calculation based on the operation provided.

    Args:
        x: The first operand.
        y: The second operand.
        fn: The operation to perform (+, -, *, /, //, **, %).

    Returns:
        A string representing the result of the calculation or an error message.
    """
    if fn not in {"+", "-", "*", "/", "//", "**", "%"}:
        return "Lütfen geçerli bir işlem seçiniz!"

    if fn == "+":
        return f"{x} + {y} = {x + y}"
    elif fn == "-":
        return f"{x} - {y} = {x - y}"
    elif fn == "*":
        return f"{x} * {y} = {x * y}"
    elif fn == "/":
        if y == 0:
            return "Sıfıra bölme hatası!"
        return f"{x} / {y} = {x / y}"
    elif fn == "//":
        if y == 0:
            return "Sıfıra bölme hatası!"
        return f"{x} // {y} = {x // y}"
    elif fn == "**":
        return f"{x} ** {y} = {x ** y}"
    elif fn == "%":
        if y == 0:
            return "Sıfıra bölme hatası!"
        return f"{x} % {y} = {x % y}"
    





while True:
    user_menu_input= input ("1-İşlem Yapınız\n2-Programdan Çıkınız\nLütfen seçim yapınız: ")
    if user_menu_input == "1":
        try:
            # Kullanıcıdan giriş al
            # user_input = input("İşlem yapmak için aralara boşluk koyarak iki sayı ve işlem opratörü [format: <sayı1> <işlem> <sayı2>] giriniz veya ([q] ile çıkabilirsiniz): ")

            x = input("İlk sayısal değeri giriniz ('q' ile çıkabilirsiniz): ")
            if x.lower() == "q":  # Exit check
                print("Programdan çıkılıyor...")
                sys.exit()

            fn = input("Yapmak istediğiniz işlem operatörünü giriniz (+, -, *, /, //, **, % veya 'q' ile çıkabilirsiniz): ")
            if fn.lower() == "q":  # Exit check
                print("Programdan çıkılıyor...")
                sys.exit()

            y = input("İkinci sayısal değeri giriniz ('q' ile çıkabilirsiniz): ")
            if y.lower() == "q":  # Exit check
                print("Programdan çıkılıyor...")
                sys.exit()

            
            
            

            

            # # Verileri ayıkla ve işle
            # parts = user_input.split()
            # if len(parts) != 3:
            #     print("Lütfen şu formatta giriş yapın: <sayı1> <işlem> <sayı2> (örn: 5 + 3)")
            #     continue

            # x, fn, y = parts[0], parts[1], parts[2]


            

            # Sayılara dönüştür
            x = float(x)
            y = float(y)

            # Hesaplama yap ve sonucu yazdır
            result = calc(x, y, fn)
            print(result)

        except ValueError:
            print("Hatalı giriş! Sayılar ve geçerli bir işlem kullanınız.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

    elif user_menu_input == "2":    #menü çıkış kontrolü
        print("Programdan çıkılıyor...")
        break
    else:
        print("Hatalı Menü Seçimi yaptınız!")





