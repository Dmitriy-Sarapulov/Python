from chardet import detect

with open('test_file.txt', 'rb') as f:
    s = f.read()
    print(s)
    print(detect(s))

with open('test_file.txt', encoding='utf-8') as file:
    print(file.read())