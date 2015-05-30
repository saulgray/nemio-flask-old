from flask import Flask, render_template, jsonify
from urllib2 import urlopen
import urllib
import json
from json import load
import requests



app = Flask(__name__)

@app.route('/')
def home():

    # urlVersion = 'http://bob.nem.ninja/version.json'
    # urlHeight = 'http://37.59.120.16:7890/chain/height'
    # urlNodes = 'http://37.59.120.16:7890/node/peer-list/all'
    # urlPolo = 'https://poloniex.com/public?command=returnTicker'
    #
    # poloStatus = urllib.urlopen(urlPolo).getcode()
    # versionStatus = urllib.urlopen(urlVersion).getcode()
    # heightStatus = urllib.urlopen(urlHeight).getcode()
    # nodeStatus = urllib.urlopen(urlNodes).getcode()
    #
    # if (poloStatus|versionStatus|heightStatus|nodeStatus) != 200:
    #     print 'Stats will not be displayed, a site is down.'
    # else:
    #     print 'hellllllo'
    #     heightResponse = requests.get(urlHeight)
    #     heightResponseJ = heightResponse.text
    #     jsonHeight = json.loads(heightResponseJ)
    #     finalHeight = int(jsonHeight['height'])
    #
    #
    #     response3 = urlopen(urlPolo)
    #     jsonPrice = load(response3)
    #     priceXEM = float(jsonPrice['BTC_XEM']['last'])
    #     priceXEM *= 100000000 #100,000,000
    #     finalPriceXEM = ("%.0f" % priceXEM)
    #
    #     versionResponse = requests.get(urlVersion)
    #     versionResponseJ = versionResponse.text
    #     jsonVersion = json.loads(versionResponseJ)
    #     finalVersion = jsonVersion['stable']

    return render_template('home.html')

    # jHeight=finalHeight, jPrice=finalPriceXEM, jVersion=finalVersion

    # Below code does not work yet
        #     nodeResponse = requests.get(urlNodes)
        #     nodeResponseJ = nodeResponse.text
        #     jsonNode = json.loads(nodeResponseJ)
        #     nodeCounter = 0
        #     for active in jsonNode['active']['endpoint']['protocol']:
        #         nodeCounter += 1
        #     print jsonNode


@app.route('/faq')
def faq():
  return render_template('faq.html')

@app.route('/install')
def install():
  return render_template('install.html')


if __name__ == '__main__':
  app.run(debug=True,port=1338)
