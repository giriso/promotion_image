from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def phrase1():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def phrase2():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion_image')
def func():
    phrases = ['Человечество вырастает из детства',
               'Человечеству мала одна планета',
               'Мы сделаем обитаемыми безжизненные пока планеты',
               'И начнем с Марса!',
               'Присоединяйся!']

    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for('static', filename='img/image.jpg')}">
                          <div class="alert alert-secondary" role="alert">
                          {phrases[0]}
                          </div>
                          <div class="alert alert-success" role="alert">
                          {phrases[1]}
                          </div>
                          <div class="alert alert-secondary" role="alert">
                          {phrases[2]}
                          </div>
                          <div class="alert alert-warning" role="alert">
                          {phrases[3]}
                          </div>
                          <div class="alert alert-danger" role="alert">
                          {phrases[4]}
                          </div>
                          </body>
                        </html>'''



@app.route('/promotion')
def advertisment():
    return '<p>Человечество вырастает из детства.<br>Человечеству мала одна планета.<br>' \
           'Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!</p>'


@app.route('/image_mars')
def decoration():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/durka.jpg')}">
                        <h2>Вот она какая, красная планета.</h2>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.2')
