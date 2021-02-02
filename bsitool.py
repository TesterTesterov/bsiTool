import sys
test_flag = False

if (test_flag):
    zlo = open("en._bsi", 'rb')
    dobro = open("en_._bsi", 'rb')
    one = zlo.read(1)
    two = dobro.read(1)
    count = 0
    while ((one != b'') and (two != b'')):
        if (one != two):
            print(count)
            break
        one = zlo.read(1)
        two = dobro.read(1)
        count += 1
    zlo.close()
    dobro.close()
    exit()

String = ''
Mode = 0
try:
    Mode = int(input("Декодировать (0), кодировать (1):/Decode (0), encode (1): "))
    if ((Mode != 0) and (Mode != 1)):
        raise Exception("Караул!")
except:
    print("Ошибка! Некорректное значение!/Error! Incorrect value!")
    input()
    sys.exit()

global InFile
global OutFile
FileString = input("Введите название файла:/Input file name: ")
if (Mode == 0):
    FileNewString = FileString + ".txt"
    try:
        InFile = open(FileString, 'rb')
        OutFile = open(FileNewString, 'w', encoding="utf-8")
        Bytes = InFile.read()
        InFile.close()
        Ukaz = 0
        Neo = 0
        End = len(Bytes)
        try:
            while (Neo < End):
                if (Bytes[Neo] == 0x00):
                    truth = 1
                    try:
                        if (Bytes[Neo-1] == 0x00):
                            truth = 0
                    except:
                        pass
                    if (truth == 1):
                        try:
                            test = Bytes[Ukaz:Neo].decode('utf-8')
                            OutFile.write(test)
                        except:
                            OutFile.write("@" + Bytes[Ukaz:Neo].hex(' '))
                    OutFile.write('\n###SEP###\n')
                    Ukaz = Neo+1
                    pass
                Neo += 1
        except:
            print(Bytes[Ukaz:Neo], Neo)
            print("Ошибка декодировки!")
            input()
            sys.exit()
        OutFile.close()
    except:
        print("Ошибка! Такого файла нет!/Error! No such file!")
        input()
        sys.exit()
else:
    try:
        FileNewString = FileString[:-4]
    except:
        input()
        print("Ошибка! Неправильный файл!")
        sys.exit()
    try:
        InFile = open(FileString, 'r', encoding="utf-8")
        OutFile = open(FileNewString, 'wb')
        lines = InFile.readlines()
        InFile.close()
        down = ''
        linenum = 0

        while (linenum < len(lines)):
            line = lines[linenum]

            if (line == '###SEP###\n'):
                ifer = True
                try:
                    if (down[0] == '@'):
                        down = down[1:]
                        OutFile.write(bytearray.fromhex(down))
                        ifer = False
                except:
                    pass
                else:
                    try:
                        if (down[-1] == '\n'):
                            down = down[:-1]
                    except:
                        pass
                    if (ifer):
                        OutFile.write(bytearray(down.encode('utf-8')))
                OutFile.write(bytearray(b'\x00'))
                down = ''
            else:
                down += line
            linenum += 1
        OutFile.close()
    except:
        print("Ошибка! Такого файла нет!/Error! No such file!")
        input()
        sys.exit()
