from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry

@app.route('/')
def show_entries():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('entries/index.html', entries=entries)


@app.route('/entries', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry(
            title=request.form['title'],
            text=request.form['text']
            )
    db.session.add(entry)
    db.session.commit()
    flash('A new article has been created.')
    return redirect(url_for('show_entries'))


@app.route('/entries/new', methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')


@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)