import os
from re import I
try:         
    print("*********************************")
    print(" Find File/Folder Last Modified ")
    print("*********************************")

    print("")

    # TYPE FILE 

    print("* Kosongi Jika Ingin Mencari Semua File/Folder")

    print("* Contoh .txt")

    print("")

    type_file = input("Type File : ")

    print("")

    # HIDDEN FILE 

    print("Masukan Ya/Tidak");

    print("")

    is_hidden_file = input("Termasuk File Yang Tersembunyi : ")

    print("")

    # TIME

    print("*Opsi Pilihan : ")
    print("Tahun -> Year")
    print("Bulan -> Month")
    print("Hari -> Day")
    print("Jam -> Hour")
    print("Menit -> Minute")

    print("")

    time = input("Jangka Waktu : ")

    print("")

    # TIME COUNT
    print("*Masukan Angka ")

    print("")

    time_count = int(input("Kurun Waktu : "))

    print("")

    if(type_file != ""):
        if(len(type_file) < 2):
            raise Exception("Type file tidak valid") 
        else:
            if(type_file[0] != "."):
                raise Exception("Type file tidak valid")

    if(is_hidden_file not in ["Ya","Tidak"]):
        raise Exception("Termasuk file yang tersembunyi harus Ya/Tidak")

    if(time not in ["Year","Month","Day","Hour","Minute"]):
        raise Exception("Jangka waktu tidak valid")

    print(f"Type File : {type_file}")
    print(f"Termasuk File Yang Tersembunyi : {is_hidden_file}")
    print(f"Jangka Waktu : {time}")
    print(f"Kurun Waktu : {time_count}")

    print("")

    print("Start")

    command = 'find'

    command += ' .'

    if(is_hidden_file == "Tidak"):
        if(type_file == ""):
            command += '/*'
        else:
            command += "/*"+type_file
    else:
        if(type_file != ""):
            command += "/*"+type_file            

    command += ' -newermt'

    command += ' "'+str(time_count)

    command += ' '+time.lower()  

    command += ' ago" -ls'
    
    print(command)

    os.chdir('/home/user')    

    os.system(command)

    print("End")

except Exception as e :
    print("")
    print("****")
    print(e)
    print("****")

