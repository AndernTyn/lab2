# Импорт объекта db из текущего пакета.
from . import db

# Импорт класса UserMixin из flask_login для удобства работы с пользователями.
from flask_login import UserMixin

# Определение модели данных для пользователей в приложении.
class users(db.Model, UserMixin):
    # Определение уникального идентификатора пользователя (первичный ключ).
    id = db.Column(db.Integer, primary_key=True)

    # Определение имени пользователя, обязательное и уникальное поле.
    username = db.Column(db.String(30), nullable=False, unique=True)

    # Определение хэшированного пароля пользователя.
    password = db.Column(db.String(102), nullable=False)

    # Метод __repr__ для удобного отображения объекта в виде строки при отладке.
    def __repr__(self):
        return f'id:{self.id}, username:{self.username}'

# Определение модели данных для статей в приложении.
class articles(db.Model):
    # Определение уникального идентификатора статьи (первичный ключ).
    id = db.Column(db.Integer, primary_key=True)

    # Определение внешнего ключа, связывающего статью с пользователем.
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Определение заголовка статьи, обязательного поля.
    title = db.Column(db.String(50), nullable=False)

    # Определение текста статьи, обязательного поля.
    article_text = db.Column(db.Text, nullable=False)

    # Флаг, указывающий, является ли статья избранной (логическое значение).
    is_favorite = db.Column(db.Boolean)

    # Флаг, указывающий, является ли статья общедоступной (логическое значение).
    is_public = db.Column(db.Boolean)

    # Количество лайков статьи.
    likes = db.Column(db.Integer)
