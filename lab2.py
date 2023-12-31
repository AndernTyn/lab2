from flask import Blueprint, redirect, url_for, render_template
# пакет и класс 
# хранит имя программы
# возвращает нужный нам путь в виде строки.
# отвечает за рендеринг шаблонов
lab2=Blueprint('lab2', __name__)


@lab2.route('/lab2')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/example')
def example():
        name, number, groupe, course='Туняк Андрей', 2, 'ФБИ-13', '3 курс'
        fruits = [
            {'name': 'яблоки', 'price': 100},
            {'name': 'груши', 'price': 120},
            {'name': 'апельсины', 'price': 80},
            {'name': 'мандарины', 'price': 95}, 
            {'name': 'манго', 'price': 321},
        ]
        books = [
        {'author': 'Джеймс Джойс', 'name': 'Улисс', 'genre': 'роман', 'pages': '1056'},
        {'author': 'Драйзер Т.', 'name': 'Трилогия желания', 'genre': 'роман', 'pages': '1152'},
        {'author': 'Толстой Л.', 'name': 'Война и мир', 'genre': 'роман-эпопея', 'pages': '1360'},
        {'author': 'Голсуорси Дж.', 'name': 'Сага о Форсайтах', 'genre': 'роман', 'pages': '1376'},
        {'author': 'Солженицын А.', 'name': 'Архипелаг ГУЛАГ', 'genre': 'роман', 'pages': '1424'},
        {'author': 'Палиссер Ч.', 'name': 'Квинканкс', 'genre': 'роман', 'pages': '1472'},
        {'author': 'Манн Т.', 'name': 'Иосиф и его братья', 'genre': 'роман', 'pages': '1492'},
        {'author': 'Музиль Р.', 'name': 'Человек без свойств', 'genre': 'роман', 'pages': '1774'},
        {'author': 'Пруст М.', 'name': 'В поисках утраченного времени', 'genre': 'роман', 'pages': '3031'},
        {'author': 'Кнаусгор К.', 'name': 'Моя борьба', 'genre': 'биография', 'pages': '3600'},
        ]
        return render_template('example.html', name=name, number=number, groupe=groupe, course=course, fruits=fruits, books=books)



@lab2.route('/lab2/vaz')
def vaz():
    return render_template('vaz.html')