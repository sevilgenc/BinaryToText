import os
files = os.listdir('C:/pythonProject/Kartaca') #Klasördeki .txt dosyalarını listele

for i in range(1,len(files)): #liste uzunluğunca işlem devam etsin
    a = open("{}".format(files[i])) #dosyayı aç
    file = a.read() #dosyayı oku
    binary_values = file.split()
    ascii_string = ""

    for binary_value in binary_values:
        an_integer = int(binary_value, 2) #ikilik tabandan ondalık tabana çevirir
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    print(ascii_string)
