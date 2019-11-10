from flask import Flask, render_template, request, json, url_for, redirect
import requests

app = Flask(__name__)

@app.route("/")
@app.route("/search", methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        code = request.form['code']
        return redirect(url_for('home', code=code))

    return render_template('search.html')


@app.route("/home/<code>")
def home(code):
    params = {
        'Authorization' : 'Bearer 8lLSKb6YF7zz8L1cXAN5eSAY5tVK'
    }

    r = requests.get(f'https://test.api.amadeus.com/v1/reference-data/locations?subType=AIRPORT,CITY&keyword={code}', headers=params)
    

    _list = json.loads(r.text)['data']

    seen = set()
    result = []
    for item in _list:
        if item['subType'] == "AIRPORT" and item['name'] not in seen:
            seen.add(item['name'])
            result.append(item)

    if not result:
        return "<h1>No Airports Found</h1>"
    
    result = sorted(result, key=lambda k: k['address']['countryName'])  # Sort by country name    
    return render_template('home.html', var=result, code=code.upper())


if __name__ == '__main__':
    app.run(debug=True)