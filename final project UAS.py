# Kelompok 3 Struktur Data
mahasiswa = {
    "Ulayya Aqilah": "24241148",
    "Baiq Leti Mutia Hasira Putri": "24241135",
    "Baiq Abdalis Sani": "24241127"
}

# Menampilkan Kelompok
print("Anggota Kelompok 3:")
for nama, nim in mahasiswa.items():
    print(f"Nama: {nama} | NIM: {nim}")

def meet1():
    print("\n=== Meet 1: Tabel Kebenaran ===")
    print("A\tB\tAND\tOR\tNOT A")
    for a in [True, False]:
        for b in [True, False]:
            print(f"{a}\t{b}\t{a and b}\t{a or b}\t{not a}")

def meet2():
    print("\n=== Meet 2: Logika Input Angka ===")
    angka = int(input("Masukkan sebuah angka: "))
    if angka > 0:
        print("Angka positif")
    elif angka < 0:
        print("Angka negatif")
    else:
        print("Angka nol")

def meet3():
    print("\n=== Meet 3: Nilai Kuliah ===")
    nilai = float(input("Masukkan nilai Anda (0-100): "))
    if nilai >= 85:
        grade = 'A'
    elif nilai >= 70:
        grade = 'B'
    elif nilai >= 60:
        grade = 'C'
    elif nilai >= 50:
        grade = 'D'
    else:
        grade = 'E'
    print("Grade Anda:", grade)

def meet4():
    print("\n=== Meet 4: Cek Umur ===")
    umur = int(input("Masukkan umur Anda: "))
    if umur >= 18:
        print("Anda sudah dewasa.")
    else:
        print("Anda masih anak-anak.")

def meet5():
    print("\n=== Meet 5: Cek Password ===")
    password = input("Masukkan password: ")
    if password == "admin123":
        print("Akses diterima!")
    else:
        print("Password salah!")

def meet6():
    print("\n=== Meet 6: String Angka ===")
    string_angka = input("Masukkan angka dalam bentuk string: ")
    if string_angka.isdigit():
        angka = int(string_angka)
        print("Angka yang dimasukkan:", angka)
    else:
        print("Input bukan angka valid.")

def meet7():
    print("\n=== Meet 7: Pemisah Domain ===")
    email = input("Masukkan email: ")
    if "@" in email:
        username, domain = email.split("@")
        print("Username:", username)
        print("Domain:", domain)
    else:
        print("Email tidak valid.")

def meet8():
    print("\n=== Meet 8: Pembulatan Harga ===")
    harga = float(input("Masukkan harga: "))
    pembulatan = round(harga, -3)  # pembulatan ke ribuan terdekat
    print(f"Harga setelah dibulatkan: Rp{pembulatan:,.0f}")

# Menu utama
def main():
    while True:
        print("\n=== Final Project: Daftar Program ===")
        print("1. Meet1 - Tabel Kebenaran")
        print("2. Meet2 - Logika Input Angka")
        print("3. Meet3 - Nilai Kuliah")
        print("4. Meet4 - Cek Umur")
        print("5. Meet5 - Cek Password")
        print("6. Meet6 - String Angka")
        print("7. Meet7 - Pemisah Domain")
        print("8. Meet8 - Pembulatan Harga")
        print("9. Keluar")

        pilihan = input("\nMasukkan nomor program yang ingin dijalankan: ")
        if pilihan == '1':
            meet1()
        elif pilihan == '2':
            meet2()
        elif pilihan == '3':
            meet3()
        elif pilihan == '4':
            meet4()
        elif pilihan == '5':
            meet5()
        elif pilihan == '6':
            meet6()
        elif pilihan == '7':
            meet7()
        elif pilihan == '8':
            meet8()
        elif pilihan == '9':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Jalankan program
if __name__ == "__main__":
    main()
