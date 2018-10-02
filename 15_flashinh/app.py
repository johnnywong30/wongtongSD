# Team weakKnees
# Johnny Wong
# K14 -- Do I Know You?
# 2018-10-02

from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__) #instantiate flask obj
app.secret_key = os.urandom(32)


@app.route('/')
def index():
    if 'jwong25' in session:
        return render_template('welcomeTemplate.html', title = 'weakKnees', username = 'jwong25')
    return render_template('formTemplate.html', title = 'weakKnees')

@app.route('/login')
def login():
    user = request.args['username']
    password = request.args['password']
    message = None
    if user != 'jwong25' or password != 'jwong25':
        if user != 'jwong25' and password == 'jwong25':
            message = "Invalid username. Please try again"
        else:
            message = "Invalid password. Please try again"
    else:
        session['jwong25'] = 'jwong25'
        return redirect(url_for('index'))
    return render_template('formTemplate.html', title = 'weakKnees', error = message)


@app.route('/logout')
def logout():
    session.pop('jwong25', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run()
