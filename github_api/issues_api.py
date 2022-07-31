from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth
import requests, os, json

app = Flask(__name__, template_folder='templates')
auth=HTTPBasicAuth()
tok= os.getenv('GITHUB_API_TOKEN')

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
    ticketState='open' if (request.form.get('state')==None or request.form.get('state')=="") else request.form.get('state')
    url = "https://api.github.com/repos/Monish-Samuel/rest-api/issues?state="+ticketState
    payload = ""
    headers = {
        'Authorization': f'Bearer {tok}'
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()
    

    newFileStart= """<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Result</title>
    </head>
    <body>
    <table style="border-collapse: collapse; width: 100%; height: 36px;" border="1">
    <tbody>
    <tr style="height: 18px;">
    <th style="width: 25%; text-align: center; height: 18px;"><strong>Issue Number</strong></th>
    <th style="width: 25%; text-align: center; height: 18px;"><strong>Issue Title</strong></th>
    <th style="width: 25%; text-align: center; height: 18px;"><strong>Opened By</strong></th>
    <th style="width: 25%; text-align: center; height: 18px;"><strong>State</strong></th>
    """
    newHtml= open('templates/table.html','w')
    newHtml.write(newFileStart)
    newHtml.close()

    for rowData in response:
        data= json.dumps(rowData)
        finalData=json.loads(data)
        newFileMid="</tr>\n<tr style=\"height: 18px;\">\n<td style=\"width: 25%; height: 18px; text-align: center;\">"+str(finalData['number'])+"</td>\n<td style=\"width: 25%; height: 18px; text-align: center;\">"+finalData['title']+"</td>\n<td style=\"width: 25%; height: 18px; text-align: center;\">"+finalData['user']['login']+"</td>\n<td style=\"width: 25%; height: 18px; text-align: center;\">"+finalData['state']+"</td>\n</tr>"
        newHtml= open('templates/table.html','a')
        newHtml.write(newFileMid)
        newHtml.close()

    newFileEnd="""
    </tbody>
    </table>
    </body>
    </html>
    """
    newHtml= open('templates/table.html','a')
    newHtml.write(newFileEnd)
    newHtml.close()
    
    return render_template('table.html')


@app.route('/create', methods=['POST'])

def issue_creator():
    title = request.form['title']
    body = request.form['issue']
    url = "https://api.github.com/repos/Monish-Samuel/rest-api/issues"

    payload = "{\r\n    \"title\": \""+title+"\",\r\n    \"body\": \""+body+"\"\r\n}"
    headers = {
        'Authorization': f'Bearer {tok}',
        'Content-Type': 'application/json'
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
        'Authorization': f'Bearer {tok}',
        'Content-Type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload).json()
    return render_template('pass1.html', r=response)

# @app.route('/dashboard', methods=['POST'])
# def devopsDashboard():
#     url = "https://api.github.com/repos/Monish-Samuel/rest-api/issues/"
#     payload = {}
#     headers = {
#         'Authorization': f'Bearer {tok}'
#     }

#     response = requests.request("GET", url, headers=headers, data=payload).json()
#     return render_template('pass1.html', r=response)


@auth.verify_password
def verify_password(username,password):
    if (username=='testUser' and password=='testPassword'):
        return True
    else:
        return False  

if __name__ == '__main__':
    app.run()
