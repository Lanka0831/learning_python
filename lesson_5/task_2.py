# Задание 2
# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.


file = open('test.txt', 'r', encoding='utf-8')
text = file.readlines()
line = len(text)
print(f'Всего строк: {line}')
for line in text:
    print(f'{len(line.split())}')
file.close()