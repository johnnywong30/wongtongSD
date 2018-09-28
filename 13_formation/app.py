# Johnny Wong
# SoftDev1 pd8
# K13 -- Echo Echo Echo
# 2018-09-28

from flask import Flask, render_template, request
app = Flask(__name__) #instantiate flask Object


@app.route('/')
def home():
    print(app)
    return render_template('formTemplate.html')

@app.route('/auth', methods=['POST'])
def authenticate():
    print(app)
    print(request)
    print(request.form)
    print(request.form)
    print(request.headers)
    return render_template('responseTemplate.html',
    username = request.form['username'],
    requestMethod = request.method
    )




if __name__ == '__main__':
    app.debug = True
    app.run()
