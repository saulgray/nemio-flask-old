from flask import Flask, render_template, jsonify
from urllib2 import urlopen
import json
from json import load
import requests

app = Flask(__name__)


@app.route("/")
def template_test():

    uri = "https://api.stackexchange.com/2.0/users?   order=desc&sort=reputation&inname=fuchida&site=stackoverflow"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    displayName = data['items'][0]['display_name']# <-- The display name
    reputation = data['items'][0]['reputation']# <-- The reputation

    return render_template('template.html', Jresponse=Jresponse, my_list=[0,1,2,3,4,5])


if __name__ == '__main__':
    app.run(debug=True)
