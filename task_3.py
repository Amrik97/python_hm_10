words = ['attribute', 'класс', 'функция', 'type']

for word in words:
    try:
        # Пытаемся преобразовать слово в байтовый формат
        word_bytes = b'' + word
        print(word, "можно записать в байтовом формате")
    except:
        # Если выбрасывается исключение, значит слово нельзя записать в байтовом формате
        print(word, "нельзя записать в байтовом формате")