from node import NodeTree
from code import CreateHuffmanCodes
from compress import HuffmanCompression
from datetime import datetime as time
import os

os.system('cls')
file_path = 'bootstrap.min.css.map'

while True:
    print("\n\t\t\t  ------- Information Security Project --------- ")
    # print("\t\t\t | \t\t\t\t\t\t|")
    # print("\t\t\t | \tFile Name :  " + file_path + "\t| ")
    print("\t\t\t | \t\t\t\t\t\t|")
    print(
        "\t\t\t | \t1. Read File \t\t\t\t| \n\t\t\t | \t2. Generate \t\t\t\t| \n\t\t\t | \t _ Characters Frequency \t\t|\n\t\t\t | \t _ Huffman Tree \t\t\t|")
    print("\t\t\t | \t _ Huffman Codes \t\t\t| \n\t\t\t | \t3. Compress \t\t\t\t| \n\t\t\t | \t4. Percentage \t\t\t\t|")
    print("\t\t\t | \t5. DeCompress \t\t\t\t|\n\t\t\t | \t6. Exit \t\t\t\t|")
    print("\t\t\t | \t\t\t\t\t\t|")
    print("\t\t\t  ---------------------------------------------- ")
    choice = int(input("\n\t\t\t Enter Number :\t"))
    os.system('cls')
    if choice == 1:
        print(" ---------------------------------------- ")
        print("|  File is Reading . . .\t\t |")
        print(" ---------------------------------------- ")
        time1 = time.now()
        ##ye object az class create code huffman misazim
        code = CreateHuffmanCodes()
        # file_path = 'bootstrap.js'
        contents = code.Read_File(file_path)
        time2 = time.now()
        total = time2 - time1
        print("\n[ + ] Training Time is : ", float(total.total_seconds()), " Seconds")
        input("\n\nPress Any Key To Go Menu  . . . \t")
        os.system('cls')
    elif choice == 2:
        print(" ---------------------------------------- ")
        print(" | Generate . . .  \t\t\t|")
        print(" ---------------------------------------- ")
        time1 = time.now()
        print("\n [ + ] 1. Loading Frequency Of Characters")
        print("\n [ + ] 2. Creating Tree")
        print("\n [ + ] 3. Adding Codes to Each Character")
        print("\n [ * ] 4. Write Output of Each Function To Text File")
        ##ba mohtavaye dade shode class shoro be sakht tree va code ha mikonad
        patern = code.Generate(string=contents)
        time2 = time.now()
        total = time2 - time1
        print("\n [ + ] Training Time is : ", float(total.total_seconds()), " Seconds")
        input("\n\nPress Any Key To Go Menu  . . . \t")
        os.system('cls')
    elif choice == 3:
        print(" ---------------------------------------- ")
        print(" | Compressing . . . \t\t\t|")
        print(" ---------------------------------------- ")
        time1 = time.now()
        ##ye object az class compression huffmanmisazim va paterno midim besh
        d_or_c_ompressor = HuffmanCompression(patern=patern)
        compressed = d_or_c_ompressor.Compress(contents)
        print("\n[ + ] Compressing Content to the output Text file ...")
        print("\n[ * ] Finish ...")
        print("\n[ + ] Compressed File Size is : ", os.path.getsize(d_or_c_ompressor.compressed_file_path) / 8,
              " bytes")
        time2 = time.now()
        total = time2 - time1
        print("\n[ + ] Training Time is : ", round(total.total_seconds(), 3), " Seconds")
        input("\n\nPress Any Key To Go Menu  . . . \t")
        os.system('cls')
    elif choice == 4:
        print(" ---------------------------------------- ")
        print(" | Compression Percentage . . .  \t|")
        print(" ---------------------------------------- ")
        time1 = time.now()
        print("\n[ * ] 1. Calculating Compression Percentage From Size of input And output Files\n")
        d_or_c_ompressor.Compression_Percent_From_File_Size(file_path)
        time2 = time.now()
        total = time2 - time1
        print("\n[ + ] Training Time is : ", round(total.total_seconds(), 3), " Seconds")
        time1 = time.now()
        print("\n[ * ] 2. Calculating Compression Percentage From input File Contents . . .")
        c_rate = code.Compression_Percent_From_File_Content()
        # print('\n[ + ] Compression rate: %f'%(c_rate*100)+' %')
        time2 = time.now()
        total = time2 - time1
        print("\n[ + ] Training Time is : ", float(total.total_seconds()), " Seconds")
        input("\n\nPress Any Key To Go Menu  . . . \t")
        os.system('cls')
    elif choice == 5:
        print(" ---------------------------------------- ")
        print(" | Decompressing  . . . \t\t|")
        print(" ---------------------------------------- ")
        time1 = time.now()
        ##bad hamon code compress shode ro midim besh decompress mikone va stringo barmigardone
        print("\n[ + ] Decompressing to the output file ...")
        de_compressed = d_or_c_ompressor.Decompress(compressed)
        # print("[ + ] Result: " + de_compressed)
        print("\n[ * ] Finish ...")
        # print("\n[ + ] deCompressed File Size is : ",code.stringFormat(len(de_compressed),out='byte'))
        print("\n[ + ] deCompressed File Size is : ", os.path.getsize(d_or_c_ompressor.decompressed_file_path),
              " bytes")
        time2 = time.now()
        total = time2 - time1
        print("\n[ + ] Training Time is : ", float(total.total_seconds()), " Seconds")
        input("\n\nPress Any Key To Go Menu  . . . \t")
        os.system('cls')
    else:
        exit()
