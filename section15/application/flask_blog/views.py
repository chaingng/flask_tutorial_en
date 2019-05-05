from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('entries/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            print('User name is different')
        elif request.form['password'] != app.config['PASSWORD']:
            print('Password is different')
        else:
            session['logged_in'] = True
            return redirect('/')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')
