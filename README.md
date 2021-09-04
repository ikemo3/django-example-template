# django-example

Djangoのサンプルコードです。

## パッケージ

* Django 3.2.7
* black 21.8b0
* flake8 3.9.2

## 注意点

このリポジトリをcloneやforkして使うのは自由ですが、そのままでは問題があるため、
**本番環境では使わないでください**。

* `SECRET_KEY` が記載されている
* `DEBUG = True` で動いている
* SQLiteを使っている

## 起動方法

```sh
python3 -m venv venv
source venv/bin/activate
python manage.py migrate
python manage.py runserver
```

http://localhost:8000/ でアクセスできます。
