import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

def create_db():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                userid INTEGER PRIMARY KEY AUTOINCREMENT,
                fio VARCHAR(100) NOT NULL,
                age INTEGER NOT NULL,
                hobby TEXT
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
                userid INTEGER,
                subject VARCHAR(100) NOT NULL,
                grade INTEGER NOT NULL,
                FOREIGN KEY (userid) REFERENCES users(userid)
            )
        ''')

    connect.commit()

create_db()

def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio} добавлен")

def get_users_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?', (age,))
    users = cursor.fetchall()

    if users:
        print(f"Пользователи с возрастом {age}:")
        for user in users:
            print(f"ID: {user[0]}, FIO: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}")
    else:
        print(f"Пользователей с возрастом {age} не найдено")


add_user("Иван ", 20, "Чтение")
add_user("Мария ", 25, "Танцы")
add_user("Петр ", 20, "Спорт")

get_users_by_age(20)
get_users_by_age(25)

connect.close()
