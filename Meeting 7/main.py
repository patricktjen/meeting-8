from Encryption import Encryption

def main():
    print("Selamat datang, game ini adalah sebuah game yang mengaplikasikan konsep Caesar Cipher Encryption.")
    print("██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░")
    print("██░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗")
    print("███████║█████╗░░██║░░░░░██║░░░░░██║░░██║")
    print("██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║")
    print("██║░░██║███████╗███████╗███████╗╚█████╔╝")
    print("╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░")
    kunci_jawaban = "Finish"
    encryption = Encryption(kunci_jawaban,5)
    soal = encryption.caesar_cipher()
    print("Kata yang harus didekripsi adalah: {0}".format(soal))
    jawaban = input("Jawaban anda: ")
    jika_benar = True
    while jika_benar:
        if jawaban == kunci_jawaban:
            jika_benar = False
            print("Game Over, You Won!")
        else:
            print("Kata yang harus didekripsi adalah: {0}".format(soal))
            jawaban = input("Jawaban anda: ")



if __name__ == "__main__":
    main()

