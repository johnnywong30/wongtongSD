# Johnny Wong
# K24 -- A RESTful Journey Skyward
# 2018-11-14

from flask import Flask, render_template, request
import urllib.request as url_req
app = Flask(__name__) #instantiate flask obj

url = url_req.urlopen('https://api.nasa.gov/planetary/apod?api_key=UGzS4YPwatWhmTQmlWXehivYD5GzSU9hAYnQJMq8')

response = url.read()


# index
@app.route('/')
def index():
    print(response)
    print('The url: ' )
if __name__ == '__main__':
    app.debug = True
    app.run()
