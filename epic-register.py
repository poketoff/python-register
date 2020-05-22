
name_File = input("Введите имя txt файла(с расширением .txt): ")
file = open(name_File, "w")

first_Name = input("Введи имя: ")
file.write(first_Name + "\n")

second_Name = input("Введи фамилию: ")
file.write(second_Name + "\n")

login_Name = input("Введи логин: ")
file.write(login_Name + "\n")

email_Name = input("Введи mail: ")
file.write(email_Name + "\n")

pass_Name = input("Введи пароль: ")
file.write(pass_Name + "\n")

file.write("\n1- имя\n2- фамилия\n3- логин\n4- мыло\n5- пароль")

file.close()

