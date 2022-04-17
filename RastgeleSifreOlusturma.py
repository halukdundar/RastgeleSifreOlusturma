import random

Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
 
password_len = int(input("ŞİFRE KAÇ KARAKTERTEN OLUŞTURULACAK, LÜTFEN GİRİN: "))
password_count = int(input("KAÇ ADET ŞİFRE OLUŞTURULSUN: "))
for x in range(0, password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(Chars)
            password      = password + password_char
        print("RASTGELE ŞİFRENİZ : " , password)