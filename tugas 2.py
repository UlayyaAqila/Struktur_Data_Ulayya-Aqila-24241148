print("Nama:Ulayya Aqilah Nim : 24241148")

inputUser = int(input("masukan angka yang bernilai kurang dari 24 atau lebih besar dari 48:"))

#+++++24-------------
#memeriksa angka kurang dari 24
iskurangdari = (inputUser <24)

#memeriksa angka lebih dari 48
islebihdari = (inputUser >48)

final = iskurangdari or islebihdari
print("angka yang anda masukan :",final)