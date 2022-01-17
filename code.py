from node import NodeTree
import os

# ba kelase zir be ezaye har character yek code binarry misazim va on ra dar dictionary gharar midahim
# sakhtare dictionary be soorate zir ast
# {
#   character:binary string   
# }
# baraye mesal:
# result = {
#   'c':'0001',
#   'b':'10111',
#   'y':'001011110'
# }
class CreateHuffmanCodes:
    def __init__(self):
        self.__string = ""
        self.__codes = {}
        self.__input_file=''
        self.__freq_file = open('Freq.txt','w')
        self.__tree_file = open('tree.txt','w')
        self.__codes_file = open('codes.txt','w')
    #    
    def Read_File(self,file_path):
        ##to ye halge binahayet say mikone file ro begire
        size, typ = self.fileSize(file_path, out = 'byte')
        size2, typ2 = self.fileSize(file_path, out = 'bit')
        
        while True:
            #file_path = input("[ + ] Give me path to a file : ")
            if os.path.exists(file_path):
                #print("file size : ",fileSize(file_path,out='kb'))
                print("\n[ + ] File Name : ", file_path)
                print("\n[ + ] File Size : " + str(size) + " " + str(typ) + " And " + str(size2) + " " + str(typ2))
                print("\n[ + ] File Contains " + str(int(size)) + " Characters")
                #print("file size : ",fileSize(file_path,out='bit'))
                break
            else:
                print("\n[ ! ] File not found")
        print("\n[ + ] Reading file contents ...")
        ##file baz mishe mohtavash ro dakhele motagayere contents rikhte mishe
        self.__input_file = open(file_path, 'r')
        content = self.__input_file.read()
        self.__input_file.close()
        return content
    ##
    def stringFormat(self,size, out = 'kb', precision = 2): 
        if out == 'kb':
             round(float(size)/1024, precision),out
        elif out == 'mb': 
            return round(float(size)/(1024 * 1024), precision),out
        elif out == 'gb':
             round(float(size)/(1024 * 1024 * 1024), precision),out
        elif out == 'byte':
            return round(float(size), precision),out
        elif out == 'bit':
            return round(float(size)*8, precision),out
        return False
    ## 
    def fileSize(self,filename, out = 'kb', precision = 4):  
        ##    with codecs.open(filename, 'r') as file:
        ##        string = file.read()
        ##        file.close()
        self.__input_file = open(filename, 'r')
        content = self.__input_file.read()
        self.__input_file.close()
        return self.stringFormat(len(content), out, precision)
    
    # mohasebeye tedade tekrare har character dar string ke dade shode
    def frequency(self):
        freq = {}
        for c in self.__string:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        ##        print("frequency not sort : ")
        ##        for key in freq.keys():
        ##            if key == '\n':
        ##                print(' ' * 2 + "'\\n'" + ' -> ' + str(freq[key]))
        ##            else:
        ##                print(' ' * 3 + "'" + key + "' -> " + str(freq[key]))
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        #print("[ + ] First Create list of")
        #print("[ + ] Frequency of characters of given file is :")
        #print("[ + ] this is sorted list\n")
        #print(' ' * 2 + 'char' + ' -> ' + 'freq')
        #print('-'*18)
        for i in range(len(freq)):
            if freq[i][0] == '\n':
                #print(' ' * 2 + "'\\n'" + ' -> ' + str(freq[i][1]))
                self.__freq_file.write(' ' * 2 + "'\\n'" + ' -> ' + str(freq[i][1]) + '\n')
            else:
                #print(' ' * 3 + "'" + freq[i][0] + "' -> " + str(freq[i][1]))
                self.__freq_file.write(' ' * 3 + "'" + freq[i][0] + "' -> " + str(freq[i][1]) + '\n')
        #print('_' * 70)
        #input('\nPress Any Key . . . \t')
        #print("\n\n[ + ] This is Huffman Tree \n\n")
        
        return freq
    ##    x={'a':2,'b':3,'c':1}
    ##    x=[('b', 3), ('a', 2), ('c', 1)]
        
    ##    sakhte derakht ba estefade az kelase NodeTree ke dar bala sakhtim
    ##    in function list frequency ro migire ke be sorate nozoli sort shode avalin onsor bishtarin tekrar
    ##    har bar ba 2 ta onsor akhar list ke kamtarin tekrar ro daran ye node misaze
    #  va left va right node ro barabar on 2 ta onsor mizare
    ##    badesh miad node jadid ke sakhte ro be list frequecy ezafe mikone
    #  va tedad tekrar node ro majmo tekrar haye on on 2 ta onsor akhar mizare
    def create_tree(self, freq):
        nodes = freq
        while len(nodes) > 1:
            ##akharin onsor list  key1:'c' c1:3 character c 3 bar tekrar shode
            key1, c1 = nodes[-1]
            ##do ta be akhar monde
            key2, c2 = nodes[-2]
            ##2 ta onsor akhar list ro hazf mikonim  
            nodes = nodes[:-2]
            ##ba in 2 ta onsor node misazim
            node = NodeTree(key1, key2)
            ##majmo tedad tekrar in 2 onsor ro ba nodesh be list ezafe mikonim
            nodes.append((node, c1 + c2))
            ##list ro be sorate makoos sort mikonim
            nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
            ##print("\nnodes : \n",nodes)
        return nodes

    # ba komake derakhte sakhte shode, be soorate bazgashti cod haye binary
    #  be ezaye har character misazim va dar dictionary gharar midahim
    def create_codes(self, node, left=True, binString="", MINUS=''):
        ##age type node string bashe binary string ro mosavi node mizarom
        if type(node) is str:
            return {node: binString}
        ##bachehaye node ro left va right mizarim
        (l, r) = node.children()
        ##dictionary mizarim
        d = dict()
        ##shoro mikonim be nemayeshe tree
        #print(' ' + MINUS + 'LEFT: ' + binString)
        self.__tree_file.write(' ' + MINUS + 'LEFT: ' + binString + '\n')
        ##be sorate bazgashti dictionary ro update mikonim
        ##be in sorat ke aval az root shoro mikonim va az samte chap ta payin tarin node tree mirim
        d.update(self.create_codes(l, True, binString + "0", MINUS + '---|'))
        #print(' ' + MINUS + 'RIGHT: ' + binString[:-1] + "1")
        self.__tree_file.write(' ' + MINUS + 'RIGHT: ' + binString[:-1] + "1" + '\n')
        ##sepas az samte rast edame midim
        d.update(self.create_codes(r, False, binString + "1", MINUS + '---|'))
        ##dictionary ro barmigardonim
        ##print("\ndictionary is : \n",d)
        return d

    # in function faghat baraye farakhaniye function haye private kelas mibashad
    def Generate(self, string=""):
        self.__string = string
        #print('_' * 70 + '\n')
        ##in function baray sakhtan code has ke ye tree migire va in tree ba list freqency sakhte shode
        t = self.create_codes(self.create_tree(self.frequency())[0][0])
        self.__codes = t
        #print('\n' + '_' * 70)
        for key in t.keys():
            if key == '\n':
                #print(' ' * 2 + "'\\n'" + ' -> ' + t[key] + ' : ' + str(len(t[key])))
                self.__codes_file.write(' ' * 2 + "'\\n'" + ' -> ' + t[key] + ' : ' + str(len(t[key])) + '\n')
            else:
                #print(' ' * 3 + "'" + key + "' -> " + t[key] + ' : ' + str(len(t[key])))
                self.__codes_file.write(' ' * 3 + "'" + key + "' -> " + t[key] + ' : ' + str(len(t[key])) + '\n')
        #print("\n[ + ] Codes is writing to the text file . . .")
        self.__tree_file.close()
        self.__codes_file.close()
        self.__freq_file.close()
        return t
    ##    
    def Compression_Percent_From_File_Content(self):
        Tedad_character = 0
        codes_len = 0
        ratio = 0
        for i in self.__string:
            Tedad_character += 1
            for key in self.__codes.keys():
                if i == key:
                    codes_len += len(self.__codes[key])
        print("\n[ + ] number of characters in content : ",Tedad_character," This means Byte")
        character_bits = Tedad_character * 8 
        #print("\n[ + ] characters bit in content : ",character_bits, " This means Bit")
        print("\n[ + ] length of characters code : ",codes_len/8, " This means Byte")
        #print("\n[ + ] Sorate kasr : ",float(character_bits - codes_len)," Makhraje kasr : ",float(character_bits))
        ratio = float(character_bits - codes_len)/float(character_bits)
        print("\n[ + ] Ratio : ",round((codes_len / 8)/Tedad_character,2))
        ratio_Percent = round(ratio * 100,2)
        print("\n[ + ] Compression Percentage : ",ratio_Percent,"%")
        #return ratio_Percent
