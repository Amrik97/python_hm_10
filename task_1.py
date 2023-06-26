# определяем список слов
words = ['разработка', 'сокет', 'декоратор']

# инициализируем списки для хранения буквенных форм и кодовых точек
letter_formats = []
unicode_codepoints = []

# обходим каждое слово в списке
for word in words:
    # преобразуем слово в буквенный формат и добавляем в список
    letter_format = ' '.join([format(ord(letter), 'x') for letter in word])
    letter_formats.append(letter_format)

    # преобразуем слово в набор кодовых точек Unicode и добавляем в список
    unicode_codepoint = ''.join([f'\\u{ord(letter):04x}' for letter in word])
    unicode_codepoints.append(unicode_codepoint)

# выводим результаты
for i in range(len(words)):
    print(f'Слово "{words[i]}" в буквенном формате: {letter_formats[i]}')
    print(f'Слово "{words[i]}" в наборе кодовых точек Unicode: {unicode_codepoints[i]}')
    print(f'Тип переменной для буквенного формата: {type(letter_formats[i])}')
    print(f'Содержание переменной для буквенного формата: {letter_formats[i]}')
    print(f'Тип переменной для набора кодовых точек Unicode: {type(unicode_codepoints[i])}')
    print(f'Содержание переменной для набора кодовых точек Unicode: {unicode_codepoints[i]}')
    print(f'Содержание переменной для набора кодовых точек Unicode: {unicode_codepoints[i]}')