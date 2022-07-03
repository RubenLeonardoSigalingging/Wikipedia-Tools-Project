#!/usr/bin/env python3


# Wikipedia Tools Project
def Wikipedia_Tools_Project(Created_By="Ruben Leonardo Sigalingging"):
	import os
	from os import system
	# system("pip install wikipedia")
	# system("pip install pyfiglet")
	system("clear")
	import wikipedia


	# PILIH BAHASA YANG AKAN KAMU GUNAKAN,
	# MODUL WIKIPEDIA MENDUKUNG 444 BAHASA DI DUNIA.
	# KEREN BRO, EAAA
	# Languages supported.
	pilih_bahasa_yang_akan_kamu_gunakan=str(input("---PILIH BAHASA---\n\n[!] English: 'en'\n[!] Indonesian: 'id'\n[!] Italian: 'it'\n[!] Japanese: 'ja'\n[!] Kannada: 'kn'\n[!] Kazakhstan: 'kk'\n[!] Korean: 'ko'\n[!] Latin: 'la'\n[!] Malaysia: 'ms'\n[!] Portuguese: 'pt'\n[!] Romanian: 'ro'\n[!] Russian: 'ru'\n[!] Spanish: 'es'\n[!] Ukrainian: 'uk'\n[!] German: 'de'\n\n[!] PILIH DISINI: "))
	pilih_bahasa_yang_akan_kamu_gunakan=wikipedia.set_lang(pilih_bahasa_yang_akan_kamu_gunakan)


	# METODE PENCARIAN MODUL WIKIPEDIA.
	print("\n")
	from wikipedia import search
	apa_yang_ingin_kamu_cari=str(input("[!] Apa Yang Ingin Kamu Cari: "))
	apa_yang_ingin_kamu_cari=search(apa_yang_ingin_kamu_cari)
	# print(f"[!] Hasil: {apa_yang_ingin_kamu_cari[1]}")
	# print(f"[!] Hasil: {apa_yang_ingin_kamu_cari}")
	# BUAT PERULANGAN ATAU FOR LOOP.
	for hasil_pencarian in apa_yang_ingin_kamu_cari:
		print(f"[!] Hasil: {hasil_pencarian}")
	print("\n\n")


	# UNTUK MENDAPATKAN RINGKASAN ARTIKEL, AKU MENGGUNAKAN METODE:
	# .SUMMARY()
	print("\n\n")
	from wikipedia import summary
	apa_yang_ingin_kamu_cari=str(input("[!] Dapatkan Ringkasan Artikel Dari: "))
	print("\n")
	apa_yang_ingin_kamu_cari=summary(apa_yang_ingin_kamu_cari)
	print(f"[!] Hasil Ringkasan Artikel: {apa_yang_ingin_kamu_cari}")
Wikipedia_Tools_Project()