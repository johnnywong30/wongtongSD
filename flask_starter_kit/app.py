# Team weakKnees
# Johnny Wong
# K14 -- Do I Know You?
# 2018-10-02

from flask import Flask, render_template, request
app = Flask(__name__) #instantiate flask obj


# redirects root dir to /occupations
@app.route('/')
def redir():


@app.route('/occupations')
def go():


if __name__ == '__main__':
    app.debug = True
    app.run()
  
