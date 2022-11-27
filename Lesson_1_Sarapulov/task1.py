DEV_UNICODE = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
SOC_UNICODE = "\u0441\u043e\u043a\u0435\u0442"
DEC_UNICODE = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"
words = ["разработка", "сокет", "декоратор", DEV_UNICODE, SOC_UNICODE, DEC_UNICODE]
counter = 0
for i in words:
    print(f"{i} = {type(i)}")
    if counter == 2:
        print("ниже расположены эти же слова в кодировке UNICODE")
    counter += 1