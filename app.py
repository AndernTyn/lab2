from flask import Flask, redirect, url_for
app=Flask(__name__)

@app.route("/")
def slesh():
     return redirect('/menu', code=302)

@app.route("/index")
def start():
    return redirect('/menu', code=302)


@app.route('/lab1')
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title>Туняк Андрей Николаевич, Лабораторная 1</title>
    </head>
    <body>
        <header>
            Лабораторная работа 1
        </header>

        <h1>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.         
            
            <a href="/menu" target="_blank">Меню</a>
        </h1>

        <h2>Реализованные роуты</h2>

        <ul>
            <li><a href="/lab1/oak" target="_blank">/lab1/oak - Дуб</a></li>
            <li><a href="/lab1/student" target="_blank">/lab1/student - Студент</a></li>
            <li><a href="/lab1/python" target="_blank">/lab1/python - Питон</a></li>
            <li><a href="/lab1/car" target="_blank">/lab1/car - Жигули </a></li>
        </ul>

        <footer>
            &copy; Туняк Андрей, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>
"""

@app.route("/menu")
def menu():
    return """
<!DOCTYPE html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>
        <h2><a href="/lab1" target="_blank">Первая лабораторная</a></h2>

        <footer>
            &copy; Туняк Андрей, ФБИ-13, 3 курс, 2023
        </footer>
    </body>
</html>

"""

@app.route('/lab1/oak')
def oak():
    return '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>   
    <body>
        <h1><a href="/lab1" target="_blank">Дуб</a></h1>
        <div class='photo'><img src="''' + url_for('static', filename='oak.jpg') + '''">
        </div>    
    </body>
'''

@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
    <head>
        <title>Туняк Андрей Николаевич</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>
           Туняк Андрей Николаевич
        </h1>
        <div class='photo'><img src="''' + url_for('static', filename='ngtu.png') + '''">
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <head>
        <title>Туняк Андрей Николаевич</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>
           Python в русском языке встречаются названия пито́н или па́йтон) — высокоуровневый язык программирования общего 
           назначения с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение 
           производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. 
           Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью языка является 
           выделение блоков кода пробельными отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает 
           необходимость обращаться к документации. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов. 
           Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по 
           сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++.
        </h1>
        <h1>
           Python является мультипарадигменным языком программирования, поддерживающим императивное, процедурное, структурное, 
           объектно-ориентированное программирование, метапрограммирование и функциональное программирование. Задачи обобщённого 
           программирования решаются за счёт динамической типизации. Аспектно-ориентированное программирование частично 
           поддерживается через декораторы, более полноценная поддержка обеспечивается дополнительными фреймворками. 
           Такие методики как контрактное и логическое программирование можно реализовать с помощью библиотек или расширений. 
           Основные архитектурные черты — динамическая типизация, автоматическое управление памятью, полная интроспекция, механизм 
           обработки исключений, поддержка многопоточных вычислений с глобальной блокировкой интерпретатора (GIL), высокоуровневые 
           структуры данных. Поддерживается разбиение программ на модули, которые, в свою очередь, могут объединяться в пакеты.
        </h1>
        <h1>
           Эталонной реализацией Python является интерпретатор CPython, который поддерживает большинство активно используемых платформ 
           и являющийся стандартом де-факто языка. Он распространяется под свободной лицензией Python Software Foundation License, 
           позволяющей использовать его без ограничений в любых приложениях, включая проприетарные. CPython компилирует исходные 
           тексты в высокоуровневый байт-код, который исполняется в стековой виртуальной машине. 
           К другим трём основным реализациям языка относятся Jython (для JVM), IronPython (для CLR/.NET) и PyPy. 
           PyPy написан на подмножестве языка Python (RPython) и разрабатывался как альтернатива CPython с целью повышения скорости 
           исполнения программ, в том числе за счёт использования JIT-компиляции. Поддержка версии Python 2 закончилась в 2020 году. 
           На текущий момент активно развивается версия языка Python 3. Разработка языка ведётся через предложения по расширению языка PEP 
           (англ. Python Enhancement Proposal), в которых описываются нововведения, делаются корректировки согласно обратной связи от сообщества 
           и документируются итоговые решения.
        </h1>
        <div class='photo'><img src="''' + url_for('static', filename='python.png') + '''">
    </body>
</html>
'''

@app.route('/lab1/car')
def car():
    return '''
<!doctype html>
<html>
    <head>
        <title>Туняк Андрей Николавич</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>
            «Жигули́» (позднее — LADA Classic, неофициально — «ВАЗовская классика» или просто «классика») — семейство советских 
            и российских легковых автомобилей малого класса Волжского автомобильного завода, созданных на базе итальянского автомобиля 
            Fiat 124. Различные модели, которых всего было семь (не считая грузовых и иных модификаций), выпускались с 1970 по 2014 год, 
            став самым массовым семейством автомобилей в истории СССР и России, выпущенным в количестве 17,6 млн машин 
            (включая автомобили, собранные за рубежом).        
        </h1>
        
        <h1>
            16 августа 1966 года в Москве было подписано генеральное соглашение между итальянской компанией Fiat и советским Внешторгом 
            о научно-техническом сотрудничестве в области разработки легковых автомобилей. В его рамках был утвержден проект строительства 
            автозавода на территории СССР. Этим соглашением определялись и сами модели: два автомобиля в комплектации «норма» с кузовами 
            седан (ВАЗ-2101) и универсал (ВАЗ-2102), и автомобиль «люкс» (ВАЗ-2103). В качестве прототипа для «нормы» сразу был определён 
            Fiat 124, получивший в 1967 году титул «Автомобиль года».
        </h1>
        <div class='photo'><img src="''' + url_for('static', filename='car.jpg') + '''">
    </body>
</html>
'''