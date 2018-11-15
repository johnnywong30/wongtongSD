# Johnny Wong
# K26 --
# 2018-11-16

from flask import Flask, render_template, request
import urllib.request as url_req, urllib.parse as url_parse, json
app = Flask(__name__) #instantiate flask obj

API_KEY = "34b0833e-2bd7-4614-99d8-cec395f9c68c"

def getMeme(size):
    baseurl = "http://version1.api.memegenerator.net//Generators_Select_ByPopular?pageIndex=0&pageSize={0}&days=&apiKey={1}".format(size, API_KEY)
    result = url_req.urlopen(baseurl).read()
    data = json.loads(result)['result']
    return data

data = getMeme('6')

#print(data)
rank1 = data[0]
rank2 = data[1]
#print(rank1)
rank1_info = (rank1['displayName'], rank1['ranking'], rank1['imageUrl'])
border = '==================={0}======================'
print(border.format(rank1_info[0]))
print('Ranking: {0}'.format(rank1_info[1]))
print('imageUrl {0}'.format(rank1_info[2]))

'''
results = data['query']['results']['channel']
wind_conds = results['wind']
atmosphere_conds = results['atmosphere']
astronomy_conds = results['astronomy']
title = results['item']['title']
weather = results['item']['condition']


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
'''

# index
@app.route('/')
def index():
    return render_template('template.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
