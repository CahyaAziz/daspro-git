# Nama  : Cahya Abdul Aziz
# NIM   : 2404096
# Kelas : 1C

def login():
    chance = 5
    while True:
        user = input("Username: ")
        password = input("Password: ")
        if user == "Daspro2023" and password == "Latihan":
            return True
        else:
            chance -= 1
            if chance == 0:
                break
            print(f"Username atau Password salah! Sisa percobaan anda {chance} kali lagi!\n")
    return False

if login():
    print("Login berhasil!")
else:
    print("Terlalu banyak percobaan salah!")

    