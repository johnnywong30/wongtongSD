# Zebrows - Wei Wen Zhou, Johnny Wong
# SoftDev1 pd8
# K15 -- Oh yes, perhaps I do…
# 2018-10-02

from flask import Flask, render_template, request, session, url_for, redirect, flash
import os

app = Flask(__name__)

# Encode cookies
app.secret_key = os.urandom(32);

@app.route("/")
def index():
    if "Zebrows" in session:
        return render_template('welcome.html', user_welcome="Zebrows")
    else:
        return render_template('form.html', title='welcome')

@app.route("/auth", methods=["POST"])
def authenticate():
    usr = request.form["name"]
    pw = request.form["pass"]

    if usr != "Zebrows":
        flash("Incorrect username!")
        return render_template("error.html")
    if pw != "abc123":
        flash("Incorrect password!")
        return render_template("error.html")

    # add username to session
    session[usr] = pw

    return redirect(url_for("index"))

@app.route("/logout", methods=["POST"])
def logout():
    session.pop('Zebrows', None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.debug = True
    app.run()
