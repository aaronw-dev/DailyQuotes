from flask import Flask, render_template
import urllib.request
import json
from bs4 import BeautifulSoup
import requests
import os
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
def get_google_img(query):
    """
    gets a link to the first google image search result
    :param query: search query string
    :result: url string to first result
    """
    url = "https://www.google.com/search?q=" + str(query) + "&source=lnms&tbm=isch"
    headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    html = requests.get(url, headers=headers).text

    soup = BeautifulSoup(html, 'html.parser')
    with open("output.html", "w") as file:
        file.write(str(soup))
    image = soup.find("img",{"class":"yWs4tf"})

    if not image:
        return 
    print("I found an image!")
    return image['src']
    
app = Flask(__name__)

@app.route("/")
def main():
  
    result = json.load(urllib.request.urlopen("https://zenquotes.io/api/random"))
    print(result[0]["q"] + " \n-" + result[0]["a"] + "\n\n")

    '''    
    resultimage = get_google_img(result[0]["a"] + " face")
    urllib.request.urlretrieve(
    resultimage,
    "downloaded.png")
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open('downloaded.png', 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'rCyhnmo63dzwYDQzqoCRRhXd'},
    )
    if response.status_code == requests.codes.ok:
        with open( os.path.join("static", "headshot.png"), 'wb') as out:
            out.write(response.content)
            out.close()
    '''
    return render_template("index.html", quote=result[0]["q"], author=result[0]["a"])

app.run(host='0.0.0.0', port=5001, debug=False)