# Напишите программу, которая запрашивает у пользователя строку и выводит ее длину, количество гласных и солганных символов. (Строки вводятся на русском)


# создаем переменную и присваиваем ей строку, введенную пользователем
string = input("Введите строку: ").lower()
# создаем переменную и присваиваем ей строку
vowels = "уеаояиюэы"
# выводим строку
print(f"Длина строки равна {len(string)}")
# создаем переменную и присваиваем ей значение равное количеству гласных в строке
vowels_count = sum(string.count(vowel) for vowel in vowels)
# создаем переменную и присваиваем ей количеству согласных в строке
consonants_count = len(string) - vowels_count
# выводим строку
print(f"Количество гласных в строке {vowels_count}")
# выводим строку
print(f"Количество согласных в строке {consonants_count}")

