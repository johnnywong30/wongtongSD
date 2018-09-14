# Team hasFeet - Johnny Wong, Cheryl Qian
# SoftDev1 pd8
# K#06 -- StI/O: Divine your Destiny!
# 2018-09-13

import random

def listOfContent(nameOfFile):
    # opens the file with only read access
    f = open(nameOfFile, 'r')
    # skips the first line that lacks useable data
    skip = f.readline()
    # content stores the file's contents in one big list
    # where each element is each line of the file
    content = f.readlines()
    # closes file after reading
    f.close()
    return content


def dictOfOccupations(contentList):
    listOfOccupations = []

    # strips the "\n" character of each element in contentList
    strippedContentList = map(lambda str: str.strip("\n"), contentList)

    # iterate through each element in strippedContentList
    for elt in strippedContentList:
        # if the string does not start with a ", then it can just be split by the comma
        if elt.find('"') != 0:
            # append a list that contains an occupation and it's corresponding percentage
            keyAndValueSubList = elt.split(',')
            keyAndValueSubList[1] = float(keyAndValueSubList[1])
            listOfOccupations.append(keyAndValueSubList)
        else:
            # indexing this way removes the quotations and properly sorts the list in the format [ 'occupation', <percent>]
            keyAndValueSubList = [ elt[1 : elt.rfind('"')], elt[elt.rfind(',') + 1: len(elt)] ]
            keyAndValueSubList[1] = float(keyAndValueSubList[1])
            # otherwise, append a list that contains the entire occupation category and it's corresponding percentage
            listOfOccupations.append(keyAndValueSubList)
    # a list of sublists can be converted into a dictionary as long as each sublist contains a pair of a key and a value


    return dict(listOfOccupations)

def getKeyByValue(dict, index):
    # make a list of keys that can be indexed
    listOfKeys = list(dict.keys())
    # return the key that corresponds with the values' index
    return listOfKeys[index]


def randomOccupation(dictionary):
    # generate a random float from 0.0 to 99.8
    randNum = random.uniform(0.0, 99.8)
    currentTotal = 0
    generatedOccupationIndex = 0
    print(randNum)
    # iterate through each value in dictionary
    for val in dictionary.values():
        # if currentTotal is below the randNum, add val to total
        # and proceed to next occupation
        if currentTotal < randNum:
            currentTotal += val
            generatedOccupationIndex += 1
        # if currentTotal exceeds randNum, go back one index to
        # select correct occupation
        elif currentTotal > randNum:
            generatedOccupationIndex -= 1
            break
        # if current total is exactly the randNum
        # then the current index is the correct occupation
        else:
            break
    return getKeyByValue(dictionary, generatedOccupationIndex)


# ranges for jobs
# Management                                          0.0 <= n <= 6.1
# Business and Financial operations                   6.1  < n <= 11.1
# Computer and Mathematical                           11.1 < n <= 13.8
# Architecture and Engineering                        13.8 < n <= 15.5
# "Life, Physical and Social Science"                 15.5 < n <= 16.4
# Community and Social Service                        16.4 < n <= 18.0
# Legal                                               18.0 < n <= 18.8
# "Education, training and library"                   18.8 < n <= 24.9
# "Arts, design, entertainment, sports and media"     24.9 < n <= 26.6
# Healthcare practioners and technical                26.6 < n <= 32.1
# Healthcare support                                  32.1 < n <= 34.9
# Protective service                                  34.9 < n <= 37.2
# Food preparation and serving                        37.2 < n <= 45.5
# Building and grounds cleaning and maintenance       45.5 < n <= 49.2
# Personal care and service                           49.2 < n <= 53.2
# Sales                                               53.2 < n <= 63.4
# Office and administrative support                   63.4 < n <= 78.5
# "Farming, fishing and forestry"                     78.5 < n <= 79.1
# Construction and extraction                         79.1 < n <= 83.4
# "Installation, maintenance and repair"              83.4 < n <= 87.2
# Production                                          87.2 < n <= 93.3
# Transportation and material moving                  93.3 < n <= 99.8


def main():
    dict = dictOfOccupations(listOfContent("occupations.csv"))
    print(dict)
    print("\n")
    print("This is your randomly generated occupation: " + randomOccupation(dict))

main()
