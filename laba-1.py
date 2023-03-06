#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно),
#распознает, преобразует и выводит на экран числа по определенному правилу.
#Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь.
#Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
#Регулярные выражения использовать нельзя.

#Шеснадцатиричные числа, у которых 2 слева цифра равна В16 расположенные в порядке не убывания.
#Четные цифры выводить словами.

buffer_len = 1 #размер буфера чтения
work_buffer = "" #рабочий буфер
                    
def number_to_words(n): #все цифры в шестнадцатиричной СС и их пропись
    f = {0 : 'ноль', 1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять',
    6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять', 10 : 'A', 11 : 'B', 12 : 'C', 13 : 'D',
         14 : 'E', 15 : 'F'}
    return f.get(n)
 
a = []
with open("laba-1.txt") as file: #открываем файл
    buffer = file.read(buffer_len) #читаем первый блок
    if not buffer: #если файл пустой
        print("Файл пустой")
        exit()
    while buffer: #пока файл не пустой
        while buffer >= '0' and (buffer <= 'F' or buffer <= 'f'): #обрабатываем текущий блок
            if buffer >= '0' and (buffer <= 'F'or buffer <= 'f'):
                work_buffer += buffer
            buffer = file.read(buffer_len) #читаем очередной блок
        if len(work_buffer) >= 2:
            if work_buffer[1] == 'B' or work_buffer[1] == 'b': #ищем числа, в которых вторая слева цифра B
                a.append(work_buffer)
                a.sort() #сортируем список по неубыванию  
        work_buffer = ""
        buffer = file.read(buffer_len) #читаем очередной блок
    
    if len(a) == 0:
        print('В файле нет подходящих чисел')

       
    print('Список чисел, подходящих под условие: ', a)
    for i in a:
        print(i)
        for j in i:
            if int(j,16) % 2 == 0:
                evenNumber = number_to_words(int(j, 16)) #четные цифры выводим словами
                print(evenNumber + ' - четная цифра')
    
"""
a = []
with open("laba-1.txt") as file: #открываем файл
    buffer = file.read(buffer_len) #читаем первый блок
    if not buffer: #если файл пустой
        print("Файл laba-1.txt пустой")
        exit()
    while buffer: #пока файл не пустой
        while buffer >= '0' and buffer <= 'F': #обрабатываем текущий блок
            if buffer >= '0' and buffer <= 'F':
                work_buffer += buffer
            buffer = file.read(buffer_len) #читаем очередной блок
        if len(work_buffer) >= 2:
            if work_buffer[1] == 'B': #ищем числа, в которых вторая слева цифра B
                a.append(work_buffer)
                a.sort() #сортируем список по неубыванию  
        work_buffer = ""
        buffer = file.read(buffer_len) #читаем очередной блок
        
    print(a)
    
if len(a) == 0:
    print('В файле нет подходящих чисел')
else:   
    for i in a:
        print(i)
        for j in i:
            if int(j,16) % 2 == 0:
                evenNumber = number_to_words(int(j, 16)) #четные цифры выводим словами
                print(evenNumber)
"""
















        