from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)
target = os.path.join(app.static_folder, 'theProducts.csv')
theData = pd.read_csv(target)
 
@app.route('/')
def index():
    return render_template('index.html')
 
'''
@app.route('/show_data',  methods=("POST", "GET"))
def showData():
    theData_html = theData.to_html()
    return render_template('show_csv_data.html', data = theData_html)
'''

if __name__=='__main__':
    app.run(debug = True)