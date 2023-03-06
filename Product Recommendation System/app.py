import os
import pandas as pd
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'D:/NI7IN/Inventory-Management-using-IoT/Product Recommendation System/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

theProducts = pd.read_csv("theProducts.csv")

def recommend(prod, n):
    basket = prod
    no_of_suggestions = n
    all_of_basket = theProducts[basket]
    all_of_basket = all_of_basket.sort_values(ascending = False)
    suggestions_for_shopkeepers = list(all_of_basket.index[:no_of_suggestions])
    print('You May Consider Restocking : ', suggestions_for_shopkeepers)
    output = []
    for i in suggestions_for_shopkeepers:
        output.append(theProducts.loc[i,'Unnamed: 0'])
    return (output)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("./index.html")

if __name__== '__main__':
    app.run("localhost", "9999", debug = True)