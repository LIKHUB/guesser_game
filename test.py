word_list = ['Sport', 'Aerobics', 'Cheer', 'Football', 'Basketball', 'Volleyball', 'Track']

def delete_repeat(list_of_symbols):#Удаление в списке из букв одинаковых символов
    list_of_symbols = [list_of_symbols[i] for i in range(0, len(list_of_symbols))]
    for i in range(0, len(list_of_symbols)):#Проверка если в слове были повторяющиеся буквы и их замена на пустые строки
        for j in range(0, i):
            if list_of_symbols[i] == list_of_symbols[j]:
                list_of_symbols[j] = ''

    list_of_symbols = ''.join(list_of_symbols).strip()#Окончательное преообразование списка в набор букв, которые встречаются в веденном слове без повторений
    list_of_symbols = [list_of_symbols[i] for i in range(len(list_of_symbols))]

    return list_of_symbols

def word_as_symbol_combination(s):#Функция преобразования строки в набор неповторяющихся символов из нее
    inpaslist = []

    for i in range(0, len(s)):#Создание списка, в котором каждый элемент - это один символ из введенного слова
        inpaslist.append(s[i])

    for i in range(0, len(inpaslist)):#Проверка если в слове были повторяющиеся буквы и их замена на пустые строки
        for j in range(0, i):
            if inpaslist[i] == inpaslist[j]:
                inpaslist[j] = ''

    inpaslist = ''.join(inpaslist).strip()#Окончательное преообразование списка в набор букв, которые встречаются в веденном слове без повторений
    inpaslist = [inpaslist[i] for i in range(len(inpaslist))]


    return inpaslist

def try_symbols(list_of_symbols, word):#Проверка символов из введенной попытки на присутствие в слове
   
    appropriate_symbols = []

    for i in range(0, len(word)):
        for j in range(0, len(list_of_symbols)):#Проверка каждого символа на присутствие в слове
            if word.lower()[i] == list_of_symbols[j].lower():
                appropriate_symbols.append(list_of_symbols[j])

    for i in range(0, len(appropriate_symbols)):#Проверка если в слове были повторяющиеся буквы и их замена на пустые строки
        for j in range(0, i):
            if appropriate_symbols[i] == appropriate_symbols[j]:
                appropriate_symbols[j] = ''

    appropriate_symbols = ''.join(appropriate_symbols).strip()
    appropriate_symbols = [appropriate_symbols[i] for i in range(len(appropriate_symbols))]

    return appropriate_symbols