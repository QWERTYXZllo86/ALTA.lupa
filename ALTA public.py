import sys, re, os, shutil, random, zipfile, statistics, math
if os.name != "nt": #уже давно не поверял под линукс так-что поставил это
    print("ALTA не проверяется под linux и других системах")
    print("Если она вылетает то пишите ко мне Prosto_Maksim")
    input("Enter - для продолжения...")
def clear(mode): #Ну даже не знаю??? что это делает??? :D
    os.system('cls' if os.name == 'nt' else 'clear') 
    if mode != "0": #Если не авто чистка, то показать версию.
        print("Versions ALTA v5.2 by Prosto_Maksim")
print("loading.    1/26")

def Placal(folder,data): #Писал пиздец давно, так-что помню только часть, еще писал на приколе(пришлось переменные другими именами называть :D )
    hardest = 1 #по название доложно понятно быть)
    if folder == "0":
        try:
            folder = input("Drag the file here>").replace('"', '')
        except KeyboardInterrupt:
            sys.exit()
    try:
        file = open(folder, 'r')
    except FileNotFoundError:
        if data == "1":
            print("Not found in db")
        else:
            print("File not found or cannot be read")
        return 0
    
    pp = 0
    Scan = 1
    
    print("Player:" + file.readline().rstrip('\n')) #Показывает какой игрок
    
    while Scan == 1:
        pp1 = re.findall(r'\d+', file.readline().rstrip(' ').rstrip('\n').rstrip(':'))
        
        try:
            lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
        except IndexError:
            print("file is corrupted")
            return 0
        
        if lvl != 0:
            pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
            hardest = hardest + 1
        
        if lvl == 0:
            Scan = 0
    print("PP:" + str(round(pp)))
    
    file.close()
    Scan = "1"
    file = open(folder, 'r')
    file.readline().rstrip('\n') #Убирает данные о имени игрока
    total = 0
    hardest = 1
    
    while Scan != "0": #Повторно обротока для вывода % от всех лвлов
            
            if Scan != "0":
                total = 0.85**(hardest-1) #Формула расчета % для вывода)
                Scan = file.readline().rstrip('\n') #Чтение строки из файла
                if Scan != "0":
                    print(str(Scan) + "pp " + str(round(total * 100, 2)) + "%")
                hardest = hardest + 1
            
            if Scan == "0": #if else лень :D
                Scan = "0"
                if data == "0":
                    print("все!")
                file.close()
clear("0")
print("loading..   2/26")

def lvlcal(fps,Timings,seting):
    Referencepoint = 40000
    Сounter = 0 #Сетчик таймингов
    HardestC = 99999999 #Сетчик самого сложного тайминга
    Mior = 0 #ср тайминг
    FreeC = 0
    point = 0
    Compression = 216
    Mior = 0
    if Timings == "0": #если ничего нет, то повторно попросить вести тайминги.
        print("\nMark - Invisible timings = timing itself / 2(Rounding up to the side)")
        print("Mark - Any clicks that simply need to be pressed in advance should not be taken into account in any way")
        print("Mark - If the timings are too simple, set the FPS lower")
        print("Mark - If you have 0 frames, set the fps higher")        
        print("Timings are written like this - \n timing;Timing;Timing;Timing | example 1;3;56;1;3")        

        try:
            Timings = input(">")
        except ValueError:
            print("Wrong format!")
            return 0
        except KeyboardInterrupt:
            sys.exit()
    Timings = str(Timings)
    for Timing in Timings.split(";"): #Делаем масив по ; и сразу заходим в цикл for
        try:
            mc = 1000 / (int(fps) / int(Timing)) #считает время тайминга
        except ZeroDivisionError:
            print("Impossible lvl!")
            return 0
        except ValueError:
            print("This is exactly the timing?")
            return 0
        if mc <= 40:
            point = point + (Referencepoint / (mc/1.05)) #считаем баллы за время тайминга
        elif mc >= 41 and mc <= 60:
            point = point + (Referencepoint / (mc * 1.05))
        elif mc >= 60 and mc <= 65:
            point = point + (Referencepoint / (mc * 1.1))
        elif mc >= 65 and mc <= 70:
            point = point + (Referencepoint / (mc * 1.4))
        elif mc >= 70 and mc <= 100:
            point = point + (Referencepoint / (mc * 2.5))
        elif mc >= 100 and mc <= 150:
            point = point + (Referencepoint / (mc * 3.5))        
        else:
            point = point + (Referencepoint / (mc * (mc / 9)))
        if int(Timing) < int(HardestC): #Если тайминг сложнее старого, то он записывается
            HardestC = Timing
        
        if int(Timing) > int(FreeC): #Если тайминг легче старого, то он записывается
            FreeC = Timing
        
        Сounter = Сounter + 1 #сетчик таймингов
        Mior = Mior + int(Timing)
    result = point / Compression
    Mior = Mior / Сounter #Сумма таймингов на сумму кликов
    if seting != "2":
        print("\nVersion ALTA v5.2 by Prosto_Maksim")
        print("Level Timings:" + str(Timings) + "\nTotal timings:" + str(Сounter))
        print("FPS measurements:" + str(fps) + "\n")
        print("The hardest timing:" + str(HardestC)+"frame")
        print("simple timing:" + str(Mior)+"frame")
        print("The easiest timing:" + str(FreeC)+"frame\n")
    if seting == "1": #Вывод баланса
        balanceKZ(fps,Timings,"1")
    if seting != "2":
        print("pp:" + str(round(result, 1)) + "\n")
    return str(round(result, 1))

clear("0")
print("loading...   3/26")

def debuglvlcal(): #создано чисто для проверки(не для обычного юзера)
    data = ''
    frame = 1    
    while 1 == 1:
        data = data + lvlcal("240",frame, "2") + "," 
        if frame == 40:
            return data
        frame = frame + 1

clear("0")
print("loading...   4/26")

def settingfiles(mode, typE, Number): #Отвечает за сохранения настроек в файл. ГОВНО КОД потом перепишу!
    
    def reset(fist): #сброс файла
        if fist != "1": #ругатся если это был не первый запуск)
            print("Error reading settings file")
            print("It has been reset")
            print("The error was:" + str(typE))
            input()
        Filesetting = open('setting.alta', 'w') #Создает стоковый файл
        Filesetting.write("FPS:240 \n")
        Filesetting.write("Clear:0 \n")
        Filesetting.write("lvlbanace:0")
        Filesetting.close()
    
    Ok = 0
    
    folder = os.listdir() #ищет файл
    for files in folder:
        match files:
            case "setting.alta": #если нашел
                Ok = 1 #          все значить супер
    if Ok != 1: # если его нет, то сброс
        reset("1")
    
    match mode: #Какой режим - чтение или запись.
        
        case "read":            
            Filesetting = open('setting.alta', 'r')
            
            match typE: #Какую настройку считать
                
                case "fps":
                    read = re.findall(r'\d+', Filesetting.readline().rstrip(' ').rstrip('\n').rstrip(':'))
                    Filesetting.close()
                    if not read or read[-1] == "0": #если битый файл
                            reset("0")
                            return 240
                    Filesetting.close()
                    return read[-1]
                
                case "clear":
                    Filesetting.readline()
                    read = re.findall(r'\d+', Filesetting.readline().rstrip(' ').rstrip('\n').rstrip(':'))
                    Filesetting.close()
                    if not read: #если битый файл
                            reset("0")
                            return 0
                    Filesetting.close()
                    return read[-1]
                
                case "lvlbanace":
                    Filesetting.readline()
                    Filesetting.readline()
                    read = re.findall(r'\d+', Filesetting.readline().rstrip(' ').rstrip('\n').rstrip(':'))
                    Filesetting.close()
                    if not read: #если битый файл
                            reset("0")
                            return 0
                    Filesetting.close()
                    return read[-1]

        case "white": #режим записи
            Filesetting = open('setting.alta', 'r') #сохраняет настройки
            oldfps = Filesetting.readline().rstrip('\n')
            oldclean = Filesetting.readline().rstrip('\n')
            oldbanace = Filesetting.readline().rstrip('\n')
            Filesetting.close()
            
            match typE: #Какую настройку изменить
                
                case "fps": #создает новые настройки с новым фпс
                  Filesetting = open('setting.alta', 'w')  
                  Filesetting.write("FPS:" + str(Number) + "\n")
                  Filesetting.write(oldclean + "\n")
                  Filesetting.write(str(oldbanace) + "\n")
                  Filesetting.close()
                
                case "clear": #создает новые настройки с другим режимом чистки
                  Filesetting = open('setting.alta', 'w')  
                  Filesetting.write(str(oldfps) + "\n")
                  Filesetting.write("Clear:" + str(Number) + "\n")
                  Filesetting.write(str(oldbanace) + "\n")
                  Filesetting.close()                    

                case "lvlbanace": #создает новые настройки с другим режимом чистки
                  Filesetting = open('setting.alta', 'w')  
                  Filesetting.write(str(oldfps) + "\n")
                  Filesetting.write(oldclean + "\n")
                  Filesetting.write("lvlbanace:" + str(Number) + "\n")
                  Filesetting.close()  
clear("0")
print("loading.     5/26")

def conv(Timings): #Ну... просто ; среть и все)
    coun = len(str(Timings))
    coun = coun - 1
    for Timing in str(Timings):
        if coun != 0:
            print(Timing, end=";")
        else:
            print(Timing, end="\n")
            print("Готово!")
        coun = coun - 1

clear("0")
print("loading..    6/26")

def Victors(lvl):
    try:
        files = os.listdir("Base") #В скобаках какой папке база.
    except FileNotFoundError:
        print("DataBase not found")
        return 0
    all = []
    altapl = list(filter(lambda x: x.endswith('.altapl'), files)) #фильтр форматов(altapl - для игроков юзается)
    print("lvl:" + str(lvl))
    print("Have it>", end=" ")
    
    for file in altapl:
        Scan = 1
        data = open("Base/" + file, 'r')
        while Scan != "0":
            Scan = data.readline().rstrip('\n')
            Scan = Scan.split(":")[0]
            if Scan.lower() == lvl.lower():
                print(file.split(".altapl")[0] + ",", end=" ") #Вывод всех у кого есть лвл в пройденных
                all.append(file.split(".altapl")[0])
    print("\n")
    return all

clear("0")
print("Загрузка...   7/26")

standard = settingfiles("read","fps",1) #фпс по умолчанию
autoclear = settingfiles("read", "clear", 1) #какой режим чистки
KZbalance = settingfiles("read", "lvlbanace", 1)
TPS = int(standard) #Переносится стандартный фпс в переменную где с ним будут работать.

clear("0")
print("loading.     8/26")

def addlvl():

    try:
        print("lvl name") #Это почти как заглушка, потом будет что-то нормальное)
        com1 = input(">")
        print("Author(s) of lvl")
        com2 = input(">")
        print("verifier of lvl(if no, that - ?)")
        com3 = input(">")
        print("timings of lvl")
        com4 = input(">")
        print("FPS")
        com5 = input(">")
        print("idlvl:")
        com6 = input(">")
        pp = lvlcal(com5,com4,"2")
        if pp == 0:
            return 0
        fan = balanceKZ(int(com5),com4,"2")
    except KeyboardInterrupt:
        sys.exit()
    
    scan = 0
    try:
        data = open("Base/lvldatabase.altalvl", 'r')
    except FileNotFoundError:
        print("DataBase not found")
        return 0
    while scan == 0:
        lvlscan = data.readline().rstrip('\n')
        if lvlscan.lower() == com1.lower():
            print("It's already in the dataBase")
            return 0
        if lvlscan == "":
            scan = 1
    data.close()
    try:
        data = open("Base/lvldatabase.altalvl", 'a')
    except FileNotFoundError:
        return 0
    data.write("" + str(com1.lower()))
    data.write("\nAuthor(S):" + str(com2.lower()))
    data.write("\nVerification:" + str(com3.lower()))
    data.write("\nTimings:" + str(com4.lower()))
    data.write("\nFPS:" + str(com5.lower()))
    data.write("\nbalance:" + str(fan.lower()))
    data.write("\nPP:" + str(pp.lower()))
    data.write("\nidlvl:" + str(com6.lower()))
    data.write("\nend\n")
    data.close()

clear("0")
print("loading..    9/26")

def infolvl(lvl,setmode):
    good = 0
    try:
        data = open("Base/lvldatabase.altalvl", 'r')
    except FileNotFoundError:
        print("DataBase not found")
        return 0
    scan = 0
    while scan == 0:
        lvlscan = data.readline().rstrip('\n')
        if lvlscan.lower() == lvl.lower():
            info = 6
            while info != 0:
                info = info - 1
                lvlinfo = data.readline().rstrip('\n').lower()
                if setmode == "1":
                    print(lvlinfo)
                if info == 0:
                    return lvlinfo.split(":")[-1]
                scan = 1
                good = 1
        if lvlscan == "":
            scan = 1
    
    if good == 0:
        if setmode == "1":
            print("lvl not found in the database")
        return 0
    data.close()

clear("0")
print("loading...   10/26")

def addvict(Player,lvld): #Дает добавить лвл игроку
    try:
        pp = float(infolvl(lvld, "0"))
    except ValueError:
        print("He led exactly?")
        return 0
    if pp == 0:
        return 0
    pp = round(pp)
    Player = Player + ".altapl"
    
    try:
        data = open("Base/" + Player, 'r')
    except FileNotFoundError:
        print("there is no such player in the database or the database itself")
        return 0
    name = data.readline()
    lvl = data.readlines()
    for scan in lvl:
        if scan.split(":")[0] == lvld:
            print("He's already beaten it")
            return 0
    hardest = 0
    Comlit = 1
    
    while Comlit == 1:
        ll = lvl[hardest].split(":")[-1].rstrip('\n')
        hardest = hardest + 1
        if pp > int(ll):
            New = (hardest - 1)
            Comlit = 0
    data.close()
    data = open("Base/" + Player, 'w')
    data.write(name)
    hardest = 0
    
    print("New top", end=" ")
    print(New + 1, end=" ")
    print("at " + str(name))
    
    if New == 0:
        data.write(str(lvld) + ":" + str(pp) + "\n")
    
    while New != 0:
        New = New - 1
        data.write(lvl[hardest])
        hardest = hardest + 1
        if New == 0:
            data.write(str(lvld) + ":" + str(pp) + "\n")
    scan = "1"
    
    while scan != "0":
        scan = lvl[hardest]
        data.write(lvl[hardest])
        hardest = hardest + 1
    data.close()

clear("0")
print("loading.     11/26")

def createdb():
    files = os.listdir() #Проверка на наличие уже датабазы
    for scan in files:
        if scan == "Base": #если есть то -
            antidelete = random.randint(1000,9999)
            try:
                com = input("Are you sure to delete the old database???(write back>" + str(antidelete) + ") >" )
            except KeyboardInterrupt:
                sys.exit()
            if com == str(antidelete):
                shutil.rmtree("Base")
                print("Database is deleted!")
            else:
                print("wrong!")
                return 0
    os.mkdir("Base")
    new = open("Base/lvldatabase.altalvl", 'w')
    new.close()
    print("Database created!")

clear("0")
print("loading..    12/26")

def addpla(pla):
    files = os.listdir("Base/")
    for scan in files: #не дает повторно создать профиль.
        if pla == scan.split(".")[0]:
            print("The player is already in the database")
            return 0
    
    new = open("Base/"+str(pla)+".altapl", 'w') #если все-таки его нет, то это-
    new.write(pla)
    new.write("\n0")
    new.close()
    print("Player added")

clear("0")
print("loading...   13/26")

def loaddb():
    files = os.listdir() #Проверка на наличие уже датабазы
    for scan in files:
        if scan == "Base": #если есть то -
            antidelete = random.randint(1000,9999)
            try:
                com = input("Are you sure to delete the old database???(write back>" + str(antidelete) + ") >" )
            except KeyboardInterrupt:
                sys.exit()
            if com == str(antidelete):
                shutil.rmtree("Base")
                print("database is deleted!")
            else:
                print("wrong!")
                return 0
    try:
        db = input("Drag the database here>").replace('"', '')
    except KeyboardInterrupt:
        sys.exit()
    try:
        zip = zipfile.ZipFile(db, 'r')
    except FileNotFoundError:
        print("Not found")
        return 0
    zip.extractall('')
    zip.close()
    print("Database loaded!")

clear("0")
print("loading...   14/26")

def savedb():
    try:
        name = input("Name>")
        folder = input("Where to create?(path to any folder)>").replace('"', '')
    except KeyboardInterrupt:
        sys.exit()
    zip = zipfile.ZipFile(name +".zip", "w") #Создает архив
    try:
        zip.write("Base") #Создает папку в нем
    except FileNotFoundError:
        print("Database not found")
        return 0
    files = os.listdir("Base/") #Смотрит что у вас в базе
    
    for scan in files: #Смотрит что у вас в базе
        zip.write("Base/" + scan) #что нашел в ахрив
    
    zip.close() #закрывает ахрив
    shutil.copyfile(name + ".zip", folder + "/"+ name + ".zip") #копирует куда нужно
    os.remove(name + ".zip") #Удалает уже ненужный ахрив
    print("Database saved!")

clear("0")
print("loading.     15/26")

def infopla(pla):
    if pla == "0":
        try:
            files = os.listdir("Base/") #ищет в базе игроков
        except FileNotFoundError:
            print("Database not found")
            return 0
        print("All players in the database")
        files = filter(lambda x: x.endswith('.altapl'), files)
        
        for plaer in files: #Кусок от placal
            hardest = 1 #по название доложно понятно быть)
            folder = "base/" + plaer.replace('"', '')
            file = open(folder, 'r')
            pp = 0
            Scan = 1
            print("\nPlayer:" + file.readline().rstrip('\n')) #Показывает какой игрок
    
            while Scan == 1:
                pp1 = re.findall(r'\d+', file.readline().rstrip(' ').rstrip('\n').rstrip(':'))
        
                lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
        
                if lvl != 0:
                    pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
                    hardest = hardest + 1
        
                if lvl == 0:
                    Scan = 0
            print("PP:" + str(round(pp)))
    else:
        pla = pla + '.altapl'
        
        Placal("Base/" + pla, "1")
def plalvlcomm(requirements): #Для безопастности вынес это как функцию
            if requirements == "-l": #если лвл
                alllvl = scanallvl() #Получает все лвла
                print("Top all lvls>")
                pplvl = []
                for lvl in alllvl:
                    pplvl.append(infolvl(lvl,"0")) #Получает пп
                top(alllvl,pplvl) #Делает топ
            
            if requirements == "-ver": #если лвл
                alllvl = scanallvl() #Получает все лвла
                safelllvl = scanallvl()
                print("Top verified lvls>")
                pplvl = []
                for lvl in safelllvl:
                    if scanerpla(lvl, '2') != "?":
                        pplvl.append(infolvl(lvl,"0")) #Получает пп
                    else:
                        alllvl.remove(lvl)
                try:
                    top(alllvl,pplvl) #Делает топ
                except IndexError:
                    print("But they are not there :/")
            if requirements == "-p":
                Ramdonmane = os.listdir("Base/") #ищет в базе игроков
                Ramdonmane = filter(lambda x: x.endswith('.altapl'), Ramdonmane)
                print("Top players>")
                pplvl = []
                alllvl = []
                for plaer in Ramdonmane:
                    wfr = plaer.split(".altapl")
                    alllvl.append(wfr[0])
                    pplvl.append(round(tophelper(plaer)[0])) #Получает пп
                top(alllvl,pplvl)#Делает топ

clear("0")
print("loading..     16/26")

def tophelper(plaer):
        
        hardest = 1 #по название доложно понятно быть)
        folder = "base/" + plaer.replace('"', '')
        file = open(folder, 'r')
        pp = 0
        Scan = 1
        plarr = []
        pparr = []
        plarr.append(file.readline().rstrip('\n')) #Показывает какой игрок
    
        while Scan == 1:
            pp1 = re.findall(r'\d+', file.readline().rstrip(' ').rstrip('\n').rstrip(':'))
    
            lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
    
            if lvl != 0:
                pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
                hardest = hardest + 1
    
            if lvl == 0:
                Scan = 0
                pparr.append(pp)
        return pparr
clear("0")
print("loading...    17/26")

def balanceKZ(fps,sequence,lvlcalmode): #Не мое, так-что писать ничего не буду)
    score = 0
    points = 0
    list = []
    for i in sequence.split(";"):
        list.append(int(i))
    for k in list:
        if k == statistics.mode(list):
            score=score+1
        elif k < statistics.mode(list):
            try: #Баг фикс от меня '.'
                score=score+1-(((2*math.pi)**(statistics.mode(list)/int(k)))/fps)
            except OverflowError: #.
                score = 0 #.
                break #.
        elif k > statistics.mode(list):
            try: #.
                score=score+1-(((2*math.pi)**(int(k)/statistics.mode(list)))/fps)
            except OverflowError: #.
                score = 0 #.
                break #.
    points = score/len(list)*10
    if points < 0:
        points=0
    if lvlcalmode != "2":
        if lvlcalmode != "1":
            print('Ср timing:',str(round(statistics.mean(list),2)),'frame')
        print('Balance:',str(round(points,2))+'/10')
    return str(round(points,2))+'/10'

clear("0")
print("loading.      18/26")

def scanpplvl(lvl):
    pp = lvlcal(scanerpla(lvl,"4"),scanerpla(lvl,"3"),"2")
    lvlcha(lvl,"5", pp)
    lvlcha(lvl,"4", str(balanceKZ(int(scanerpla(lvl,"4")),str(scanerpla(lvl,"3")),"2")))

    allvict = Victors(lvl)
    for plar in allvict:
        deleteplalvl(plar,lvl)
        addvict(plar,lvl)

clear("0")
print("loading..     19/26")

def deleteplalvl(pla, lvl): #Дает удалить пройденный лвл у игрока
    pla = pla + ".altapl"
    
    try:
        data = open("Base/" + pla, 'r')
    except FileNotFoundError:
        print("there is no such player in the database or the database itself")
        return 0
    
    name = data.readline()
    lvlset = data.readlines()
    coutler = 0
    ok = 1
    antiass = 0
    
    while  ok == 1:
        for scan in lvlset:
            if scan.split(":")[0] == lvl:
                ok = coutler * 10
                antiass = 1
            coutler = coutler + 1
            if scan == "0" and antiass == 0:
                print("He doesn't have this lvl")
                return 0
    
    ok = ok / 10
    data.close()
    data = open("Base/" + pla, 'w')
    data.write(name)
    delet = 0
    
    for delete in lvlset:
        if delet != ok:
            data.write(delete)
        delet = delet + 1

clear("0")
print("loading...    20/26")

def lvlcha(lvl,type,nyper): #дает менять данные в базе о лвле
    
    types = ["Author(S):","Verification:","Timings:","FPS:","balance:","PP:","idlvl:"]
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    data.close()
    data = open("Base/lvldatabase.altalvl", 'w')
    ok = 0
    cout = type
    
    for dated in lvls:
        if ok == 1:
            cout = int(cout) - 1
        if cout != 100:
            if dated.split("\n")[0] != lvl and cout != 0:
                data.write(dated)
            else: #находит лвл и..
                data.write(dated)
                ok = 1
        else:
            cout = 101
        if cout == 0:
            data.write(str(types[int(type)]) + str(nyper) + "\n") #..и записывет новые данные
            ok = 0
            cout = 100
    data.close()

clear("0")
print("loading.      21/26")

def scanerpla(lvl,type):
    
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    data.close()
    cout = 0

    while lvls != "":
        try:
            if lvls[cout].split("\n")[0] == lvl:
                dl = lvls[cout + int(type)].split(":")[-1]
                return dl.rstrip('\n')
        except IndexError:
            return 0
        cout = cout + 1

clear("0")
print("loading..     22/26")

def top(data,pp): #Делает топ
    datapp = ([])
    cont = 0
    for d in data:
        pp1 = float(pp[cont])
        datapp.append((d,pp1))
        cont = cont + 1
    datapp = sorted(datapp, key=lambda datapp: datapp[-1], reverse=True)
    cont = 1
    for printtop in datapp:
        if printtop[1] != 0:
            print("Топ-" + str(cont))
            print(" " + str(printtop[0]))
            print(" pp:" + str(printtop[1]) + '\n')
        cont = cont + 1

clear("0")
print("loading...    23/26")

def scanallvl(): #Ищет все лвла
    
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    lvls.append("")
    data.close()
    scan = "0"
    cout = 0
    alllvl = []
    alllvl.append(lvls[0].rstrip("\n"))
    while scan != "":
        if (cout % 9) == 0: #если что-то хочу добавить в дб!!!
            alllvl.append(scan.rstrip("\n"))
        cout = cout + 1
        scan = lvls[cout]
    return alllvl

clear("0")
print("loading...    24/26")

def freme(fps,Timings): #считает не точно но пойдет)
    Сounter = 0
    Counter2fp = 0
    Counter3fp = 0
    Fremere = [0,0,0]

    Timings = Timings.split('-')
    if len(Timings) == 1:
        Timings = str(Timings[0])

    elif Timings[1] == "l":  # если -l
        
        Timings = str(Timings[0]) #чистить название лвл от -l 
        if len(Timings) == 0:
            print("You entered the level correctly?")
            return 0
        Lvl = Timings.rstrip(Timings[-1])
        
        oldTimings = Timings
        Timings = scanerpla(Lvl,"3") #Ищет тайминги в датабазе
        if Timings == 0:
            print("lvl - " + oldTimings + "<Not found>")
            return 0    
    elif Timings:
        print("You've entered exactly what you need?")
        return 0
    for T in Timings.split(";"):
        Сounter = Сounter + 1
        T = int(T)
        
        if T == 1: #первый фп(например 240фп)
            Fremere[0] = Fremere[0] + 1
        
        elif T == 2 or T == 3: #Второй фп(например 120фп)
            if T == 2:
                Fremere[1] = Fremere[1] + 1
            elif T == 3:
                if Counter2fp <= 1:
                    Fremere[1] = Fremere[1] + 1
                Counter2fp = Counter2fp + 1 #попытка эмулировать разные кадры))
                if Counter2fp >= 13:
                    Counter2fp = 0
        
        elif T >= 4 and T <= 5: #Третий фп(например 60фп)
            if T == 4:
                Fremere[2] = Fremere[2] + 1
            elif T == 5:
                if Counter3fp <= 2:
                    Fremere[2] = Fremere[2] + 1
                Counter3fp = Counter3fp + 1 #попытка эмулировать разные кадры))
                if Counter3fp >= 4:
                    Counter3fp = 0                
    print("\nVersiom ALTA v5.2 by Prosto_Maksim")
    print("Level timings:" + str(Timings) + "\nTotal timings:" + str(Сounter))
    print("FPS measurements:" + str(fps) + "\n")
    print(str(fps) +" fps frames:"+ str(Fremere[0]))
    print(str(int(fps)/2) +" fps frames:"+ str(Fremere[1])+" +-")
    print(str(int(fps)/4) +" fps frames:"+ str(Fremere[2])+" +-")
clear("0")
print("Загрузка...    24/26")
def verdbtest(): #Сигналка на случай неправильной дб
    types = ["Author(S):","Verification:","Timings:","FPS:","balance:","PP:","idlvl:","end"]
    try:
        data = open("Base/lvldatabase.altalvl", 'r')
    except FileNotFoundError:
        return 0
    data.readline()
    count = 0
    while 1 == 1:
        datas = ""
        ttpyes = ""
        datas = data.readline()
        test = ''.join(datas.split(":")[0])
        test = test.split("\n")
        ttpyes = str("".join(types[count].split(":")[0].split("\n")))
        if test[0] != ttpyes:
            print("Attention, the version of your db is NOT supported!!!!!")
            print("Any actions with it will most likely destroy it!!!!")
            print("I recommend that if you want to work with it, write a command 'convdb'")
            data.close()
            input("enter to continue>")
            return 1
        if test[0] == ttpyes == "end":
            data.close()
            return 2
        count = count + 1
verdbtest()
clear("0")
print("loading...    25/26")

def convdb():
    data = open("Base/lvldatabase.altalvl", 'r')
    db = data.read()
    dblist = db.split("\n")
    endreal = 0
    countw = 0
    count = 0 
    data.close()
    while countw == 0:
        if dblist[count] == "end":
            countw = count
        count = count + 1
    if countw >= 9:
        print("database is newer than alta, update alta!!!!!")
        return 9
    if countw == 8:
        print("database already current version!")
        return 8
    if countw == 7:
        print("database update")
        data = open("Base/lvldatabase.altalvl", 'w')
        for dd in dblist:
            if dd == "end":
                data.write("idlvl:?\n")
            if dd != "":
                data.write(dd + "\n")
        print("Successfully!")
        data.close()
        return 7
clear("0")
print("loading...    26/26")

clear("0")
print("version ALTA v5.2 by Prosto_Maksim")
print("for help write help")

while 1 == 1:
    
    try:
        com = input("/") #ждет команд
        if autoclear == "1":
            clear("0")
    except KeyboardInterrupt:
        sys.exit()
    
    com = com.lower() #убирает высокий регистр
    main = com.split(' ')
    auto = len(com) #сетчик буквЬ)
    requirementscalving = com.split(' ') #делает массив по пробелам
    Length = len(requirementscalving) - 1 #Смотрить сколько в массиве элементов.
    
    if Length != 0: #Смотрить если их не один, то
        requirements = str(requirementscalving[Length])
        Length = Length - 1
    else:
        requirements = str(requirementscalving[-1])
    while Length != 0: #Смотрить если их больше двух, то
        requirements = str(requirementscalving[Length] + " " + str(requirements))
        Length = Length - 1
    match main[0]:
        
        case "help":
            match requirements:
                case "help":
                    print(" To view all commands, enter help 'number' \n1 - Basic commands \n2 - commands for database \n3 - Extra")
                    print(" For help about a specific command, enter help 'desired command'")
                case "1":
                    print(" Basic commands:")
                    print("  fps - changes fps calculation pp")
                    print("  fps.set - fps which will be at startup")
                    print("  Placal - measuring a player's total pp from a file")
                    print("  lvlcal - pp lvl measurement")
                    print("  balcal - lvl balance measurement(by SpaceKZ)")
                case "2":
                    print(" For Database:")
                    print("  add.pla - add a player to the database")
                    print("  info.pla - List of players (if you write a nickname, it will work like placal)")
                    print("  victors - Searches for all victors of the desired lvl")
                    print("  add.vict - add completed lvl to player")
                    print("  del.vict - Delete a player's completed lvl")
                    print("  add.lvl - add lvl to the database")
                    print("  info.lvl - search and info about lvl")
                    print("  chatim - change timings for lvl (automatically recalculate for players)")
                    print("  chaver - change verifier (add/remove) for lvl")
                    print("  rebal - recalculate the ENTIRE DATABASE (if the software system has been updated)")
                    print("  top (-p = players) (-l = all lvls) (-ver top verified lvls)")
                    print("  load.db - Load database")
                    print("  save.db - Save the database")
                    print("  create.db - create a new database (Delete if there was one)")
                    print("  delete.db - Just delete the installed database")
                    print("  chaid - allows you to change the id of the lvl")
                    print("  convdb - converts db to current version.")
                    print("!Attention, Victor and the verifier are not communicating! if someone verified lvl, add separately as verifier and as victor!")
                case "3":
                    print(" Extra:")
                    print("  conv - converter from the old 12354 format to the new format 1;2;3;5;4 timings")
                    print("  clear - clear command line")
                    print("  clear.auto - leaves only the last command on the command line")
                    print("  lvlcal.bal - integrates into lvlcal and balcal measurements")
                    print("  exit - exit the program (you can use Ctrl + C )")
                    print("  dev - list of everyone who took part and so on")
                    print("  frep - approximate measurement of frame perfects")
                case "fps":
                    print("FPS command - to change the fps of pp calculation")
                    print("  Even if you skip FPS in chatim, the FPS you specified in fps will be")
                    print("  If you write fps '0' then the fps will be reset by fps.set")
                case "fps.set":
                    print("Command fps.set - stock fps that will be selected at startup")
                    print("  If you write FPS '0' it will be saved at 240")
                case "placal":
                    print("command placal - calculates the player’s total pp from a file")
                    print("  To work, you need to transfer the file to the console and press ENTER")
                    print("  The file must be in the correct format -< ")
                    print("  Player Name")
                    print("  LVL (his hardest): pp (how much lvlcal gave)")
                    print("  LVL (his prehardest): pp (how much lvlcal gave)")
                    print("  and so on")
                    print("  0 - at the end  >")
                    print("  % this is how much they gave from the pp")
                    print("  The cube challenge 1:500pp 85% == 500pp*0.85%=425pp (425 how much they gave him)")
                case "lvlcal":
                  print("command lvlcal for measuring lvl difficulty by pp")
                  print("   To measure you need to have a GD with FrameStep and an FPS bypass (physics bypass in 2.2)")
                  print("   We set the fps (in gd and in alta (command fps)) on which you will measure (the more fps the more accurate (but the measurement will take longer))")
                  print("   Next, we begin to measure how many frames each timing has for the flight and record it through ;")
                  print("   After the measurements you will have approximately 4;7;3;6;2;10;1;2")
                  print("   Then press Enter and get the result")
                case "balcal":
                    print("Balcal team for measuring lvl balance")
                    print("  Measured in the same way as lvlcal")
                    print("-  -  -  -  -  -")
                    print(" To measure you need to have a GD with FrameStep and an FPS bypass (physics bypass in 2.2)")
                    print(" We set the fps (in gd and in alta (command fps)) on which you will measure")
                    print(" Next, we begin to measure how many frames each timing has for the flight and record it through ;")
                    print(" After the measurements you will have approximately 4;7;3;6;2;10;1;2")
                    print(" Then press Enter and get the result")
                    print("-  -  -  -  -  -")
                case "frep":
                    print("Command frep to measure the number of frames in a level")
                    print("  Measured in the same way as lvlcal")
                    print("-  -  -  -  -  -")
                    print(" To measure you need to have a GD with FrameStep and an FPS bypass (physics bypass in 2.2)")
                    print(" We set the fps (in gd and in alta (command fps)) on which you will measure")
                    print(" Next, we begin to measure how many frames each timing has for the flight and record it through ;")
                    print("After the measurements you will have approximately 4;7;3;6;2;10;1;2")
                    print(" Then press Enter and get the result")
                    print("-  -  -  -  -  -")
                    print("And if you already have lvl in the database then")
                    print("/frep (level) -l")
                    print("-l = lvl, that is, search the database by name")                    
                case "add.pla":
                    print("command add.pla adds a player to the database.\nAfter this you can work with him")
                case "info.pla":
                    print("Command info.pla, if input is empty, shows everyone in the data base")
                    print(" If you add a nickname, it will work like something like placal")
                case "victors":
                    print("command victors 'lvl' - shows all lvl victors in the database, without order")
                case "add.vict":
                    print("Command add.vict adds the level passed to the player")
                    print("  For this we write")
                    print("  1 - Victor's nickname in the database")
                    print("  2 - Beaten lvl (it must be in the database)")
                case "del.vict":
                    print("Command del.vict removes the player's completed level")
                    print("  For this we write")
                    print("  1 - Victor's nickname in the database")
                    print("  2 - Beaten lvl")
                case "add.lvl":
                    print("Command add.lvl - adds lvl to the database")
                    print(" For this we write")
                    print("  1 - lvl name")
                    print("  2 - Author(s) or host(s) lvl")
                    print("  3 - Nickname of lvl verifier")
                    print("  4 - Timings that were obtained after measuring lvl, that is, for example '2;3;6;3;7;4;3;7")
                    print("  5 - FPS at which you measured")
                case "info.lvl":
                    print("Command info.lvl 'original lvl' - shows basic lvl data")
                case "chatim":
                    print("Command chatim - allows you to change the timings of the lvl in the database")
                    print("And he automatically changes all Victors’ pp for him")
                    print(" For this we write")
                    print("  1 - lvl name")
                    print("  2 - fps (if you enter 0, the one set to fps or fps.set)")
                    print("  3 - timings")
                case "chaver":
                    print("Command chaver - allows you to change the verifier at lvl in the database")
                    print(" For this we write")
                    print("  1 - lvl name")
                    print("  2 - Verifier (if you remove - '?')")
                case "rebal":
                    print("Command rebal - serve for quick recalculation when changing the pp system")
                    print("  Recalculates all lvl and lists pp to players")
                case "top":
                    print("Command top -l(all lvls), -ver (all verified lvls), -p (players) - Sorts players or lvls by pp and makes the top")
                case "load.db":
                    print("Command load.db - allows you to load a database from a file(zip)")
                    print("  To download, he will delete the old database (for protection, he will ask for a captcha)")
                    print("  After that, he will ask you to throw a database file into the program window(zip)")
                    print("  And he load it up")
                case "save.db":
                    print("Command save.db - allows you to save the database so that you can later load it via load.db")
                    print(" To save you need")
                    print("  1 - Name the database")
                    print("  2 - Name the database")
                    print("  3 - Path where to save it (you can drop the desired folder into the window)")
                case "create.db":
                    print("Command create.db - creates a database (if it doesn’t exist) or clears it (if there was one))")
                    print("If she was, then she would ask for a captcha")
                case "delete.db":
                    print("Command delete.db - delete the database (ask for a captcha)")
                case "conv":
                    print("conv - If you still have timings from older versions of ALTA, where the timings were up to a maximum of 9 frames")
                case "clear":
                    print("Clear console")
                case "clear.auto":
                    print("Clean after each command (this setting remains even after restarting ALTA)")
                case "lvlcal.bal":
                    print("embeds lvlcal and balcal into measurements (this setting is retained even after restarting ALTA)")
                case "exit":
                    print("exit the program (you can use Ctrl + C)")
                case "dev":
                    print("About the developers of ALTA and assistants")
                case "chaid":
                    print("Lets you change your lvl id")
                    print("for this we write")
                    print("1 - lvl name")
                    print("2 - id(if removed - '?')")
                case "convdb":
                    print("convdb - converts database to current version.")
                    print(" To convert, just write it stupidly and that’s it!")
                    print(" IF DATABASE is NEWER than ALTA then it will not be able to convert!")
        case "clear":
            clear("1")
        
        case "placal":
            Placal("0","0")
        
        case "fps": #Выбор кастом фпс
            try:
                if auto == 3: #если только команда
                    TPS = float(input(">>"))
                else: #если с ней что-то еще написано
                    TPS = int(requirements)   #Выбирает последную из всего массива и считает как за выбранный фпс
            except ValueError: #защита от идиота
                print("You definitely entered FPS?")
            except KeyboardInterrupt:
                sys.exit()
            if TPS == 0: #cброс
                print("reset!")
                TPS = int(standard)
            print("Fps set to " + str(TPS))
        
        case "fps.set":
            try:
                if auto == 7: #если только команда
                    standard = round(float(input(">>")))
                    settingfiles("white","fps", standard)
                else: #если с ней что-то еще написано
                    standard = int(requirements)
                    settingfiles("white","fps", int(requirements))  #Выбирает последную из всего массива и считает как за выбранный фпс
            except ValueError: #защита от идиота
                print("You definitely entered FPS?")
                standard = settingfiles("read","fps",1)
            except KeyboardInterrupt:
                sys.exit()
            if standard == 0: #cброс
                print("reset!")
                settingfiles("white","fps","240")
                standard = 240
            print("Fps by default>" + str(round(int(standard), 1)))
        
        case "clear.auto": #Переключение режимов чистки
            if autoclear == "1":
                autoclear = "0"
                settingfiles("white","clear", "0")
                print("Auto clear - off") #Выкл
            else:
                autoclear = "1" 
                settingfiles("white","clear", "1")
                print("Auto clear - on") #Вкл
        
        case "lvlcal.bal": #Переключение режимов чистки
            if KZbalance == "1":
                KZbalance = "0"
                settingfiles("white","lvlbanace", "0")
                print("Balance display - off") #Выкл
            else:
                KZbalance = "1" 
                settingfiles("white","lvlbanace", "1")
                print("Balance display - on") #Вкл        
        
        case "lvlcal":
            if auto == 6:#если только команда
                lvlcal(TPS,"0",KZbalance)
            else: #если с ней что-то еще написано
                lvlcal(TPS,requirements,KZbalance) #Выбирает последную из всего массива и считает как за тайминги
        
        case "exit": #выход из проги
            sys.exit()

        case "conv":
            try:
                if auto == 4: #если только команда
                    com = input(">>")
                    conv(com)
                else: #если с ней что-то еще написано
                    conv(requirements)
            except ValueError: #защита от идиота
                print("You've entered exactly what you need?")
            except KeyboardInterrupt:
                sys.exit()
        
        case "victors":
            try:
                if auto == 7: #если только команда
                    com = input(">>")
                    Victors(com)
                else: #если с ней что-то еще написано
                    Victors(requirements)
            except ValueError: #защита от идиота
                print("You've entered exactly what you need?")
            except KeyboardInterrupt:
                sys.exit()
        
        case "info.lvl":
            try:
                if auto == 8: #если только команда
                    com = input(">>")
                    infolvl(com, "1")
                else: #если с ней что-то еще написано
                    infolvl(requirements, "1")
            except ValueError: #защита от идиота
                print("You've entered exactly what you need?")
            except KeyboardInterrupt:
                sys.exit()        
        
        case "add.lvl":
            addlvl()
        
        case "add.vict":
            try:
                plar = input("Which player?>")
                lvl = input("What lvl?>")
            except KeyboardInterrupt:
                sys.exit()
            addvict(plar.lower(),lvl.lower())
        
        case "delete.db":
            antidelete = random.randint(1000,9999)
            try:
                com = input("Are you sure?? (write back>" + str(antidelete) + ") >" )
            except KeyboardInterrupt:
                sys.exit()
            if com == str(antidelete):
                shutil.rmtree("Base")
                print("Database is deleted")
            else:
                print("Wrong!")
        
        case "create.db":
            createdb()
        
        case "add.pla":
            try:
                if auto == 7: #если только команда
                    com = input(">>")
                    addpla(com)
                else: #если с ней что-то еще написано
                    addpla(requirements)
            except ValueError: #защита от идиота
                print("You've entered exactly what you need?")
            except KeyboardInterrupt:
                sys.exit()
        
        case "info.pla":
            try:
                if auto == 8: #если только команда
                    infopla("0")
                else: #если с ней что-то еще написано                    
                    infopla(requirements)
            except ValueError: #защита от идиота
                print("You've entered exactly what you need?")
            except KeyboardInterrupt:
                sys.exit()
        
        case "load.db":
            loaddb()
        
        case "save.db":
            savedb()
        
        case "balcal":
            try:
                if auto == 6: #если только команда
                    com = input(">>")
                    balanceKZ(TPS,com,"0")
                else: #если с ней что-то еще написано
                    balanceKZ(TPS,requirements,"0")
            except ValueError: #защита от идиота
                print("You've entered exactly what you need?")
            except KeyboardInterrupt:
                sys.exit()
        case "frep":
            try:
                if auto == 4: #если только команда
                    com = input(">>")
                    freme(TPS,com)
                else: #если с ней что-то еще написано
                    freme(TPS,requirements)
            except ValueError: #защита от идиота
                print("You've entered exactly what you need?")
            except KeyboardInterrupt:
                sys.exit()        
        case "del.vict":
            com = input("Who has?>")
            com2 = input("What lvl?>")
            deleteplalvl(com.lower(),com2.lower())
        
        case "chatim":
            com = input("What lvl?>").lower()
            com3 = input("What fps?(0 if normal)")
            if com3 == "0" or com3 == "": #Если ничего то обычный фпс
                com3 = TPS
            com2 = input("What are the timings??>")
            try:
                lvlcha(com,"2",com2)
                lvlcha(com,"3",com3)
                scanpplvl(com)
            except FileNotFoundError:
                print("Database not found")
        
        case "chaver":
            com = input("What lvl?>").lower()
            com3 = input("Who verifier?(sign ? to remove)>")
            try:
                lvlcha(com, "1", com3)
            except FileNotFoundError:
             print("Database not found")   
        case "rebal":
            try:
                com = scanallvl()
            except FileNotFoundError:
                    print("Database not found")            
            
            for lvl in com:
                if lvl != "0":
                    try:
                        scanpplvl(lvl)
                    except FileNotFoundError:
                        print
        case "chaid":
            com = input("What lvl?>").lower()
            com3 = input("New id( '?' - if private)>")
            try:
                lvlcha(com, "6", com3)
            except FileNotFoundError:
             print("Database not found")   
        case "convdb":
            convdb()        
        case "top":
            try:
                plalvlcomm(requirements)
            except FileNotFoundError:
                print("Database not found")
        case "dev":
            print("Developer - Prosto_Maksim - https://youtube.com/@Prosto_Maksim\n")
            print("Thanks - SpaceKZ for (balcal) - https://www.youtube.com/@spaceKZ1\n")
            print("Licence - GNU GPL v3 - https://www.gnu.org/licenses/quick-guide-gplv3.ru.html")
        case "debug.1":
            print(debuglvlcal()[:-1])
        