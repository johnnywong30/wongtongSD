# Johnny Wong
# SoftDev1 pd8
# K08 -- Fill Yer Flask
# 2018-09-20

from flask import Flask

app = Flask(__name__) #instantiates the Flask class using a constructor

@app.route("/")
def home():
    return 'Hola mundo! <a href="/chicken"> Va a aqui para pollo por favor. </a>'

@app.route("/chicken")
def chicken():
    return 'Soy pollo. <a href="/sadchicken"> No me comas por favor. </a>'

@app.route("/sadchicken")
def sadchicken():
    return '<a href="/"> Soy muy triste ahora. </a>'

app.debug = True
app.run()
