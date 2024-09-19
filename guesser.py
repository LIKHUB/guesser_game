import test
import random

word = random.choice(test.word_list)
word_guess = '_'*len(word)
ind_list = []
indices = []
tried_symbols_all = []
guessed = False
cnt = 0

while not guessed:
    guess = input()#Ввод слова или символа для угадывания
    if guess.isalpha():#Проверка на то, что введенная строка содержит только буквы
        if guess not in tried_symbols_all:#Проверка на повторение
            if len(guess) == 1:#Случай, если ввели одну букву
                tried_symbols_all += test.word_as_symbol_combination(guess)
                tried_symbols_all = test.delete_repeat(tried_symbols_all)

                if guess.lower() in word.lower():#Если введенная буква в слове, то нахождение ее индекса в загаданном слове
                    for i in range(len(word)):
                        if word[i].lower() == guess.lower():
                            indices.append(i)

                    for index in indices:#Подстановка загаданной буквы, если она в слове, в ворд гес на свой индекс
                        word_guess = list(word_guess)
                        word_guess[index] = guess
                        word_guess = ''.join(word_guess)
                    ind_list = indices
                    indices = []

                if word_guess.lower() == word.lower():
                    guessed = True
                    cnt+=1
                    print('Congrats, you won')
                    print(cnt, tried_symbols_all, ind_list, word_guess, word, guessed)
                    break
                
                cnt+=1

            elif len(guess) > 1:
                tried_symbols_all += test.word_as_symbol_combination(guess)
                tried_symbols_all = test.delete_repeat(tried_symbols_all)

                for i in range(len(tried_symbols_all)):#Перебор символов из введенного на проверку слова
                    if tried_symbols_all[i].lower() in word.lower():
                        if tried_symbols_all[i].lower() not in word_guess:#Исключение повторения символов, если пробовались 
                            for j in range(len(word)):#Цикл перебора букв исходного слова и сравнение с буквами введенного слова
                                if tried_symbols_all[i].lower() == word[j].lower():
                                    indices.append(j)
                                    for index in indices:#Подстановка в ворд гес
                                         word_guess = list(word_guess)
                                         word_guess[index] = tried_symbols_all[i]
                                         word_guess = ''.join(word_guess)
                                         ind_list = indices
                                         indices = []
                        else:
                            continue

                if word_guess.lower() == word.lower():
                    guessed = True
                    cnt+=1
                    print('Congrats, you won')
                    print(cnt, tried_symbols_all, ind_list, word_guess, word, guessed)
                    break
            
                cnt+=1
        else:
            print('You have tried that already')

    else:
        print('Enter charachters only')
    
    print(cnt, tried_symbols_all, ind_list, word_guess, word, guessed)
    if cnt == 6:
        print('You did not win')
        break