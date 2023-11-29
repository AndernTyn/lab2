from flask import Blueprint, render_template, request, redirect
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6 = Blueprint("lab6", __name__)

@lab6.route("/lab6/check")
def main():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"

@lab6.route("/lab6/checkarticles")
def mainart():
    my_articles = articles.query.all()
    for article_item in my_articles:
        print(f"{article_item.title}-{article_item.article_text}")
    return "Result in console!"


@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register6.html")
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    isUserExist = users.query.filter_by(username = username_form).first()

    errors = []

    if isUserExist is not None:
        errors.append("Такой пользователь уже существует!")
        return render_template("register6.html", errors = errors)
    elif not username_form:
        errors.append("Введите имя пользователя!")
        return render_template("register6.html", errors=errors)
    elif len(password_form) < 5:
        errors.append("Пароль должен содержать не менее 5 символов!")
        return render_template("register6.html", errors=errors)

    hashedPswd = generate_password_hash(password_form, method="pbkdf2")

    newUser = users(username = username_form, password = hashedPswd)

    db.session.add(newUser)

    db.session.commit()

    return redirect("/lab6/login")

@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login6.html")
    
    errors = []
    
    username_form = request.form.get("username")
    password_form = request.form.get("password")

    my_user = users.query.filter_by(username = username_form).first()

    if not (username_form or password_form):
        errors.append("Введите имя пользователя и пароль!")
        return render_template("login6.html", errors = errors)
    elif my_user is None:
        errors.append("Такого пользователя не существует! Зарегестрируйтесь!")
        return render_template("login6.html", errors = errors)
    elif my_user is not check_password_hash(my_user.password, password_form):
        errors.append("Введите правильный пароль!")
        return render_template("login6.html", errors = errors)
    elif my_user is not None:
        if check_password_hash(my_user.password, password_form):
            login_user(my_user, remember=False)
            return redirect("/lab6/articles")
    
    return render_template("login6.html")