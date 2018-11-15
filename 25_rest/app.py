# Johnny Wong
# K25 -- Getting More REST
# 2018-11-15

from flask import Flask, render_template, request
import urllib.request as url_req, urllib.parse as url_parse, json
app = Flask(__name__) #instantiate flask obj

# Yahoo! Weather does not need an api_key

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = "select wind, atmosphere, astronomy, item from weather.forecast where woeid={0}".format('2459115')
yql_url = baseurl + url_parse.urlencode({'q':yql_query}) + "&format=json"
result = url_req.urlopen(yql_url).read()
data = json.loads(result)
#print(data['query']['results'])

results = data['query']['results']['channel']
wind_conds = results['wind']
atmosphere_conds = results['atmosphere']
astronomy_conds = results['astronomy']
title = results['item']['title']
weather = results['item']['condition']
border = '==================={0}======================'

stuff = (wind_conds, atmosphere_conds, astronomy_conds, title, weather)
print(border.format('WIND'))
print(stuff[0])
print(border.format('ATMOSPHERE'))
print(stuff[1])
print(border.format('ASTRONOMY'))
print(stuff[2])
print(border.format('TITLE'))
print(stuff[3])
print(border.format('WEATHER'))
print(stuff[4])

# index
@app.route('/')
def index():
    return render_template('template.html', wind = wind_conds, atmo = atmosphere_conds, astro = astronomy_conds, weather = weather['text'], date = weather['date'], title = title)

if __name__ == '__main__':
    app.debug = True
    app.run()
