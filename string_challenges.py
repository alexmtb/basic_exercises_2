# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(f'Последняя буква в слове {word}: {word[-1]}')


# Вывести количество букв "а" в слове
word = 'Архангельск'
# code
print(
    f'Количество букв "а" в слове {word}: {word.lower().count("а")}'
)


# Вывести количество гласных букв в слове
word = 'Архангельск'
# code
vowels = 'аеёиоуыэюя'
vowels_count = 0
for letter in word.lower():
    vowels_count += vowels.count(letter)
print(f'Количество гласных букв в слове {word}: {vowels_count}')


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# code
print(f'Количество слов в предложении "{sentence}": {len(sentence.split())}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# code
print('Первые буквы слов в предложении:')
for word in sentence.split():
    print(f'{word[0]} - {word}')


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# code
av_len = sum([len(word) for word in sentence.split()]) / len(sentence.split())
print(f'Усреднённая длина слова в предложении "{sentence}" равна: {av_len:.1f}')