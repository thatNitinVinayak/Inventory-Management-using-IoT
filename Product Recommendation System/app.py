import pandas as pd
from flask import Flask, render_template, request
from flask_cors import CORS

UPLOAD_FOLDER = 'D:/NI7IN/Inventory-Management-using-IoT/Product Recommendation System'

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

products_prob = pd.read_csv("theProducts.csv")

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