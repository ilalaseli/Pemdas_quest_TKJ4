#tipe data koleksi

koleksi_data_str = ["suginem warteg", "samsul arip", "ferdi dowhill", "alibapa icikiwir"]

koleksi_data_int = [200, 300, 400, 500]

koleksi_data_mix = ["rusdi batagor", 400, True, "agung bismarck"]

print("Koleksi data String:", koleksi_data_str)

print("Koleksi data Integer:", koleksi_data_int)

print("Koleksi data Campuran:", koleksi_data_mix)



# Buatlah 3 kumpulan data: Nama Hewan, Nilai UTS, Nama Teman sebangku kalian

nama_hewan = ["klomang", "rodriguez", "kelinci", "icikiwir"]

nilai_uts = [80,90,100,95]

teman_sebangku = ["apran hololaip", "rifki kodoksan", "angga stlouis", "ilal belfast"]

print("nama nama hewan:", nama_hewan)

print("nilai uts saya:", nilai_uts)

print("nama teman sebangku:", teman_sebangku)

# Data ke 2 nama hewan

print("Data ke-2 nama hewan:", nama_hewan[1])

# Data pertama Nilai UTS

print("Data Pertama Nilai UTS:", nilai_uts[0])

# Data terakhir nama teman sebangku

print("Data Terakhir Nama Teman Sebangku:", teman_sebangku[3])

# Tambahkan 1 data disetiap data koleksi

nama_hewan.append("ookami")
nilai_uts.append(30)
teman_sebangku.append("shoukaku")

# Ubahlah data terakhir nilai UTS

nilai_uts[-1] = 30
print(nilai_uts)

# Ubahlah data ke-3 nama hewan

nama_hewan[2] = "shiroko"
print(nama_hewan)

