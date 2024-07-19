from Encryption import Encryption

def main():
    print("████████████████████████████████████████████████████████████████████████████")
    print("█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░█████████░░░░░░█████████░░░░░░░░░░░░░░█")
    print("█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█")
    print("█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█")
    print("█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█")
    print("█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█")
    print("█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█")
    print("█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█")
    print("█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█")
    print("█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█")
    print("█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█")
    print("█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█")
    print("████████████████████████████████████████████████████████████████████████████")
    print("Game ini adalah sebuah game yang mengaplikasikan konsep Caesar Cipher Encryption.")
    print("Tujuan dari game ini adalah untuk mendekripsikan kata yang sudah disediakan.")
    
    kunci_jawaban = "Python Program"
    encryption = Encryption(kunci_jawaban,12)
    soal = encryption.caesar_cipher()
    print("Kata yang harus didekripsi adalah: {0}".format(soal))
    jawaban = input("Jawaban anda: ")
    jika_benar = True
    while jika_benar:
        if jawaban == kunci_jawaban:
            jika_benar = False
            print("Selamat, Anda berhasil!")
        else:
            print("Jawaban anda kurang tepat, ayo coba lagi!")
            print("Kata yang harus didekripsi adalah: {0}".format(soal))
            jawaban = input("Jawaban anda: ")



if __name__ == "__main__":
    main() 