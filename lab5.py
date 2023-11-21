# Подключение необходимых библиотек и модулей
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, redirect, render_template, request, session
import psycopg2

# Создание Blueprint с именем "lab5"
lab5 = Blueprint("lab5", __name__)

# Функции подключения и закрытия базы данных
def dbConnect():
    # Подключение к базе данных PostgreSQL
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="knowledge_base_for_tunyak",
        user="tunyak_knowledge_base",
        password="123"
    )
    return conn

def dbClose(cursor, connection):
    # Закрытие курсора и соединения с базой данных
    cursor.close()
    connection.close()

# Функция для проверки разрешений пользователя
def user_has_permission_to_create_article(user_id):
    # Подключение к базе данных
    conn = dbConnect()
    cur = conn.cursor()

    try:
        # Проверка существования пользователя с указанным ID
        cur.execute("SELECT id FROM users WHERE id = %s", (user_id,))
        result = cur.fetchone()
        return result is not None
    finally:
        # Закрытие курсора и соединения с базой данных
        dbClose(cur, conn)

# Маршрут для вывода всех пользователей в консоль
@lab5.route("/lab5")
def main():
    # Проверка аутентификации пользователя
    user_is_authenticated = 'user_id' in session
    current_user = {"username": "Гость"}

    if user_is_authenticated:
        # Если пользователь аутентифицирован, установить его имя пользователя
        current_user["username"] = session["username"]

    # Отображение главной страницы
    return render_template("lab5.html", user_is_authenticated=user_is_authenticated, current_user=current_user)

@lab5.route("/lab5/users")
def show_users():
    # Подключение к базе данных
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")

    # Получение всех пользователей из базы данных
    result = cur.fetchall()

    # Закрытие курсора и соединения с базой данных
    dbClose(cur, conn)

    # Отображение страницы с пользователями
    return render_template("users.html", users=result)

@lab5.route('/lab5/register', methods=["GET", "POST"])
def registerPage():
    errors = []

    if request.method == "GET":
        # Отображение страницы регистрации при GET-запросе
        return render_template("register.html", errors=errors)

    # Получение данных формы при POST-запросе
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username and password):
        # Проверка наличия заполненных полей
        errors.append("Пожалуйста, заполните все поля")
        return render_template("register.html", errors=errors)

    # Хеширование пароля
    hashPassword = generate_password_hash(password)

    # Подключение к базе данных
    conn = dbConnect()
    cur = conn.cursor()

    cur.execute(f"SELECT username FROM users WHERE username = %s;", (username,))

    if cur.fetchone() is not None:
        # Проверка уникальности имени пользователя
        errors.append("Пользователь с данным именем уже существует")
        conn.close()
        cur.close()
        return render_template("register.html", errors=errors)

    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, hashPassword))
    conn.commit()
    conn.close()
    cur.close()

    # Перенаправление на страницу логина после успешной регистрации
    return redirect("/lab5/logins")

@lab5.route('/lab5/logins', methods=["GET", "POST"])
def loginPage():
    errors = []

    if request.method == "GET":
        # Отображение страницы логина при GET-запросе
        return render_template("logins.html", errors=errors)

    # Получение данных формы при POST-запросе
    username = request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        # Проверка наличия заполненных полей
        errors.append("Пожалуйста, заполните все поля")
        return render_template("logins.html", errors=errors)

    with dbConnect() as conn, conn.cursor() as cur:
        try:
            # Проверка правильности логина и пароля
            cur.execute("SELECT id, password FROM users WHERE username = %s", (username,))
            result = cur.fetchone()

            if result is None:
                errors.append("Неправильный логин или пароль")
                return render_template("logins.html", errors=errors)

            userID, hashPassword = result

            if check_password_hash(hashPassword, password):
                # Успешная аутентификация
                session['user_id'] = userID
                session['username'] = username
                return redirect("/lab5")
            else:
                errors.append("Неправильный логин или пароль")
                return render_template("logins.html", errors=errors)

        except Exception as e:
            errors.append(f"Ошибка при выполнении запроса: {str(e)}")
            return render_template("logins.html", errors=errors)

@lab5.route('/lab5/logout')
def logout():
    # Выход пользователя из системы
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect("/lab5/logins")

@lab5.route('/lab5/new_article', methods=["GET", "POST"])
def new_article():
    # Проверка аутентификации пользователя
    if 'user_id' not in session:
        return redirect('/lab5/logins')

    user_id = session['user_id']

    if not user_has_permission_to_create_article(user_id):
        # Проверка разрешений пользователя на создание статьи
        return redirect('/lab5')

    sent = False

    if request.method == "GET":
        # Отображение страницы создания новой статьи при GET-запросе
        return render_template("new_article.html", errors=[], sent=sent)
    elif request.method == "POST":
        # Получение данных формы при POST-запросе
        title = request.form.get("title_article")
        text_article = request.form.get("text_article")

        if not (title and text_article):
            # Проверка наличия заполненных полей
            errors = ["Пожалуйста, заполните все поля"]
            return render_template("new_article.html", errors=errors, sent=sent)

        # Подключение к базе данных
        conn = dbConnect()
        cur = conn.cursor()

        try:
            # Вставка новой статьи в базу данных
            cur.execute(
                "INSERT INTO articles (user_id, title, article_text, is_public) VALUES (%s, %s, %s, %s) RETURNING id;",
                (user_id, title, text_article, True)
            )
            new_article_id = cur.fetchone()[0]
            conn.commit()

            print(f"Inserted new article with ID: {new_article_id}")

            sent = True

        except Exception as e:
            errors = [f"Ошибка при выполнении запроса: {str(e)}"]
            return render_template("new_article.html", errors=errors, sent=sent)
        finally:
            # Закрытие курсора и соединения с базой данных
            dbClose(cur, conn)

        if new_article_id is not None:
            return render_template("new_article.html", errors=[], sent=sent)
        else:
            errors = ["Не удалось получить идентификатор новой статьи"]
            return render_template("new_article.html", errors=errors, sent=sent)

@lab5.route("/lab5/articles/<int:article_id>")
def getArticle(article_id):
    user_id = session.get("user_id")  # Получение ID пользователя из сессии
    # Проверка аутентификации пользователя
    if user_id is not None:
        conn = dbConnect()
        cur = conn.cursor()
        # SQL-инъекция! Используйте параметризованные запросы для безопасности.
        cur.execute("SELECT title, article_text FROM articles WHERE id = %s AND user_id = %s", (article_id, user_id))
        # Получение одной строки из результата запроса
        articleBody = cur.fetchone()
        dbClose(cur, conn)
        if articleBody is None: 
            return "Not found!"
        # Разделение текста статьи на абзацы
        text = articleBody[1].splitlines()
        return render_template("articleN.html", article_text=text, article_title=articleBody[0], username=session.get("username"))
    else:
        # Перенаправление на страницу логина, если пользователь не аутентифицирован
        return redirect("/lab5/logins")

# Добавление маршрута для отображения статей пользователя
@lab5.route("/lab5/my_articles")
def my_articles():
    current_user = {"username": None}  # Исправлено присвоение
    if 'user_id' in session:
        user_id = session['user_id']

        conn = dbConnect()
        cur = conn.cursor()

        try:
            # Получение статей, принадлежащих текущему пользователю
            cur.execute("SELECT id, title, article_text, likes FROM articles WHERE user_id = %s;", (user_id,))
            articles = [{'id': row[0], 'title': row[1], 'article_text': row[2], 'likes': row[3]} for row in cur.fetchall()]

            current_user["username"] = session.get("username")  # Установка имени пользователя для текущего пользователя

            return render_template("articles.html", user_is_authenticated=True, articles=articles, current_user=current_user)
        finally:
            # Закрытие курсора и соединения с базой данных
            dbClose(cur, conn)
    else:
        # Если пользователь не аутентифицирован, перенаправление на страницу логина
        return redirect('/lab5/logins')

# Добавление маршрута для добавления статьи в избранное
@lab5.route('/lab5/articles/<int:article_id>/add_to_favorite')
def add_to_favorite(article_id):
    if 'user_id' not in session:
        return redirect('/lab5/logins')

    user_id = session['user_id']

    conn = dbConnect()
    cur = conn.cursor()

    try:
        # Обновление флага "избранное" для статьи
        cur.execute("UPDATE articles SET is_favorite = true WHERE id = %s AND user_id = %s;", (article_id, user_id))
        conn.commit()
    finally:
        # Закрытие курсора и соединения с базой данных
        dbClose(cur, conn)

    # Перенаправление на страницу со статьями пользователя
    return redirect('/lab5/my_articles')

# Добавление маршрута для лайка статьи
@lab5.route('/lab5/like_article/<int:article_id>')
def like_article(article_id):
    if 'user_id' not in session:
        return redirect('/lab5/logins')

    user_id = session['user_id']

    conn = dbConnect()
    cur = conn.cursor()

    try:
        # Проверка, ставил ли пользователь лайк ранее
        cur.execute("SELECT likes FROM articles WHERE id = %s AND user_id = %s;", (article_id, user_id))
        previous_likes = cur.fetchone()

        if previous_likes is not None and previous_likes[0] is not None:
            # Пользователь уже поставил лайк
            return redirect('/lab5')  # Можете перенаправить на другую страницу или оставить без изменений
        else:
            # Увеличение количества лайков
            cur.execute("UPDATE articles SET likes = COALESCE(likes, 0) + 1 WHERE id = %s;", (article_id,))
            conn.commit()
    finally:
        # Закрытие курсора и соединения с базой данных
        dbClose(cur, conn)

    # Перенаправление на страницу со статьями пользователя
    return redirect('/lab5/my_articles')
