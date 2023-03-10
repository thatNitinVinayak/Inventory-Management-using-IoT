import pandas as pd
import os
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
products_prob = pd.read_csv( os.path.join(app.root_path, "uploads","theProducts.csv"))
def recommend(prod, n):
    basket = prod
    no_of_suggestions = n
    all_of_basket = products_prob[basket]
    all_of_basket = all_of_basket.sort_values(ascending=False)
    productRecommendations_to_shopkeepers = list(all_of_basket.index[:no_of_suggestions])
    print('You Might Consider Restocking : ', productRecommendations_to_shopkeepers)
    output=[]
    for i in productRecommendations_to_shopkeepers:
        output.append(products_prob.loc[i,'Unnamed: 0'])
    return (output)

@app.route('/', methods = ["GET", "POST"])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)