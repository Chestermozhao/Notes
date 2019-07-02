## [flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)

- create table
    - models: 定義表結構
    ```python
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    
    app = Flask(__name__)
    # import from env or settings
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    # registere
    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)

        def __repr__(self):
            return '<User %r>' % self.username
    ```
    - 創建表結構(Python Shell)
    ```python
    from yourapplication import db
    db.create_all()
    ```
    - 插入數據
    ```python
    from yourapplication import User
    admin = User(username='admin', email='admin@example.com')
    guest = User(username='guest', email='guest@example.com')
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()
    ```
    - 查詢數據
    ```python
    # 查詢全部
    User.query.all()
    # 條件查詢
    User.query.filter_by(username='admin').first()
    ```
    - [外鍵關聯](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#simple-relationships)
- 補充閱讀
    - [flask-sqlalchemy doc](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/#flask_sqlalchemy.SQLAlchemy)
    - [sqlalchemy doc](https://docs.sqlalchemy.org/en/13/orm/scalar_mapping.html#module-sqlalchemy.orm)
