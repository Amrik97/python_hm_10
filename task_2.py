words = ['class', 'function', 'method']
byte_strings = [bytes(word, 'utf-8') for word in words] #переводит слова в байты
for byte_string in byte_strings:
    print(type(byte_string))      # выводит: <class 'bytes'>
    print(byte_string)            # выводит: b'class' (и аналогично для остальных слов)
    print(len(byte_string))       # выводит: 5 (длина байтовой строки)