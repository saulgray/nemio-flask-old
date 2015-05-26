from flask import Flask, render_template, jsonify
from urllib2 import urlopen
import json
from json import load
import requests



app = Flask(__name__)

@app.route('/')
def home():
    urlNEMBEX = 'http://nembex.nem.ninja/api/stats/nodes'
    urlNEMBEX2 = 'http://212.18.233.57:7890/chain/height'
    urlPOLO = 'https://poloniex.com/public?command=returnTicker'

    try:
        heightResponse = requests.get(urlNEMBEX2)
    except requests.ConnectionError:
        finalHeight = 'FAILED'
    heightResponseJ = heightResponse.text
    jsonHeight = json.loads(heightResponseJ)
    #add 10 blocks to account for NEMBEX lag + 10
    finalHeight = int(jsonHeight['height'])

    # response = urlopen(urlNEMBEX2)
    # jsonHeight = load(response)
    # #add 10 blocks to account for NEMBEX lag
    # finalHeight = int(jsonHeight['height']) + 10
    #
    # response2 = urlopen(urlNEMBEX)
    # jsonNodes = load(response2)
    # nodeCounter = 0
    # for nodes in jsonNodes['nodes']:
    #     nodeCounter += 1
    #
    response3 = urlopen(urlPOLO)
    jsonPrice = load(response3)
    priceXEM = float(jsonPrice['BTC_XEM']['last'])
    priceXEM *= 100000000 #100,000,000
    finalPriceXEM = ("%.0f" % priceXEM)

    # uri = "https://api.stackexchange.com/2.0/users?   order=desc&sort=reputation&inname=fuchida&site=stackoverflow"
    # try:
    #     uResponse = requests.get(uri)
    # except requests.ConnectionError:
    #    return "Connection Error"
    # Jresponse = uResponse.text
    # data = json.loads(Jresponse)
    #
    # displayName = data['items'][0]['display_name']# <-- The display name
    # reputation = data['items'][0]['reputation']# <-- The reputation

    # return Jresponse

    return render_template('home.html', Jresponse=finalHeight, jPrice=finalPriceXEM)


@app.route('/faq')
def about():
  return render_template('faq.html')

if __name__ == '__main__':
  app.run(debug=True)
