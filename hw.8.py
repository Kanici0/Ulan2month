import sqlite3

# Подключение к базе данных
connect = sqlite3.connect('users.db')
cursor = connect.cursor()

# Создание базы данных и таблиц с различными связями
def create_db():
    # Таблица пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            userid INTEGER PRIMARY KEY AUTOINCREMENT,
            fio VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
    ''')

    # Таблица оценок, связь один ко многим
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS grades (
            gradeid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            subject VARCHAR(100) NOT NULL,
            grade INTEGER NOT NULL,
            FOREIGN KEY (userid) REFERENCES users(userid)
        )
    ''')

    # Таблица профилей, связь один к одному
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profiles (
            profileid INTEGER PRIMARY KEY AUTOINCREMENT,
            userid INTEGER,
            address TEXT,
            phone TEXT,
            FOREIGN KEY (userid) REFERENCES users(userid)
        )
    ''')

    # Таблица курсов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            courseid INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name VARCHAR(100) NOT NULL
        )
    ''')

    # Промежуточная таблица для связи многие ко многим
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_courses (
            userid INTEGER,
            courseid INTEGER,
            FOREIGN KEY (userid) REFERENCES users(userid),
            FOREIGN KEY (courseid) REFERENCES courses(courseid),
            PRIMARY KEY (userid, courseid)
        )
    ''')

    connect.commit()

create_db()

# CRUD операции
def add_user(fio, age, hobby=""):
    cursor.execute('INSERT INTO users(fio, age, hobby) VALUES (?, ?, ?)', (fio, age, hobby))
    connect.commit()
    print(f"Пользователь {fio} добавлен")

def add_grade(user_id, subject, grade):
    cursor.execute('INSERT INTO grades (userid, subject, grade) VALUES (?, ?, ?)', (user_id, subject, grade))
    connect.commit()
    print(f"Оценка добавлена для пользователя с ID {user_id}")

def add_profile(user_id, address, phone):
    cursor.execute('INSERT INTO profiles (userid, address, phone) VALUES (?, ?, ?)', (user_id, address, phone))
    connect.commit()
    print(f"Профиль для пользователя с ID {user_id} добавлен")

def add_course(course_name):
    cursor.execute('INSERT INTO courses (course_name) VALUES (?)', (course_name,))
    connect.commit()
    print(f"Курс {course_name} добавлен")

def add_user_to_course(user_id, course_id):
    cursor.execute('INSERT INTO user_courses (userid, courseid) VALUES (?, ?)', (user_id, course_id))
    connect.commit()
    print(f"Пользователь с ID {user_id} добавлен на курс с ID {course_id}")

# Пример запросов с JOIN

# INNER JOIN - пользователи с оценками
def get_users_with_grades():
    cursor.execute('''
    SELECT users.fio, users.age, grades.subject, grades.grade
    FROM users
    INNER JOIN grades ON users.userid = grades.userid
    ''')
    rows = cursor.fetchall()
    print("Пользователи с их оценками:")
    for row in rows:
        print(f"FIO: {row[0]}, AGE: {row[1]}, SUBJECT: {row[2]}, GRADE: {row[3]}")

# LEFT JOIN - пользователи и их курсы (может быть пустое значение курса)
def get_users_with_courses():
    cursor.execute('''
    SELECT users.fio, users.age, courses.course_name
    FROM users
    LEFT JOIN user_courses ON users.userid = user_courses.userid
    LEFT JOIN courses ON user_courses.courseid = courses.courseid
    ''')
    rows = cursor.fetchall()
    print("Пользователи с курсами (LEFT JOIN):")
    for row in rows:
        print(f"FIO: {row[0]}, AGE: {row[1]}, COURSE: {row[2]}")

# Многие ко многим - таблица user_courses
def get_users_with_multiple_courses():
    cursor.execute('''
    SELECT users.fio, courses.course_name
    FROM users
    JOIN user_courses ON users.userid = user_courses.userid
    JOIN courses ON user_courses.courseid = courses.courseid
    ''')
    rows = cursor.fetchall()
    print("Пользователи с их курсами (Many-to-Many):")
    for row in rows:
        print(f"FIO: {row[0]}, COURSE: {row[1]}")

# Вложенные запросы - пользователи с максимальной оценкой
def get_users_with_highest_grade():
    cursor.execute("""
        SELECT fio, subject, grade
        FROM users JOIN grades ON users.userid = grades.userid
        WHERE grade = (SELECT MAX(grade) FROM grades)
    """)
    users = cursor.fetchall()
    print(f"Пользователи с максимальным баллом")
    for user in users:
        print(f"FIO: {user[0]}, SUBJECT: {user[1]}, GRADE: {user[2]}")

# Представления (Views)
def create_users_view():
    cursor.execute("""
        CREATE VIEW IF NOT EXISTS user_view AS
        SELECT fio, age, hobby
        FROM users
        WHERE age < 26
    """)
    connect.commit()

def get_young_users():
    cursor.execute('SELECT * FROM user_view')
    young_users = cursor.fetchall()
    print("Молодые пользователи (моложе 26 лет):")
    for user in young_users:
        print(f"FIO: {user[0]}, AGE: {user[1]}, HOBBY: {user[2]}")

# Пример использования:
# Добавление пользователей
add_user("Илья Муромец", 25, "фехтование")
add_user("John Doe", 30, "шахматы")

# Добавление курсов
add_course("Математика")
add_course("Физика")

# Добавление оценок
add_grade(1, "Математика", 5)
add_grade(2, "Физика", 4)

# Добавление профилей
add_profile(1, "Москва, ул. Ленина, д. 10", "123456789")
add_profile(2, "Санкт-Петербург, ул. Пушкина, д. 20", "987654321")


add_user_to_course(1, 1)
add_user_to_course(2, 2)


get_users_with_grades()
get_users_with_courses()
get_users_with_multiple_courses()
get_users_with_highest_grade()
create_users_view()
get_young_users()
