users = {"studentSF": "efg5fh3j", "user453": "qervh45k", "monster_skill": "hhjd7bj34", "hero_factory": "hk3867jm"}

login = input("Введите ваш логин: ")
password = input("Введите ваш пароль: ")

if login in users.keys() and password == users[login]:
    print("добро пожаловать!")
elif login in users.keys() and password != users[login]:
    print("Вы ввели неверный пароль")
else:
    print("Вам необходимо пройти регистрацию на сайте!")


