from flask import Blueprint, redirect, url_for, render_template
# пакет и класс 
# хранит имя программы
# возвращает нужный нам путь в виде строки.
lab3=Blueprint('lab3', __name__)


@lab3.route('/lab3')
def lab():
    return render_template('lab2.html')