# Johnny Wong
# SoftDev1 pd8
# K26 -- Getting More REST
# 2018-11-16

from flask import Flask, render_template, request
import urllib.request as url_req, urllib.parse as url_parse, json
app = Flask(__name__) #instantiate flask obj

memeAPI_KEY = "4b59a249-20c3-4337-afe7-af76b47bbb20"

def getMeme(size):
    baseurl = "http://version1.api.memegenerator.net//Generators_Select_ByPopular?pageIndex=0&pageSize={0}&days=&apiKey={1}".format(str(size), memeAPI_KEY)
    result = url_req.urlopen(baseurl).read()
    data = json.loads(result)['result']
    return data

data = getMeme(11)
#print(data)

def rankMemes(data):
    '''
    Return a list of rankings that contain the most popular memes in order given data
    '''
    def sortMemes(memeList):
        '''
        Selection Sort for memeList
        '''
        sorted = []
        while len(sorted) < len(memeList):
            min = 0
            pos = 0
            for i in range(len(memeList)):
                if memeList[i] not in sorted:
                    if min == 0:
                        min = memeList[i][1]
                        pos = i
                    elif min > memeList[i][1]:
                        min = memeList[i][1]
                        pos = i
            sorted.append(memeList[pos])
        return sorted

    rankings = []
    for meme in data:
        rankings.append((meme['displayName'], meme['ranking'], meme['imageUrl']))
    return sortMemes(rankings)

def printMemes(list_of_memes):
    for i in list_of_memes:
        print(i)

list_of_memes = rankMemes(data)
printMemes(list_of_memes)


def getTotalPopulation(country):
    '''
    Country string is case sensitive. eg. string for the United States should be 'United States'.
    Returns a list of tuples, where the first tuple contains the population for the country today
    and the second tuple contains the population for the country tomorrow.
    '''
    baseurl = "http://api.population.io/1.0/population/{0}/today-and-tomorrow/?format=json".format(country.replace(' ','%20'))
    result = url_req.urlopen(baseurl).read()
    data = json.loads(result)['total_population']
    population_list = [country]
    for i in data:
        population_list.append((i['date'], i['population']))
    return population_list

US_pop = getTotalPopulation('United States')
print(US_pop)

def getDoggo(breed):
    '''
    Returns the url of a doggo of input breed
    '''
    baseurl = 'https://dog.ceo/api/breed/{0}/images/random'.format(breed.replace(' ', '%20'))
    result = url_req.urlopen(baseurl).read()
    link = json.loads(result)['message']
    return link

corgi = getDoggo('corgi')


# index
@app.route('/')
def index():
    return render_template('template.html', memeList=list_of_memes, country=US_pop[0], date0=US_pop[1][0], date1=US_pop[2][0], pop0=US_pop[1][1], pop1=US_pop[2][1], doggo=corgi)

if __name__ == '__main__':
    app.debug = True
    app.run()
