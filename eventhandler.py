import dbhandler
import hashlib

def authorizePerson(user, password):
    if dbhandler.isUserExists(user):
        data = dbhandler.getUserDataFromTable('users', user)

        h = hashlib.md5(password.encode('utf-8'))
        hashPass = h.hexdigest()

        if data[0][2] == hashPass:
            return True, ''
        else:
            return False, 'Пароли не совпадают!'
    else:
        return False, 'Такого пользователя не существует!'

def registratePerson(user, password, repPass):
    if dbhandler.isUserExists(user):
        return False, 'Такой пользователь уже существует!'

    if password != repPass:
        return False, 'Пароли не совпадают!'

    dbhandler.insertIntoTable('users', user, password)

    return True, 'Регистрация пройдена успешна!'

def getUsers():
    return dbhandler.getAllUsersFromTable('users')