import  sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute("""


    CREATE TABLE   users(
    fio VARCHAR (100) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )


""")


connect.commit()

# CRUD - Creat Read Update Delete
def add_user(foi,age,hobby):
    cursor.execute("""
    INSERT INTO users (foi,age,hobby)VALUES (?,?,?),(fio,age,hobby)""")

add_user('вася пупкин ',25,'плавать ')
connect.commit()




def git_all_user():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print('список пользователя ')
        for user in users:
            print(f'FIO:{user[0]} AGE:{user[1]} HOBBY:{user[2]}')
    else:
        print(f'Список пуст ')

git_all_user()
connect.close()





