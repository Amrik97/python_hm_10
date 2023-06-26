words = ['разработка', 'администрирование', 'protocol', 'standard']
encoded_words = []
decoded_words = []

for word in words:
    # Преобразуем строку в байты, используя кодировку utf-8
    encoded_word = word.encode('utf-8')
    encoded_words.append(encoded_word)

    # Обратное преобразование: из байтов в строку
    decoded_word = encoded_word.decode('utf-8')
    decoded_words.append(decoded_word)

print(encoded_words)
print(decoded_words)