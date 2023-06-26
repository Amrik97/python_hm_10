import subprocess  # импортируем библиотеку для запуска команд в командной строке
import chardet  # импортируем библиотеку для определения кодировки текста

urls = ['yandex.ru', 'youtube.com']  # список URL-адресов, которые нужно пропинговать

for url in urls:
    # запускаем команду ping для каждого URL-адреса и сохраняем результат в переменную ping
    ping = subprocess.Popen(['ping', '-c', '4', url], stdout=subprocess.PIPE)

    # читаем вывод команды ping из стандартного потока и сохраняем его в переменную out
    out, _ = ping.communicate()

    # определяем кодировку текста с помощью модуля chardet
    encoding = chardet.detect(out)['encoding']

    # преобразуем байтовый вывод команды ping в строку с помощью метода decode()
    out_str = out.decode(encoding)

    # выводим результаты пинга на экран
    print(out_str)