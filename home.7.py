import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()
# Один к одному - One to One
# Многие к многим - Many to Many
# Один к многим - One to Many
# Многие к одному  - Many to One
# Joins
#  INNER JOIN  возвращает только те строки,
#  которые имеют соответствие в обеих таблицах.
# LEFT JOIN возвращает все строки из левой таблицы и соответствующие строки из правой таблицы.
# Если соответствий нет, подставляются NULL.
# RIGHT JOIN аналогично LEFT JOIN, но возвращает все строки из правой таблицы.
# FULL OUTER JOIN возвращает строки, имеющие соответствия хотя бы в одной из таблиц.


def create_db():
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                userid INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор пользователя
                fio VARCHAR(100) NOT NULL,                -- ФИО пользователя
                age INTEGER NOT NULL,
                hobby TEXT
            )
        ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                gradeid INTEGER PRIMARY KEY AUTOINCREMENT, -- Уникальный идентификатор записи о оценке
                userid INTEGER,                            -- Внешний ключ, который ссылается на userid из таблицы 'users'
                subject VARCHAR(100) NOT NULL,             -- Название предмета
                grade INTEGER NOT NULL,                    -- Оценка
                FOREIGN KEY (userid) REFERENCES users(userid) -- Определяем связь с таблицей 'users'
            )
        ''')

    connect.commit()

create_db()

def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio} добавлен")

def delete_user_by_id(id):
    cursor.execute('DELETE FROM users WHERE userid = ?', (id,))
    connect.commit()

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    if users:
        print("Список всех пользователей:")
        for user in users:
            print(f'FIO: {user[1]}, AGE: {user[2]}, HOBBY: {user[3]}')
    else:
        print("Список пользователей пуст")

def get_user_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?', (age,))
    users = cursor.fetchall()
    print(f"Пользователи по возрасту: {users}")

def update_user_age_by_id(id, age):
    cursor.execute('UPDATE users SET age = ? WHERE userid = ?', (age, id))
    connect.commit()

def add_grade(user_id, subject, grade):
    cursor.execute('INSERT INTO grades (userid, subject, grade) VALUES (?, ?, ?)', (user_id, subject, grade))
    connect.commit()

def get_users_with_grades():
    cursor.execute('''
    SELECT users.fio, users.age, grades.subject, grades.grade
    FROM users
    INNER JOIN grades ON users.userid = grades.userid
    ''')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def get_all_data_full_outer_join():
    cursor.execute('''
    SELECT a.*, b.*
    FROM users a
    LEFT JOIN grades b ON a.userid = b.userid
    UNION ALL
    SELECT a.*, b.*
    FROM users a
    RIGHT JOIN grades b ON a.userid = b.userid
    WHERE a.userid IS NULL
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)


try:
    add_user("Иван Иванов", 30, "Чтение")
    add_user("Мария Петрова", 25, "Танцы")
    add_grade(1, "Математика", 5)
    add_grade(2, "Литература", 4)

    get_all_users()
    get_users_with_grades()
    get_all_data_full_outer_join()
except sqlite3.Error as e:
    print(f"Произошла ошибка: {e}")

connect.close()
