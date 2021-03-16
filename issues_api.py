from flask import Flask, render_template, request
import requests

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/home', methods=['POST'])
def home_redirect_view():
    if request.form.get("view.html"):
        return render_template('view.html')
    elif request.form.get("update.html"):
        return render_template('update.html')
    else:
        return render_template('create.html')


@app.route('/view', methods=['POST'])
def issue_viewer():
    numb1 = request.form['number']
    url = "https://api.github.com/repos/Monish-Samuel/rest-api/issues/"+numb1
    payload = {}
    headers = {
        'Authorization': 'Bearer 3b2dae32edb4f80ac73f2fe5e624123a1b53e6dd',
        'Cookie': '_octo=GH1.1.906356758.1615379192; logged_in=no'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    return render_template('pass1.html', r=response)


@app.route('/create', methods=['POST'])
def issue_creator():
    title = request.form['title']
    body = request.form['issue']
    url = "https://api.github.com/repos/Monish-Samuel/rest-api/issues"

    payload = "{\r\n    \"title\": \""+title+"\",\r\n    \"body\": \""+body+"\"\r\n}"
    headers = {
        'Authorization': 'Bearer 3b2dae32edb4f80ac73f2fe5e624123a1b53e6dd',
        'Content-Type': 'application/json',
        'Cookie': '_octo=GH1.1.906356758.1615379192; logged_in=no'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    return render_template('pass1.html', r=response)


@app.route('/update', methods=['POST'])
def issue_updater():
    numb = request.form['number']
    title = request.form['title']
    body = request.form['issue']
    url = "https://api.github.com/repos/Monish-Samuel/rest-api/issues/"+numb

    payload = "{\r\n    \"title\": \""+title+"\",\r\n    \"body\": \""+body+"\"\r\n}"
    headers = {
        'Authorization': 'Bearer 3b2dae32edb4f80ac73f2fe5e624123a1b53e6dd',
        'Content-Type': 'application/json',
        'Cookie': '_octo=GH1.1.906356758.1615379192; logged_in=no'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload).json()
    return render_template('pass1.html', r=response)


if __name__ == '__main__':
    app.run(debug=True)
