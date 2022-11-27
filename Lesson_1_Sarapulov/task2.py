words = ["class", "function", "method", b"class", b"function", b"method"]
counter = 0

for i in words:
    print(f"{i} = {type(i)}")
    if counter == 2:
        print("ниже расположены эти же слова в байтах")
    counter += 1