'''
Pig Latinizer Fact Mashup Script:

http://unkno.com (facts)
https://hidden-journey-62459.herokuapp.com/ (pig latin)

'''
import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)

latinizer = 'http://hidden-journey-62459.herokuapp.com/piglatinize/'

def get_fact():
    '''Returns a random fact from unkno.com'''

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    '''Returns a url with a pig-latinized fact'''
    fact = get_fact()
    payload = {'input_text': fact}
    response = requests.post(url=latinizer,data=payload)
    return response.url


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

