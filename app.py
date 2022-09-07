from flask import Flask, render_template, url_for, request, redirect, flash, session, abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h6f'

menu = [{'name': "Установка", 'url': "install-flask"},
        {'name': "Первое приложение", 'url': "first-app"},
        {'name': "Обратная связь", 'url': "contact"}]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/hero')
def hero():
    print(url_for('hero'))
    return render_template('hero.html', title="О сайте", menu=menu)


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправленно', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f'Профель пользователя: {username}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'selfedu' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))

    return render_template('login.html', title='Авторизация', menu=menu)


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html', title='Страница не найдена', menu=menu)


# if __name__ == '__main__':
   #app.run(debug=True)
