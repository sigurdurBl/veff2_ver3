import sqlite3
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

login()