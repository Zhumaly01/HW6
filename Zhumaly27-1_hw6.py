import re

while True:
    answer = int(input(f'(1) names and surename\n(2) Enmails\n(3) Files\n(4) Colors\n(5) Exit\nвведите действие: '))

    if answer == 1:
        with open('MOCK_DATA', 'r', encoding='UTF-8') as file:
            text = file.read()
            names = re.findall(r"[A-Z][a-z-]+\s+[a-zA-Z][a-zA-Z- ']*", text)
            with open('names', 'w', encoding='UTF-8') as file:
                file.write(str(', ').join(names))
    elif answer == 2:
        with open('MOCK_DATA', 'r', encoding='UTF-8') as file:
            text = file.read()
            emails = re.findall(r'[a-z|\d]+@[a-z|\d-]+\.[a-z]{2,3}\.?[a-z]*', text)
            with open('emails', 'w', encoding='UTF-8') as file:
                file.write(str(', ').join(emails))
    elif answer == 3:
        with open('MOCK_DATA', 'r', encoding='UTF-8') as file:
            text = file.read()
            files = re.findall(r'[A-Z][a-zA-Z]*\.[a-z\d]{3,4}', text)
            with open('files', 'w', encoding='UTF-8') as file:
                file.write(str(', ').join(files))
    elif answer == 4:
        with open('MOCK_DATA', 'r', encoding='UTF-8') as file:
            text = file.read()
            colors = re.findall(r'#[\d|a-z]{6}', text)
            with open('colors', 'w', encoding='UTF-8') as file:
                file.write(str(', ').join(colors))
    elif answer == 5:
        break