"""
Optimisasi algoritma pencarian menggunakan
Algoritma Genetik dengan masukan(input) berupa huruf abjad
Github Profile Account : https://github.com/Gaxriel/
Repository Link : https://github.com/Gaxriel/Algoritma-Genetik/
"""
import random

# Membuat list karakter-karakter abjad (KAPITAL) dan spasi
karakter = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Memberi bobot setiap karakter abjad dan membuat dictionary bobotnya
bobot_karakter = {}
"""
[spasi] = 0
A = 01; B = 02; C = 03; D = 04; E = 05;
F = 06; G = 07; H = 08; I = 09; J = 10;
K = 11; L = 12; M = 13; N = 14; O = 15;
P = 16; Q = 17; R = 18; S = 19; T = 20;
U = 21; V = 22; W = 23; X = 24; Y = 25;
Z = 26;
"""
for i in range(len(karakter)):
    bobot_karakter[karakter[i]] = i

# Input karakter sebagai target dan mengkapitalkan target yang diinput
target = input("Masukkan target anda : ").upper()

# Mendapatkan bobot target dan memasukkannya ke dalam list
bobot_target = []
for i in target:
    bobot_target.append(bobot_karakter[i])
    
"""
Daftar fungsi-fungsi Algoritma Genetika
"""
# Membuat kromosom(individu) baru
def buat_kromosom():
    kromosom_baru = []
    for i in range(len(bobot_target)):
        kromosom_baru.append(random.randint(0,len(karakter)-1))
    return kromosom_baru

# Perhitungan nilai fitness
def kalkulasi_fitness(kromosom, target):
    fitness = 0
    for i in range(len(target)):
        if kromosom[i] != target[i]:
            fitness += 1
    return fitness

# Sorting populasi berdasarkan nilai fitness yang terendah
def sort_populasi(size, fitness, populasi):
    for i in range(size):
        for j in range(size):
            if fitness[i] < fitness[j]:
                temp = fitness[i]
                fitness[i] = fitness[j]
                fitness[j] = temp
                temp = populasi[i]
                populasi[i] = populasi[j]
                populasi[j] = temp
    return fitness, populasi

# Teknik Cross Over (Mate) / Kawin Silang
def crossover(ortu1, ortu2):
    kromosom_anak = []

    for i in range(len(target)):
        probabilitas = random.random()
        if probabilitas < 0.45:
            kromosom_anak.append(ortu1[i])
        elif probabilitas < 0.90:
            kromosom_anak.append(ortu2[i])
        else:
            kromosom_anak.append(mutasi_gen())
    
    return kromosom_anak

# Teknik untuk inisialisasi mutasi gen baru
def mutasi_gen():
    return random.randint(0, len(karakter)-1)

"""
Mulai Metode ALGORITMA GENETIK
"""

generasi = 1
banyak_populasi = 6
populasi = []
fitness = []
stop = False
string_populasi = []

# Inisialisasi Populasi
for i in range(banyak_populasi):
    kromosom = buat_kromosom()
    populasi.append(kromosom)
    fitness.append(kalkulasi_fitness(kromosom, bobot_target))

# Menampilkan populasi awal
for i in range(len(populasi)):
    kar = ""
    for j in populasi[i]:
        kar = kar + karakter[j]
    string_populasi.append(kar)
print ("Populasi awal : " ,string_populasi)

# Jika fitness belum 0, maka stop akan selalu False dan perulangan akan berlanjut terus
while stop == False:
    
    # Sorting populasi
    sort_populasi(banyak_populasi, fitness, populasi)
    
    solusi = ""
    for i in populasi[0]:
        solusi = solusi + karakter[i]
    
    # Jika nilai fitness populasi pertama = 0, maka selesai
    if fitness[0] == 0:
        stop = True
        print ("Generasi ke - %d: %s dengan nilai fitness : %d" % (generasi, solusi, fitness[0]))
        break

    # Jika nilai fitness belum 0, maka generate populasi baru lagi dan nilai fitness baru
    generasi_baru = []
    fitness_baru = []

    # Lakukan teknik seleksi gen, sebanyak 50% populasi pertama akan bertahan ke generasi selanjutnya
    seleksi = (50*banyak_populasi)/100
    generasi_baru.extend(populasi[:seleksi])
    
    # Lakukan teknik crossover, sebanyak 50% populasi pertama akan disilangkan untuk memproduksi generasi baru
    s = (50*banyak_populasi)/100
    mate_rate = (50*banyak_populasi)/100
    for i in range(s):
        ortu1 = populasi[random.randint(0, mate_rate)]
        ortu2 = populasi[random.randint(0, mate_rate)]
        generasi_baru.append(crossover(ortu1, ortu2))

    # Menghitung nilai fitness dari generasi baru
    for i in range(len(generasi_baru)):
        fitness_baru.append(kalkulasi_fitness(generasi_baru[i], bobot_target))

    # Populasi generasi lama akan digantikan dengan populasi generasi baru
    populasi = generasi_baru
    fitness = fitness_baru

    print ("Generasi ke - %d: %s dengan nilai fitness : %d" % (generasi, solusi, fitness[0]))
    generasi += 1    
