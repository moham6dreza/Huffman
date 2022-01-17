from code import CreateHuffmanCodes
import os

# ba komake kelase zir mitavanim ba dadane yek patern be an, yek string ra compress konim
# masalan agar paterne ma be soorate zir bashad:
# patern = {
#   'a':'001',
#   'b':'10',
#   'c':'111'
# }
# angah stringe zir be soorate zir compress mishavad:
# string = 'aabbccc'
#
#               a    a       b     b      c      c      c
# compressed = 001  001     10    10     111    111    111       pass compress = 0010011010111111
class HuffmanCompression:
    ##class ye patern migire bala tozih dadam
    def __init__(self, patern={}):
        self.__patern = patern
        self.compressed_file_path = 'compressedfile.txt'
        self.decompressed_file_path = 'decompressedfile.txt'
        self.__compressed_file = open(self.compressed_file_path,'w')
        self.__decompressed_file = open(self.decompressed_file_path,'w')
    ##in function test mikone age string 0 ya 1 nabashe false mide
    def __is_compressed_string(self, string=''):
        for ch in string:
            if ch != '0' and ch != '1':
                return False
        return True
    ##in func ye value migire dakhele patern check mikone age ono dashte bashe barmigardone
    def __key_of_this_value(self, value=''):
        for ch in self.__patern.keys():
            if self.__patern[ch] == value:
                return ch
    ##in func ye string migire mesle aabbccc va binary string ono barmigardone
    def Compress(self, string=""):
        result = ""
        for ch in string:
            result += self.__patern[ch]
        self.__compressed_file.write(result)
        self.__compressed_file.close()
        return result

    def Compression_Percent_From_File_Size(self ,input_path):
        output_path = self.compressed_file_path
        before_size = os.path.getsize(input_path)
        after_size = os.path.getsize(output_path)
        after_size /= 8
        compression_percent = round(100 - after_size / before_size * 100, 2)
        print("[ + ] a. File Size ( Before ) : ", before_size, "Bytes")
        print("\n[ + ] b. File Size ( After ) : ", after_size, "Bytes")
        print("\n[ + ] c. Ratio : ",round(after_size/before_size,2))
        print("\n[ + ] d. Compression Percent : ",compression_percent, "%")
        #print(f"[ + ] a. File Before Size : {before_size} bytes\n\n[ + ] b. File After Size : {after_size} bytes "
        #    f"\n\n[ + ] c. Compression Ratio : {compression_percent} %")
    ##in tabe string migire aval check mikone age compress string bashe(0 1 bashe)
    ##be ezaye har binary code dakhele string check mikone age on code dakhele patern bashe key ono be result ezafe mikone
    def Decompress(self, string=""):
        if not self.__is_compressed_string(string):
            print('[ Err In Decompression ] This is not a Huffman compressed cipher')
            return ''
        else:
            result = ""
            temp_string = ""
            for ch in string:
                temp_string += ch
                if temp_string in self.__patern.values():
                    result += self.__key_of_this_value(temp_string)
                    temp_string = ''
            self.__decompressed_file.write(result)
            self.__decompressed_file.close()
            return result 
