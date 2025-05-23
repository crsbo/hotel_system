from flask import Flask, render_template, request, redirect, session, url_for
from models import init_db, get_db
import os  # ← لازم تكون فوق علشان تشتغل كويس

app = Flask(__name__)
app.secret_key = 'secret_key'
init_db()

@app.route('/')
def home():
    if 'user' in session:
        return redirect('/dashboard')
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['user'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect
