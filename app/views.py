from flask import render_template, flash, redirect, request, url_for, session
from app import app
from app import forms


@app.route('/books')
def index():
    user = {'nickname': 'Pedro'}
    books = [
        {
            'author': {'name': 'Jaroslav Hašek'},
            'title': 'The Fateful Adventures of the Good Soldier Švejk During the World War'
        },
        {
            'author': {'name': 'Glen Cook'},
            'title': 'The Black Company'
        },
        {
            'author': {'name': 'Stephen King'},
            'title': 'The Tommyknockers'
        },
    ]
    if 'username' in session:
        return render_template("books.html",
                               title='Home',
                               user=user,
                               books=books)
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        session['username'] = name
        flash('А туда ли ты зашел, ' + name + '?!')
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In',
                           form=form)


@app.route('/odminko', methods=['GET', 'POST'])
def odminko():
    return render_template('odminko.html',
                           title='Odminko',
                           )


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
