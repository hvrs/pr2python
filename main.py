
name = input("Название файла")
while(True):
    with open(name + ".txt", "a") as file:
        strk = input("Введите строку: ")
        if(len(strk) < 3 or strk.isalpha()==False):
            print("Введите только строку")
            continue
        else:
            file.write("\n" + strk)
            break

        