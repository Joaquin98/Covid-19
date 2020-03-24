import csv
import sys
import urllib
from matplotlib import pyplot as plt

deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv" 
confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

urllib.urlretrieve (deaths,"deaths.csv")
urllib.urlretrieve (confirmed,"confirmed.csv")

def get_deaths ():
    deathsDict = {}
    data = []
    with open('deaths.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range(5,len(row)):
                if row[i]=="":
                    row[i] = row[i-1]

            data.append(row[1:2] + row[4:])
        deathsDict["Dates"] = map (lambda x : "/".join(x.split("/")[0:2]) ,data[0][1:])
        for i in range(1,len(data)):
            name = data[i][0]
            if name not in deathsDict:
                deathsDict[name] = [0] * (len(data[i]) - 1)
            deathsDict[name] = [deathsDict[name][j] + int(data[i][j+1]) for j in range(0,len(data[0])-1)]
    return deathsDict

def get_confirmed ():
    confirmedDict = {}
    data = []
    with open('confirmed.csv','r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range(5,len(row)):
                if row[i]=="":
                    row[i] = row[i-1]
            data.append(row[1:2] + row[4:])
        confirmedDict["Dates"] = map (lambda x : "/".join(x.split("/")[0:2]) ,data[0][1:])
        for i in range(1,len(data)):
            name = data[i][0]
            if name not in confirmedDict:
                confirmedDict[name] = [0] * (len(data[i]) - 1)
            confirmedDict[name] = [confirmedDict[name][j] + int(data[i][j+1]) for j in range(0,len(data[0])-1)]
    return confirmedDict

def len_tuple(a):
    name,lis = a
    return len(lis)

def plot_list(opt,cList,f):

    data = []

    for country in cList:
        if opt[0] == "d":
            data.append((country,f(deathsDict[country])))
        if opt[0] == "c":
            data.append((country,f(confirmedDict[country])))
        if opt[0] == "dd":
            data.append((country,deathsDictDaily[country]))
        if opt[0] == "cd":
            data.append((country,confirmedDictDaily[country]))
    data.sort(key=len_tuple)
    
    if opt[1] == "time":
        dates = fullDates
    else :
        if opt[1] == "max":
            dates = ["Day " + str(i) for i in range(1,len_tuple(data[len(data)-1])+1)]
        else :
            dates = ["Day " + str(i) for i in range(1,len_tuple(data[0])+1)]

    for name,countryData in data:
        l = len(countryData)
        if opt[1] == "max":
            countryData = countryData + [float('nan')]*(len(dates)-len(countryData))
        else :
            countryData = countryData[:len(dates)]
        if opt[1] == "time":
            plt.plot(dates,countryData,label = name,marker='o',markersize=5)
        else :
            plt.plot(dates,countryData,label = name + " (Day 1: " + fullDates[-l] + ")" ,marker='o',markersize=5)


    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
    plt.xticks(rotation=-90)
    plt.show()


def replace_zeros (data):
    return map(lambda x : float('nan') if x == 0 else x,data)

def clean_zeros (data):
    return [x for x in data if x>0]

def get_daily (dataDict):
    dailyDict = {}
    for k,vc in dataDict.items():
        v = vc[:]
        if k =="Dates":
            continue
        r = range(1,len(v))
        map(int,v)
        r.reverse()
        for i in r:
            v[i] -= v[i-1]
            if v[i] == 0 and i<len(v)-1:
                v[i] = 4*v[i+1]/10
                v[i+1] = 6*v[i+1]/10
        dailyDict[k] = v
    return dailyDict

deathsDict = get_deaths()
deathsDictDaily = get_daily(deathsDict)
confirmedDict = get_confirmed()
confirmedDictDaily = get_daily(confirmedDict)
fullDates = deathsDict["Dates"]
option = (sys.argv[1],sys.argv[2])
countries = sys.argv[3:]
if option[1] == "time":
    plot_list(option,countries,replace_zeros)
else :
     plot_list(option,countries,clean_zeros)

