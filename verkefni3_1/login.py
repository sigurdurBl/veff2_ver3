import sqlite3,sys
import time
def login():
    while True:
        username= input("Please enter your username:")
        password= input("Please enter your password")
        with sqlite3.connect("quiz.db") as db:
            cursor = db.cursor()
        find_uesr = ("SELECT * FROM user WHERE username = ? and password = ? ")
        cursor.execute(find_uesr,[(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("welcome" +i[2])
            #return ("exit")
            break
        else:
            print("username and password not recognised")
            again = input("do you want to try again (y/n)")
            if again.lower() == "n":
                print("Goodbye")
                time.sleep(1)
                #return ("exit")
                break
def newUser():
    found = 0
    while found == 0:
        username = input("please enter a username:")
        with sqlite3.connect("quiz.db") as db:
            cursor = db.cursor()
        findUser = ("SELECT * FROM user WHERE username = ?")
        cursor.execute(findUser,[username])

        if cursor.fetchall():
            print("username taken please try again")
        else:
            found = 1

    firstname = input("Enter your first name")
    surname = input("Enter your surname")
    password = input("please enter your password")
    password1 = input("please reenter your password")
    while password != password1:
        print("your passwords didn´t match please try again")
        password = input("please enter your password")
        password1 = input("please reenter your password")
    insertData = '''INSERT INTO user(username,firstname,surname,password)
    VALUES(?,?,?,?)'''

    cursor.execute(insertData,[(username),(firstname),(surname),(password)])
    db.commit()


def menu():
    while True:
        print("welcome to my system")
        menu = ('''
        1 - create new user
        2 - login to system
        3 - exit system\n''')
        userchoice = input(menu)
        if userchoice == "1":
            newUser()
        elif userchoice == "2":
            login()
        elif userchoice == "3":
            print("Goodbye")
            sys.exit()
        else:
            print("comand not recognised")
menu()