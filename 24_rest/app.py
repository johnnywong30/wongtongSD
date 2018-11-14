# Johnny Wong
# K24 -- A RESTful Journey Skyward
# 2018-11-14

from flask import Flask, render_template, request
import urllib.request as url_req, urllib.parse as url_parse, json
app = Flask(__name__) #instantiate flask obj

url = url_req.urlopen('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=ROvaiLc2fr3Lc4vqfeYdN7qghWc1KBsghyFUm5bF')

response = url.read()
resp_dict = json.loads(response)
#print('=================RESPONSE======================')
#print(response)
print('=================DICTIONARY======================')
first_photo = resp_dict['photos'][0]
camera_name = first_photo['camera']['full_name']
print(first_photo)
rover = first_photo['rover']['name']
print('=================ROVER=================')
print(rover)
print('=================URL======================')
img_url = resp_dict['photos'][0]['img_src']
print(img_url)

# index
@app.route('/')
def index():
    return render_template('template.html', camera = camera_name, rover = rover, url = img_url)

if __name__ == '__main__':
    app.debug = True
    app.run()
