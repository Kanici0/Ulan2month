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

    # Создание таблицы 'grades'
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

# CRUD - Create Reade Update Delete
#
# def add_user(fio, age, hobby=""):
#     cursor.execute('INSERT INTO users(fio, age) VALUES (?, ?)', (fio, age))
#     connect.commit()
#     print(f"Пользователь {fio}, Добавлен")

# add_user('Илья Муровец', 25)
# add_user('John Doe1', 25)
# add_user('John Doe2', 27)
# add_user('John Doe3', 28)

def delete_user_by_id(id):
    cursor.execute(
        'DELETE FROM users WHERE user_id = ?',
        (id,)
    )

    connect.commit()

# delete_user_by_id(3)

def get_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    # return print(users)

    if users:
        print(f"Список всех пользователей:")
        for user in users:
            print(f'FIO: {user[0]}, AGE: {user[1]}')
    else:
        print(f'Список пользователей пуст')


# get_all_users()



def get_user_by_age(age):
    cursor.execute('SELECT * FROM users WHERE age = ?',
                   (age,))
    users = cursor.fetchall()
    return print(f"Пользователи по возрасту {users}")

# get_user_by_age(25)


def update_user_age_by_id(id, age):
    cursor.execute(
        'UPDATE users SET fio = ? WHERE user_id = ?',
        (age, id)
    )

    connect.commit()

# update_user_age_by_id(4, " Арзыбек Абды")

get_all_users()


def add_grade(user_id, subject, grade):
    cursor.execute(
        "INSERT INTO grades (userid, subject, grade) VALUES (?,?,?)",
        (user_id, subject, grade)
    )

    connect.commit()

add_grade(3, "Алгебра", 5)
add_grade(2, "Алгебра", 5)

def get_users_with_grades():
    cursor.execute("""
    SELECT users.fio, users.age, grades.subject, grades.grade
    FROM users INNER JOIN grades ON users.userid = grades.userid
    """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
get_all_users()
get_users_with_grades()


connect.close()
connect = sqlite3.connect('users.db')

def get_average_age():
    cursor.execute('SELECT AVG (age) FROM users')
    avg_age = cursor.fetchall()[0]
    print(f'average age: {avg_age}')
print('\n --- arregation functions ---')

# def get_grade_statistics():
#     cursor.execute('''
#      SELECT grades.subject, AVG(grade) as avg_grade,MAX(grade) as max_grade,MAX(grade) as max_grade
#      FROM grades
#      GROUP BY grade
#      ''')


def get_user_highest_grade():
    cursor.execute(""" 
    SELECT fio,subject,grade
    FROM users JOIN gredes 
    ON users.userid = gredes.userid
    WHERE grade = (SELECT MAX(grade) FROM grades)
    """)

    users = cursor.fetchall()
    print(f'пользователь с максмальным балом ')
    print(users)
    for user in users:
        print(f'FIO: {user[0]}, SUB: {user[1]}, GR: {user[2]}')


get_users_with_grades()


def create_users_view():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users_viwe AS
    SELECT fio,age,hobby
    FROM users
    WHERE age < 30
    """)
connect.commit()
print('пользователь users_view создано ')
