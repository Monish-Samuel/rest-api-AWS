from flask import Flask, render_template, request
import requests, json

app = Flask(__name__, template_folder='template')


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def matching_char():
    numb = request.form['number']
    url = "https://api.github.com/repos/MOnish-Samuel/rest-api/issues/"+numb

    payload = {}
    headers = {
        'Authorization': 'Bearer 412102ffa2f1dd81b165427dfb7ce29b3592ea7b',
        'Cookie': '_octo=GH1.1.906356758.1615379192; logged_in=no'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    order = response.json()
    return render_template('pass1.html', r=order)


if __name__ == '__main__':
    app.run(debug=True)
